# Encrypted Files Reference (age/rage)

> Personal quick-reference for working with `.age` encrypted files in this repo.
> Tool in use: **rage** (Rust impl of age format, scoop package `rage`, v0.11.2+).
> Passphrase-only mode — no keyfiles on disk. All passphrases live in Vaultwarden.

---

## Cheat sheet (most-used first)

### View a file without saving plaintext to disk
```powershell
rage -d <file>.age | less
```
- Prompts for passphrase, then pipes plaintext into `less`
- Plaintext lives only in memory / `less`'s pager buffer
- Quit `less` with `q` — gone, zero cleanup
- **This is the default way to read an encrypted file**

### Unlock + edit (creates a temp plaintext file on disk)
```powershell
rage -d <file>.age > <file>.md
# edit <file>.md in your editor
rage -e -p <file>.md -o <file>.age
Remove-Item <file>.md
```
- The decrypted `.md` exists on disk only between the first and last command
- Don't forget the final `Remove-Item` — that's the "re-lock" step

### Encrypt a brand-new file
```powershell
rage -e -p <file>.md -o <file>.md.age
Remove-Item <file>.md
```
- Prompts for passphrase twice (set + confirm)
- Delete plaintext only after verifying decryption works (see below)

### Decrypt to a specific output path
```powershell
rage -d <file>.age -o <output.md>
```
- Less common — usually you want stdout (`| less`) so nothing touches disk

---

## Always do this after encrypting a new file

Before deleting the plaintext, verify you can decrypt:

```powershell
rage -d <file>.age
```

If it prints the expected content to the terminal, the passphrase is right and the ciphertext is valid. **Only then** is it safe to `Remove-Item` the plaintext. Skipping this = potential permanent data loss if you mistyped the passphrase.

---

## Where passphrases live

- **Vaultwarden** (Bitwarden-compatible). Each encrypted file gets its own item.
- Naming convention used so far: `<Filename> encryption` (e.g. `AuDHD NavGuide encryption`).
- Passphrase generator settings: 32+ chars, all character classes (upper, lower, digits, specials).
- Never type a passphrase in a shell command directly — shell history can capture it. Use the interactive prompt (rage reads from the terminal, not args).

---

## Currently encrypted files in this repo

| File | Passphrase item name | Purpose |
|---|---|---|
| `b0ttsagent/NavGuides/AutismProfileNavGuide.md.age` | `AuDHD NavGuide encryption` | Personal autism/giftedness profile, locked because it contains raw mental-health Q&A |

(Add new rows here as you encrypt more files. Or don't — kept simple, this is your call.)

---

## Mental model

- **Locked state:** `.age` file on disk. Ciphertext. Useless to anyone without the passphrase. Safe in git, safe on lost laptop, safe from agents.
- **Unlocked state (read-only):** piped through `less` via `rage -d <file>.age | less`. Never touches disk. Vanishes when you quit `less`.
- **Unlocked state (editing):** plaintext `.md` exists temporarily on disk. You are responsible for deleting it after re-encrypting.
- **The `.age` file is the source of truth.** The plaintext is always a temporary artifact.

---

## Threat model (what this actually protects against)

Protects:
- Agents reading files via opencode tools (perm rules block, crypto guarantees)
- Someone grabbing your laptop, git repo, or backups — they get ciphertext, no passphrase
- Casual snooping / shoulder-surfing on the repo
- Brute-force attacks on the `.age` file (age uses scrypt N=2^17 — a 32+ char random passphrase is computationally uncrackable)

Does NOT protect against:
- Malware keylogging your passphrase as you type/paste it
- Someone compromising your Vaultwarden master password
- SSD wear-leveling leaving deleted plaintext bytes recoverable on the flash chip after `Remove-Item` (regular delete doesn't securely overwrite). For your current threat model this is fine; if you ever need forensic-grade destruction, that's a separate problem (full-disk encryption, physical destruction of the SSD).

If Vaultwarden loses the passphrase, the file is gone forever. There is no recovery.

---

## The opencode permission layer (defense in depth)

`/.opencode/opencode.json` has a `read: deny` rule for `**/AutismProfileNavGuide.md`. This is a soft policy — opencode respects it, but it's not cryptographic. The encryption is the real lock. The permission rule just stops agents from wasting tool calls trying to read a file that would be garbage anyway, and stops them from bugging you with prompts.

If you encrypt more sensitive nav guides, add similar rules:
```json
"read": {
  "**/AutismProfileNavGuide.md": "deny",
  "**/<OtherFile>.md": "deny"
}
```

---

## If something goes wrong

**"rage says `Error: incorrect passphrase or corrupted file`"**
- Either the passphrase is wrong (re-copy from Vaultwarden, watch for trailing whitespace) or the file got corrupted (rare — check git history for the `.age` file and try the previous version).

**"I encrypted a file but the `.age` is tiny / empty"**
- Check the plaintext file was the one you pointed rage at. Re-decrypt to verify.

**"rage isn't found in a new terminal"**
- `scoop install rage` should add it to PATH. If not, run `scoop update rage` or open a new terminal. rage lives at `~/scoop/apps/rage/current/bin/rage.exe`.

**"I deleted the plaintext before verifying decryption"**
- If the ciphertext was made correctly, you can still recover by decrypting it. If it wasn't (wrong passphrase, corrupted), the file is gone. This is why Step 4 (verify before delete) exists.

---

## Install (already done, here for reference)

```powershell
scoop install rage
rage --version  # should print rage 0.11.2 or newer
```

If you ever want the original Go `age` tool instead, the files are format-compatible — `age` and `rage` can decrypt each other's output. rage is just what's installed on this machine. (made by same developers)