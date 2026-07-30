# Model Override Strategies

## Finding Model Override Strings

Model refs use the format `PROVIDER_ID/MODEL_ID`. Find exact provider IDs and model IDs at [models.dev](https://models.dev).

---

## Quick Strategy Picker

| # | Strategy | Focus | GPT 5.5 + Opus 4.7 | DeepSeek Pro | Go Pro | Go Flash | Monthly Cost |
|---|----------|-------|---------------------|-------------|--------|----------|--------------|
| 1 | **[Budget Saver](#strategy-1-budget-saver)** | Save money, accept Flash quality on most agents | 0 | 8 | 3 | 24 | Go: ~15-20% |
| 2 | **[Balanced](#strategy-2-balanced)** | Best quality-per-dollar, no expensive models | 0 | 8 | 14 | 14 | Go: ~45-60% |
| 3 | **[Balanced + Brain](#strategy-3-balanced--brain)** | Balanced with GPT 5.5 planning + Opus 4.7 gate | 4 | 4 | 14 | 14 | Go: ~45-60% + ~$1-4/phase |
| 4 | **[Nuclear](#strategy-4-nuclear)** | Max quality, GPT 5.5 + Opus + Go Pro on everything | 4 | 4 | 21 | 7 | Go: ~70-90% + ~$1-4/phase |
| 5 | **[Max Subscription](#strategy-5-max-subscription)** | Burn Go budget for max quality, no GPT 5.5 | 0 | 3 | 25 | 7 | Go: ~80-100% |

---

## Agent Breakdown by Strategy

*Agents within each tier are ordered by importance — agents higher in the list benefit more from promotion to a higher model tier.*

| Strategy | GPT 5.5 | Opus 4.7 | DeepSeek Pro | Go Pro | Go Flash |
|----------|---------|----------|-------------|--------|----------|
| 1 - Budget Saver | — | — | <details><summary>8 agents</summary>• gsd-planner<br>• gsd-plan-checker<br>• gsd-code-reviewer<br>• gsd-verifier<br>• gsd-roadmapper<br>• gsd-debugger<br>• gsd-eval-planner<br>• general</details> | <details><summary>3 agents</summary>• gsd-executor<br>• gsd-phase-researcher<br>• gsd-project-researcher</details> | <details><summary>24 agents</summary>• gsd-code-fixer<br>• gsd-security-auditor<br>• gsd-integration-checker<br>• gsd-nyquist-auditor<br>• gsd-eval-auditor<br>• gsd-pattern-mapper<br>• gsd-codebase-mapper<br>• gsd-doc-synthesizer<br>• gsd-research-synthesizer<br>• gsd-doc-writer<br>• gsd-ui-researcher<br>• gsd-ui-auditor<br>• gsd-ai-researcher<br>• gsd-domain-researcher<br>• gsd-ui-checker<br>• gsd-debug-session-manager<br>• gsd-intel-updater<br>• gsd-doc-verifier<br>• gsd-doc-classifier<br>• gsd-assumptions-analyzer<br>• gsd-advisor-researcher<br>• gsd-framework-selector<br>• gsd-user-profiler<br>• explore</details> |
| 2 - Balanced | — | — | <details><summary>8 agents</summary>• gsd-planner<br>• gsd-plan-checker<br>• gsd-code-reviewer<br>• gsd-verifier<br>• gsd-roadmapper<br>• gsd-debugger<br>• gsd-eval-planner<br>• general</details> | <details><summary>14 agents</summary>• gsd-executor<br>• gsd-phase-researcher<br>• gsd-project-researcher<br>• gsd-code-fixer<br>• gsd-security-auditor<br>• gsd-integration-checker<br>• gsd-nyquist-auditor<br>• gsd-eval-auditor<br>• gsd-pattern-mapper<br>• gsd-codebase-mapper<br>• gsd-doc-synthesizer<br>• gsd-research-synthesizer<br>• gsd-ui-researcher<br>• gsd-ui-auditor</details> | <details><summary>14 agents</summary>• gsd-doc-writer<br>• gsd-ai-researcher<br>• gsd-domain-researcher<br>• gsd-ui-checker<br>• gsd-debug-session-manager<br>• gsd-intel-updater<br>• gsd-doc-verifier<br>• gsd-doc-classifier<br>• gsd-assumptions-analyzer<br>• gsd-advisor-researcher<br>• gsd-framework-selector<br>• gsd-user-profiler<br>• explore</details> |
| 3 - Balanced + Brain | <details><summary>3 agents</summary>• gsd-planner<br>• gsd-roadmapper<br>• general</details> | <details><summary>1 agent</summary>• gsd-plan-checker</details> | <details><summary>4 agents</summary>• gsd-code-reviewer<br>• gsd-verifier<br>• gsd-debugger<br>• gsd-eval-planner</details> | <details><summary>14 agents</summary>• gsd-executor<br>• gsd-phase-researcher<br>• gsd-project-researcher<br>• gsd-code-fixer<br>• gsd-security-auditor<br>• gsd-integration-checker<br>• gsd-nyquist-auditor<br>• gsd-eval-auditor<br>• gsd-pattern-mapper<br>• gsd-codebase-mapper<br>• gsd-doc-synthesizer<br>• gsd-research-synthesizer<br>• gsd-ui-researcher<br>• gsd-ui-auditor</details> | <details><summary>14 agents</summary>• gsd-doc-writer<br>• gsd-ai-researcher<br>• gsd-domain-researcher<br>• gsd-ui-checker<br>• gsd-debug-session-manager<br>• gsd-intel-updater<br>• gsd-doc-verifier<br>• gsd-doc-classifier<br>• gsd-assumptions-analyzer<br>• gsd-advisor-researcher<br>• gsd-framework-selector<br>• gsd-user-profiler<br>• explore</details> |
| 4 - Nuclear | <details><summary>3 agents</summary>• gsd-planner<br>• gsd-roadmapper<br>• general</details> | <details><summary>1 agent</summary>• gsd-plan-checker</details> | <details><summary>4 agents</summary>• gsd-code-reviewer<br>• gsd-verifier<br>• gsd-debugger<br>• gsd-eval-planner</details> | <details><summary>21 agents</summary>• gsd-executor<br>• gsd-phase-researcher<br>• gsd-project-researcher<br>• gsd-code-fixer<br>• gsd-security-auditor<br>• gsd-integration-checker<br>• gsd-nyquist-auditor<br>• gsd-eval-auditor<br>• gsd-pattern-mapper<br>• gsd-codebase-mapper<br>• gsd-doc-synthesizer<br>• gsd-research-synthesizer<br>• gsd-doc-writer<br>• gsd-ui-researcher<br>• gsd-ui-auditor<br>• gsd-ai-researcher<br>• gsd-domain-researcher<br>• gsd-ui-checker<br>• gsd-debug-session-manager<br>• gsd-intel-updater</details> | <details><summary>7 agents</summary>• gsd-doc-verifier<br>• gsd-doc-classifier<br>• gsd-assumptions-analyzer<br>• gsd-advisor-researcher<br>• gsd-framework-selector<br>• gsd-user-profiler<br>• explore</details> |
| 5 - Max Subscription | — | — | <details><summary>3 agents</summary>• gsd-planner<br>• gsd-plan-checker<br>• general</details> | <details><summary>25 agents</summary>• gsd-executor<br>• gsd-code-reviewer<br>• gsd-verifier<br>• gsd-roadmapper<br>• gsd-debugger<br>• gsd-eval-planner<br>• gsd-phase-researcher<br>• gsd-project-researcher<br>• gsd-code-fixer<br>• gsd-security-auditor<br>• gsd-integration-checker<br>• gsd-nyquist-auditor<br>• gsd-eval-auditor<br>• gsd-pattern-mapper<br>• gsd-codebase-mapper<br>• gsd-doc-synthesizer<br>• gsd-research-synthesizer<br>• gsd-doc-writer<br>• gsd-ui-researcher<br>• gsd-ui-auditor<br>• gsd-ai-researcher<br>• gsd-domain-researcher<br>• gsd-ui-checker<br>• gsd-debug-session-manager<br>• gsd-intel-updater</details> | <details><summary>7 agents</summary>• gsd-doc-verifier<br>• gsd-doc-classifier<br>• gsd-assumptions-analyzer<br>• gsd-advisor-researcher<br>• gsd-framework-selector<br>• gsd-user-profiler<br>• explore</details> |

---

## Strategy 1: Budget Saver

### Summary

Best for saving money. Puts everything you can on Flash (9x cheaper than Pro on Go). Critical planning/verification/review agents plus `general` get DeepSeek Pro. Executor and researchers stay on Go Pro because poor quality there cascades into rework. Everything else on Flash.

### `opencode.json` model overrides

```json
"agent": {
    "gsd-roadmapper": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-planner": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-plan-checker": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-code-reviewer": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-verifier": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-debugger": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-eval-planner": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-executor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-phase-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-project-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-code-fixer": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-nyquist-auditor": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-eval-auditor": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-integration-checker": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-security-auditor": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-doc-writer": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-doc-synthesizer": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-doc-classifier": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-doc-verifier": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-assumptions-analyzer": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-advisor-researcher": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-framework-selector": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-user-profiler": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-pattern-mapper": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-intel-updater": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-codebase-mapper": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-research-synthesizer": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-ai-researcher": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-domain-researcher": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-ui-researcher": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-ui-auditor": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-ui-checker": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-debug-session-manager": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "explore": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "general": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    }
}
```

---

## Strategy 2: Balanced

### Summary

Best quality-per-dollar without GPT 5.5 or Opus. DeepSeek Pro on all 8 critical planning/review agents plus `general`. Go Pro on everything where poor quality causes rework. Flash only on mechanical agents where mistakes are self-correcting. **No expensive pay-per-token models.**

### `opencode.json` model overrides

```json
"agent": {
    "gsd-roadmapper": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-planner": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-plan-checker": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-code-reviewer": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-verifier": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-debugger": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-eval-planner": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-executor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-phase-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-project-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-code-fixer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-nyquist-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-eval-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-integration-checker": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-security-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-pattern-mapper": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-doc-synthesizer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-research-synthesizer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-codebase-mapper": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-ui-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-ui-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-doc-classifier": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-doc-verifier": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-assumptions-analyzer": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-advisor-researcher": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-framework-selector": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-user-profiler": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-ai-researcher": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-domain-researcher": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-doc-writer": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-ui-checker": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-debug-session-manager": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-intel-updater": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "explore": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "general": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    }
}
```

---

## Strategy 3: Balanced + Brain

### Summary

Strategy 2's efficient foundation with 4 high-end models on the most leveraged agents. GPT 5.5 handles planning and `general`. Opus 4.7 handles adversarial plan checking. DeepSeek Pro covers review, verification, debugging, and eval planning. Everything else matches Strategy 2.

**Cross-model review advantage:** Plan-checker uses Opus 4.7 — a different model from the planner (GPT 5.5). Same-model review shares blind spots; cross-model adversarial review catches what your planner missed.

### `opencode.json` model overrides

```json
"agent": {
    "gsd-roadmapper": {
        "model": "open-router/gpt-5.5",
        "reasoning": "high"
    },
    "gsd-planner": {
        "model": "open-router/gpt-5.5",
        "reasoning": "high"
    },
    "gsd-plan-checker": {
        "model": "open-router/opus-4.7",
        "reasoning": "high"
    },
    "gsd-code-reviewer": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-verifier": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-debugger": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-eval-planner": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-executor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-phase-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-project-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-code-fixer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-nyquist-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-eval-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-integration-checker": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-security-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-pattern-mapper": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-doc-synthesizer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-research-synthesizer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-codebase-mapper": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-ui-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-ui-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-doc-classifier": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-doc-verifier": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-assumptions-analyzer": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-advisor-researcher": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-framework-selector": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-user-profiler": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-ai-researcher": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-domain-researcher": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-doc-writer": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-ui-checker": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-debug-session-manager": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-intel-updater": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "explore": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "general": {
        "model": "open-router/gpt-5.5",
        "reasoning": "high"
    }
}
```

---

## Strategy 4: Nuclear

### Summary

GPT 5.5 on planning and `general`. Opus 4.7 on plan-checking (cross-model adversarial review). DeepSeek Pro on remaining reviewers. Go Pro on execution and everything else substantial. Only 7 purely mechanical agents run Flash.

### `opencode.json` model overrides

```json
"agent": {
    "gsd-roadmapper": {
        "model": "open-router/gpt-5.5",
        "reasoning": "high"
    },
    "gsd-planner": {
        "model": "open-router/gpt-5.5",
        "reasoning": "high"
    },
    "gsd-plan-checker": {
        "model": "open-router/opus-4.7",
        "reasoning": "high"
    },
    "gsd-code-reviewer": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-verifier": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-debugger": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-eval-planner": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-executor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-phase-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-project-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-code-fixer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-nyquist-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-eval-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-integration-checker": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-security-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-doc-writer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-doc-synthesizer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-research-synthesizer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-intel-updater": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-pattern-mapper": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-codebase-mapper": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-ai-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-domain-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-ui-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-ui-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-ui-checker": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-debug-session-manager": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-doc-classifier": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-doc-verifier": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-assumptions-analyzer": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-advisor-researcher": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-framework-selector": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-user-profiler": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "explore": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "general": {
        "model": "open-router/gpt-5.5",
        "reasoning": "high"
    }
}
```

---

## Strategy 5: Max Subscription

### Summary

Extracts maximum value from your $10/month Go subscription. Everything meaningful runs on Go Pro. Only 7 mechanical agents stay on Flash. Three agents on DeepSeek API as safety valve (if you hit Go's 5-hour rolling limit, planning still works).

### `opencode.json` model overrides

```json
"agent": {
    "gsd-planner": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-plan-checker": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-roadmapper": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-code-reviewer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-verifier": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-debugger": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-eval-planner": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-executor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-phase-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-project-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-code-fixer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-nyquist-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-eval-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-integration-checker": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-security-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-doc-writer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-doc-synthesizer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-research-synthesizer": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-intel-updater": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-pattern-mapper": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-codebase-mapper": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-ai-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-domain-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-ui-researcher": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-ui-auditor": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-ui-checker": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-debug-session-manager": {
        "model": "opencode-go/deepseek-v4-pro",
        "reasoning": "max"
    },
    "gsd-doc-classifier": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-doc-verifier": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-assumptions-analyzer": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-advisor-researcher": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-framework-selector": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "gsd-user-profiler": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "explore": {
        "model": "opencode-go/deepseek-v4-flash",
        "reasoning": "high"
    },
    "general": {
        "model": "deepseek/deepseek-v4-pro",
        "reasoning": "max"
    }
}
```

---

## Model Key

| Model ID | Provider | Cost to you |
|----------|----------|-------------|
| `open-router/gpt-5.5` | OpenRouter | ~$15-25/M tokens (pay-per-token) |
| `open-router/opus-4.7` | OpenRouter | ~$15/M tokens (pay-per-token) |
| `deepseek/deepseek-v4-pro` | DeepSeek API | Your own DeepSeek API key |
| `opencode-go/deepseek-v4-pro` | OpenCode Go ($10/mo) | 17,150 req/month (subscription) |
| `opencode-go/deepseek-v4-flash` | OpenCode Go ($10/mo) | 158,150 req/month (subscription) |
