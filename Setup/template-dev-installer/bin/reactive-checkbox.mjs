// ── reactive-checkbox ───────────────────────────────────────────────
// Custom @inquirer/core prompt that wraps the standard checkbox
// behavior but adds a reactive "All" choice:
//
//   • Space on "All" → toggles all other choices to match
//   • Space on any other while "All" is checked → unchecks "All"
//   • Manually checking all others → auto-checks "All"
//   • 'a' (toggle all) updates "All" accordingly
//   • 'i' (invert) updates "All" accordingly
//
// Matches the locally installed @inquirer/checkbox v2.5.0 API
// (yoctocolors-cjs, ansi-escapes, theme v2 structure).
// ────────────────────────────────────────────────────────────────────

import {
  createPrompt,
  useState,
  useKeypress,
  usePrefix,
  usePagination,
  useMemo,
  useRef,
  makeTheme,
  isUpKey,
  isDownKey,
  isSpaceKey,
  isNumberKey,
  isEnterKey,
  ValidationError,
  Separator,
} from "@inquirer/core";
import pc from "yoctocolors-cjs";
import figures from "@inquirer/figures";
import ansiEscapes from "ansi-escapes";

// ── Theme (mirrors @inquirer/checkbox v2.5.0 defaults) ─────────────

const checkboxTheme = {
  icon: {
    checked: pc.green(figures.circleFilled),
    unchecked: figures.circle,
    cursor: figures.pointer,
  },
  style: {
    disabledChoice: (text) => pc.dim(`- ${text}`),
    renderSelectedChoices: (selectedChoices) =>
      selectedChoices.map((choice) => choice.short).join(", "),
    description: (text) => pc.cyan(text),
  },
  helpMode: "auto",
};

// ── "All" helpers ───────────────────────────────────────────────────

function findAllIndex(items) {
  return items.findIndex((item) => !Separator.isSeparator(item) && item.isAll);
}

/**
 * Reconcile "All" after individual toggles.
 * If every non-All selectable item is checked → "All" becomes checked.
 * Otherwise → "All" becomes unchecked.
 */
function reconcileAll(items) {
  const allIdx = findAllIndex(items);
  if (allIdx === -1) return items;

  const nonAllSelectable = items.filter(
    (item, i) => i !== allIdx && isSelectable(item),
  );
  const allChecked = nonAllSelectable.length > 0 &&
    nonAllSelectable.every((item) => item.checked);

  const allItem = items[allIdx];
  if (allItem.checked === allChecked) return items;

  const updated = [...items];
  updated[allIdx] = { ...allItem, checked: allChecked };
  return updated;
}

// ── Helpers (from @inquirer/checkbox v2.5.0) ────────────────────────

function isSelectable(item) {
  return !Separator.isSeparator(item) && !item.disabled;
}

function toggle(item) {
  return isSelectable(item) ? { ...item, checked: !item.checked } : item;
}

function check(checked) {
  return function (item) {
    return isSelectable(item) ? { ...item, checked } : item;
  };
}

function normalizeChoices(choices) {
  return choices.map((choice) => {
    if (Separator.isSeparator(choice)) return choice;

    if (typeof choice === "string") {
      return {
        value: choice,
        name: choice,
        short: choice,
        disabled: false,
        checked: false,
        isAll: false,
      };
    }

    const name = choice.name ?? String(choice.value);
    return {
      value: choice.value,
      name,
      short: choice.short ?? name,
      description: choice.description,
      disabled: choice.disabled ?? false,
      checked: choice.checked ?? false,
      isAll: choice.isAll ?? false,
    };
  });
}

// ── The prompt ──────────────────────────────────────────────────────

/**
 * A checkbox prompt with an optional reactive "All" choice.
 *
 * Usage is identical to @inquirer/checkbox, with one addition:
 * any choice with `{ isAll: true }` acts as a master selector.
 *
 * @example
 *   const answer = await reactiveCheckbox({
 *     message: "Select categories to install:",
 *     choices: [
 *       { name: "All", value: "all", isAll: true },
 *       new Separator(),
 *       { name: "Skills",   value: "skills" },
 *       { name: "OpenCode", value: "opencode" },
 *       { name: "Pi",       value: "pi" },
 *     ],
 *   });
 */
export default createPrompt((config, done) => {
  const {
    instructions,
    pageSize = 7,
    loop = true,
    required,
    validate = () => true,
  } = config;
  const theme = makeTheme(checkboxTheme, config.theme);
  const prefix = usePrefix({ theme });
  const firstRender = useRef(true);
  const [status, setStatus] = useState("pending");
  const [items, setItems] = useState(() => normalizeChoices(config.choices));

  const bounds = useMemo(() => {
    const first = items.findIndex(isSelectable);
    const last = items.findLastIndex(isSelectable);

    if (first < 0) {
      throw new ValidationError(
        "[checkbox prompt] No selectable choices. All choices are disabled.",
      );
    }

    return { first, last };
  }, [items]);

  const [active, setActive] = useState(bounds.first);
  const [showHelpTip, setShowHelpTip] = useState(true);
  const [errorMsg, setError] = useState();

  useKeypress(async (key) => {
    if (isEnterKey(key)) {
      const selection = items.filter((item) =>
        !Separator.isSeparator(item) && item.checked,
      );
      const isValid = await validate([...selection]);
      // "required" only counts non-All selectable items
      if (required && !items.some((item) => isSelectable(item) && !item.isAll && item.checked)) {
        setError("At least one choice must be selected");
      } else if (isValid === true) {
        setStatus("done");
        done(selection.map((choice) => choice.value));
      } else {
        setError(isValid || "You must select a valid value");
      }
    } else if (isUpKey(key) || isDownKey(key)) {
      if (
        loop ||
        (isUpKey(key) && active !== bounds.first) ||
        (isDownKey(key) && active !== bounds.last)
      ) {
        const offset = isUpKey(key) ? -1 : 1;
        let next = active;
        do {
          next = (next + offset + items.length) % items.length;
        } while (!isSelectable(items[next]));
        setActive(next);
      }
      if (errorMsg) setError(undefined);
    } else if (isSpaceKey(key)) {
      setShowHelpTip(false);
      const activeItem = items[active];

      if (activeItem && !Separator.isSeparator(activeItem) && activeItem.isAll) {
        // ── "All" toggled ────────────────────────────────────────
        setError(undefined);
        const newChecked = !activeItem.checked;
        const allIdx = findAllIndex(items);
        let updated = items.map((item, i) => {
          if (i === allIdx) return { ...item, checked: newChecked };
          if (isSelectable(item)) return { ...item, checked: newChecked };
          return item;
        });
        setItems(updated);
      } else {
        // ── Individual item toggled ──────────────────────────────
        setError(undefined);
        const newItems = items.map((choice, i) =>
          i === active ? toggle(choice) : choice,
        );
        setItems(reconcileAll(newItems));
      }
    } else if (key.name === "a") {
      // Toggle all non-All items
      const nonAll = items.filter(
        (item) => isSelectable(item) && !item.isAll,
      );
      const selectAll = nonAll.some((item) => !item.checked);

      const allIdx = findAllIndex(items);
      let updated = items.map((item, i) => {
        if (i === allIdx) return { ...item, checked: selectAll };
        if (isSelectable(item) && !item.isAll) {
          return { ...item, checked: selectAll };
        }
        return item;
      });
      setItems(updated);
    } else if (key.name === "i") {
      // Invert all non-All items, then reconcile All
      const allIdx = findAllIndex(items);
      let updated = items.map((item, i) => {
        if (i === allIdx || !isSelectable(item)) return item;
        return toggle(item);
      });
      updated = reconcileAll(updated);
      setItems(updated);
    } else if (isNumberKey(key)) {
      const position = Number(key.name) - 1;
      const item = items[position];
      if (item != null && isSelectable(item)) {
        setActive(position);
        setShowHelpTip(false);
        if (item.isAll) {
          const newChecked = !item.checked;
          const allIdx = findAllIndex(items);
          let updated = items.map((item, i) => {
            if (i === allIdx) return { ...item, checked: newChecked };
            if (isSelectable(item)) return { ...item, checked: newChecked };
            return item;
          });
          setItems(updated);
        } else {
          const newItems = items.map((choice, i) =>
            i === position ? toggle(choice) : choice,
          );
          setItems(reconcileAll(newItems));
        }
      }
    }
  });

  const message = theme.style.message(config.message);

  let description;
  const page = usePagination({
    items,
    active,
    renderItem({ item, isActive }) {
      if (Separator.isSeparator(item)) {
        return ` ${item.separator}`;
      }

      if (item.disabled) {
        const disabledLabel =
          typeof item.disabled === "string" ? item.disabled : "(disabled)";
        return theme.style.disabledChoice(`${item.name} ${disabledLabel}`);
      }

      if (isActive) {
        description = item.description;
      }

      const checkbox = item.checked ? theme.icon.checked : theme.icon.unchecked;
      const color = isActive ? theme.style.highlight : (x) => x;
      const cursor = isActive ? theme.icon.cursor : " ";
      return color(`${cursor}${checkbox} ${item.name}`);
    },
    pageSize,
    loop,
  });

  if (status === "done") {
    const selection = items.filter(
      (item) => !Separator.isSeparator(item) && item.checked,
    );
    const answer = theme.style.answer(
      theme.style.renderSelectedChoices(selection, items),
    );
    return `${prefix} ${message} ${answer}`;
  }

  let helpTipTop = "";
  let helpTipBottom = "";
  if (
    theme.helpMode === "always" ||
    (theme.helpMode === "auto" &&
      showHelpTip &&
      (instructions === undefined || instructions))
  ) {
    if (typeof instructions === "string") {
      helpTipTop = instructions;
    } else {
      const keys = [
        `${theme.style.key("space")} to select`,
        `${theme.style.key("a")} to toggle all`,
        `${theme.style.key("i")} to invert selection`,
        `and ${theme.style.key("enter")} to proceed`,
      ];
      helpTipTop = ` (Press ${keys.join(", ")})`;
    }

    if (
      items.length > pageSize &&
      (theme.helpMode === "always" ||
        (theme.helpMode === "auto" && firstRender.current))
    ) {
      helpTipBottom = `\n${theme.style.help("(Use arrow keys to reveal more choices)")}`;
      firstRender.current = false;
    }
  }

  const choiceDescription = description
    ? `\n${theme.style.description(description)}`
    : "";

  let error = "";
  if (errorMsg) {
    error = `\n${theme.style.error(errorMsg)}`;
  }

  return `${prefix} ${message}${helpTipTop}\n${page}${helpTipBottom}${choiceDescription}${error}${ansiEscapes.cursorHide}`;
});

export { Separator };
