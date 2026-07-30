# Handoff: WHEA BSOD — Q-Flash Plus F11 Flash Complete, Now in Post-Flash Verification

## Date
07-17-2026

## Summary

Continuation session of the B560 DS3H AC-Y1 BSOD 0x124 WHEA remediation (see prior handoff: `b0ttsagent/handoffs/07-16-2026/bsod-bios-update-plan.md`). This session executed the **Q-Flash Plus headless BIOS F4→F11 flash** (which succeeded where the prior Efiflash attempt hung) and entered the **post-flash verification + stabilization phase**.

Windows is now booting but hitting an **Automatic Repair loop** post-flash, and crashes haven't been ruled out yet. Diagnostics are being intentionally deferred until we observe whether the F11 flash + PCIe ASPM disable + PCIe Gen3 downshift actually stopped the WHEA crashes.

---

## What Was Completed This Session

| # | Action | Result |
|---|---|---|
| 1 | Verified F11 BIOS file + thumb drive present on laptop | `C:\Users\intel\AppData\Local\Temp\opencode\bios-f11\extracted\B560DS3HACY1.F11` (33,554,432 bytes) intact; `D:` thumb drive "BIOSF11" FAT32 14.55 GB mounted with 14.52 GB free. |
| 2 | Copied `B560DS3HACY1.F11` → `D:\GIGABYTE.bin` | Succeeded — 33,554,432 bytes on `D:\`. Original `B560DS3HACY1.F11` left alongside as backup (harmless). Driven by user instruction "you just gotta rename."
    Note: User later reported the file was "already on there" — the prior session's Efiflash-package copy was present. Q-Flash Plus filename requirement: uppercase `GIGABYTE`, lowercase `.bin`, case-sensitive (corrected from prior handoff typo "GIGABOTE.bin"). |
| 3 | Safely dismounted `D:` thumb drive | Succeeded. User unplugged and moved it to the Gigabyte PC. |
| 4 | Located Q-Flash Plus port + button on B560 DS3H AC (Rev 1.0) | **The Q-Flash Plus button is on the motherboard itself**, not the rear panel. Listed as Internal I/O Connector #16 ("1 x Q-Flash Plus button"). Per spec-page ordering, likely bottom edge near front panel header / Clear CMOS jumper.
    The **Q-Flash Plus USB port** is on the rear I/O — one of the two USB 2.0/1.1 ports (typically white-marked). USB 3.2 Gen1 ports (blue) are NOT the QF+ port. |
| 5 | Executed Q-Flash Plus flash (user-run on Gigabyte PC) | **SUCCEEDED.** User confirmed orange LED completed its cycle, flash complete. From session: "okay qflash finished now what." |
| 6 | User entered BIOS, F5 (Load Optimized Defaults) ran | Applied defaults as required post-flash. |
| 7 | Rebooted to Windows | **FAILED — Automatic Repair loop** ("Windows couldn't load correctly. Cancel or Repair."). Expected root cause: F5 wiped boot mode (CSM/Legacy toggle), Secure Boot state, boot order, and/or SATA mode — default config likely mismatching the UEFI/AHCI install. |

## Current State (where we left off)

- **Gigabyte PC**: Powered off, in Automatic Repair loop. Has F11 BIOS flashed + Load Optimized Defaults applied, but Windows boot config needs fixing in BIOS before it will boot.
- **Laptop (B0TTS, this machine)**: All prep complete. F11 BIOS ZIP + extracted files still at `C:\Users\intel\AppData\Local\Temp\opencode\bios-f11\`. Thumb drive (`D:` "BIOSF11") was the flasher — currently is NOT a Windows installer (was reformatted from Rufus installer to FAT32 BIOS flasher in the prior session).

### Pending decisions / open items

1. **Windows boot fix first** — user needs to fix BIOS boot config to get out of Automatic Repair loop. See plan Step 1 below.
2. **Crashes not yet assessed** — we don't know yet if F11 + ASPM-disabled + Gen3-downshift stabilized the crashes. The Automatic Repair loop is blocking that observation.
3. **Disk repair (`sfc`/`DISM`/`chkdsk`) is deferred** — user asked whether to run these now to fix any corrupted files from the 0x7a NVMe-read failures. **Explicit decision: NO, do not run them yet.** Detailed reasoning in Open Decision #1.
4. **BIOS settings to reconfigure** — F5 wiped XMP, boot order, Secure Boot, and all custom settings. User has NOT yet been guided through the full reconfiguration. PCIe ASPM disable + PCIe Gen3 downshift for the NVMe root port are key WHEA mitigations from prior research.
5. **Backup status unchanged** — still skipped (user "have most files I need"). External HDD ready if needed before SSD replacement.

---

## New Goals for Next Session

### Step 1: Fix the Automatic Repair loop (boot config)

Reboot, tap **DEL** at Gigabyte logo, and check these settings:

1. **Boot → CSM Support** → set to **Disabled** (UEFI only, no Legacy)
2. **Boot → Secure Boot** → **Disabled** (matches prior-session disabled state for Efiflash)
3. **Boot → Boot Option Priorities** → **Windows Boot Manager (NVMe WDC WDS100T2B0C)** = #1
4. **Settings → SATA Mode** → **AHCI** (not RAID/Optane/Intel RST)

Then **F10** → Save & Exit. If it still loops, the BCD may be corrupted (needs `bootrec` rebuild from WinPE/recovery command prompt — disk repair is secondary here).

### Step 2: Reconfigure remaining BIOS settings

- XMP (RAM profile)
- Boot order finalized
- Secure Boot (user's call)
- **Disable PCIe ASPM** (Power Management → PCIe ASPM = Disabled) — a known WHEA mitigation from prior research
- **Force NVMe root port to PCIe Gen3** (instead of Auto/Gen4) — resolves WHEA on some Gigabyte B560/B660 boards. Worth trying if crashes continue.
- IRST/RST disabled if you don't use Optane

### Step 3: Observe stabilization (NO disk repair yet)

Boot to Windows, use it normally for **a few hours to a day**, and confirm whether the crashes actually stopped. Check:

```powershell
# Confirm BIOS version
Get-CimInstance Win32_BIOS | Select-Object SMBIOSBIOSVersion, ReleaseDate

# Check for new WHEA errors since boot
Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-WHEA-Logger'} -MaxEvents 50
```

Three possible outcomes:
- **Cleans boot, no crashes** → F11 fix worked. Move to optional disk repair, then close.
- **Boots but crashes with WHEA (0x124) again** → F11 didn't fix it. **Skip disk repair** — go to Phase 2 (SSD firmware update, reseat, M.2 slot swap, SMART check).
- **Automatic Repair loop / Safe Mode only** → BCD/Windows install corrupted. Build a new Windows installer USB (Rufus + Media Creation Tool — thumb drive is currently a BIOS flasher, NOT the installer!) and rebuild BCD from the WinPE recovery command prompt via `bootrec` commands.

### Step 4 (conditional): Disk repair — ONLY if Windows is stable for a day

The user explicitly asked whether `sfc /scannow`, `DISM /Online /Cleanup-Image /RestoreHealth`, and `chkdsk C: /f /r` are safe to run now. **The answer is NO.** Run them **only after crashes have stopped** (confirm stabilization first), and in this safe order:

```powershell
1. chkdsk C: /f             # File system integrity first — fast
2. chkdsk C: /r             # Full sector scan — ONLY if /f found bad clusters; risky long scan
3. DISM /Online /Cleanup-Image /RestoreHealth   # Repairs WinSxS component store
4. sfc /scannow             # Replace corrupted system files
```

**Do not run all three at once or in a different order.**

### If crashes continue after F11 (Phase 2 — full hardware diagnostics)

These items from prior session are still pending:
- SSD firmware update via WD Dashboard
- Reseat the NVMe SSD (open the case — user hasn't done this yet)
- Try the other M.2 slot
- SMART check via CrystalDiskInfo / WD Dashboard
- Stress test (OCCT / IntelBurnTest)

### If Phase 2 doesn't fix it (Phase 3 — replacement)

- Replace the NVMe SSD
- RMA the motherboard if known-good SSD still WHEA-errors on Root Port #21

---

## Open Decisions

### 1. **DEFER disk repair (`sfc`/`DISM`/`chkdsk`) until after stabilization confirmed**

User asked when to run `sfc`, `DISM`, and `chkdsk` and whether it's safe to run them before confirming crashes are over. Decision: **NO — do not run them yet.** Reasoning:

- All three tools **hammer the NVMe SSD with heavy I/O** — exactly what triggers the WHEA crash (PCIe Root Port #21 → NVMe reads failing).
- A crash mid-run leaves Windows in a *worse* state:
  - `chkdsk C: /r` mid-run → NTFS file system itself can be left corrupt mid-write; could make C: unbootable (catastrophic).
  - `sfc /scannow` mid-run → half-written system file; Windows worse or broken.
  - `DISM /RestoreHealth` mid-run → `Pending.xml` corruption makes future operations fail; component store harder to fix.
- Prior session saw a **WHEA crash inside WinPE** (not just Windows) — proves the issue is below the OS layer the disk tools operate at. Disk repair tools won't help if the root cause is a hardware-layer PCIe fault.
- The 0x7a crashes (NVMe read failures) **could** have corrupted Windows files — that's why disk repair is on the list — but we need to confirm the NVMe is *actually stable* before trusting it with `chkdsk /r`'s full-sector rewrite cycles. Order matters: `chkdsk /f` → `chkdsk /r` (if `/f` finds bad clusters) → `DISM` → `sfc`.

### 2. Automatic Repair loop root cause

Unknown until user enters BIOS (per Step 1). Most likely candidates:
- CSM/Legacy boot enabled instead of UEFI (CSM support default probably toggled)
- Secure Boot state flipped from disabled (last session) to enabled/Setup mode
- Boot Order reset — no Windows Boot Manager entry on the list
- SATA Mode reset from AHCI to RAID/Optane — would break AHCI-installed Windows

### 3. PCIe ASPM + Gen3 downshift not yet applied

Step 2 — reconfigure BIOS — has not been done. ASPM disable + Gen3 downshift are the researched WHEA mitigations. Must be done during the BIOS reconfiguration pass.

### 4. Backup still skipped

User opted "flash-first" stating they have most files they need (prior session). External HDD (`H:` on Gigabyte, 931 GB NTFS, empty) is ready if needed before SSD replacement. The thumb drive is currently **not a Windows installer** — was reformatted to a BIOS flasher in the prior session; would need a fresh Rufus + Media Creation Tool rebuild for WinPE robocopy / BCD rebuild access.

---

## System Identification

| Component | Detail |
|---|---|
| Motherboard | Gigabyte B560 DS3H AC-Y1 (Rev 1.0) |
| BIOS | **F11** (flashed via Q-Flash Plus this session; Load Optimized Defaults applied — all custom settings wiped) |
| CPU | Intel 11th Gen (Tiger Lake-H), B560 chipset |
| Failing device | WDC WDS100T2B0C-00PXH0 (1TB NVMe SSD) at PCI bus 2 — `VEN_15B7&DEV_5009` |
| Failing root port | Intel PCIe Root Port #21 — `VEN_8086&DEV_43C4` |
| GPU | NVIDIA GeForce RTX 3060 (PEG10, separate port — not implicated) |
| WiFi | Intel Wi-Fi 7 BE200 |
| OS | Windows 11 build 26200 |
| Thumb drive | 14 GB, FAT32, label "BIOSF11" — holds `GIGABYTE.bin` + old Efiflash package files; **NOT a Windows installer anymore** |
| External HDD | 931 GB NTFS, label "BACKUP", empty, ready if needed before SSD replacement |
| Laptop (this machine) | Lenovo, hostname `B0TTS`, user `b0tts\intel`, disk 0 = WD PC SN740 1TB NVMe |

---

## Key Files, Paths, and Commands

| Item | Path / Command |
|---|---|
| Prior handoff (full diagnosis + remediation plan) | `b0ttsagent/handoffs/07-16-2026/bsod-bios-update-plan.md` |
| Source EVTX log (laptop) | `C:\Users\intel\DevelopmentProjectTemplate\EventViewerEvents.evtx` |
| F11 BIOS ZIP | `C:\Users\intel\AppData\Local\Temp\opencode\bios-f11\F11.zip` |
| F11 BIOS extracted | `C:\Users\intel\AppData\Local\Temp\opencode\bios-f11\extracted\B560DS3HACY1.F11` (33,554,432 bytes) |
| Thumb drive on laptop | `D:` — label "BIOSF11", FAT32, 14 GB — holds `GIGABYTE.bin` for Q-Flash Plus |
| Minidump directory (Gigabyte) | `C:\Windows\Minidump` (5 existing dumps: 6/8, 6/13x2, 6/14, 6/23) |
| Check BIOS version | `Get-CimInstance Win32_BIOS \| Select-Object SMBIOSBIOSVersion, ReleaseDate` |
| Check for new WHEA errors | `Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-WHEA-Logger'} -MaxEvents 50` |
| BCD rebuild (from WinPE cmd) | `bootrec /fixmbr` → `bootrec /fixboot` → `bootrec /scanos` → `bootrec /rebuildbcd` |
| Disk repair safe order (AFTER stabilization confirmed) | `chkdsk C: /f` → `chkdsk C: /r` (conditional) → `DISM /Online /Cleanup-Image /RestoreHealth` → `sfc /scannow` |
| Board manual (PDF) | `https://download.gigabyte.com/FileList/Manual/mb_manual_b560-ds3h-ac_e_1201.pdf` |
| QF+ button info (manual ex.) | Internal I/O Connector #16 — "1 x Q-Flash Plus button" — on the motherboard, NOT the rear panel |
| QF+ USB port info (manual ex.) | Rear I/O USB 2.0/1.1 Port labeled "Q-Flash Plus Port" — white-marked, NOT blue/USB 3.2 |

---

## Suggested Skills for Next Session

| Skill | Use when |
|---|---|
| `tutorial` | Resume step-by-step walkthrough through BIOS reconfiguration (Step 1 fix boot → Step 2 reconfigure → Step 3 stabilization) and conditional disk repair (Step 4). Current session used this skill. |
| `gsd-debug` | If F11 + ASPM disabled + Gen3 downshift doesn't fix the crashes and systematic hardware debugging is needed (SSD firmware, reseat, slot swap, stress test). |
| `grill-me` | If user wants to stress-test the "is it BIOS or SSD or root port motherboard?" decision before committing to SSD replacement or motherboard RMA. |
| `create-nav-guide` | After remediation is complete and stabilization confirmed, document the full WHEA diagnosis → Q-Flash Plus flash → recovery → final fix as a reference guide. |
| `create-planning-docs` | If Phase 2 / Phase 3 expands into a multi-phase hardware replacement project (e.g. SSD replacement → known-good test → motherboard RMA). |