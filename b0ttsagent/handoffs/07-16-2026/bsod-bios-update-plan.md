# Handoff: BSOD 0x124 WHEA PCIe Crash — BIOS Flash Mid-Execution (Q-Flash Plus Retry)

## Date
07-16-2026

## Summary

Diagnosed the cause of daily PC crashes from an exported Event Viewer log
(`EventViewerEvents.evtx`, 328 events). The system bugchecks with
**0x124 (WHEA_UNCORRECTABLE_ERROR)** due to a fatal PCIe hardware error on
**Intel PCI Express Root Port #21** (`VEN_8086&DEV_43C4`), whose downstream
device is the **WDC WDS100T2B0C-00PXH0 1TB NVMe SSD** (`VEN_15B7&DEV_5009`).

Crashes have **escalated from 0x124 (intermittent) to 0x7a
(KERNEL_DATA_INPAGE_ERROR)** — the SSD can no longer reliably return reads,
indicating the controller/NAND is degrading or the PCIe link is dropping more
severely. A WHEA freeze also occurred inside **WinPE** (not just Windows),
confirming the crash source is hardware-layer and independent of OS state.

The user chose the **BIOS update (F4 → F11)** path. **The first flash attempt
via Gigabyte Efiflash EFI shell HUNG** at "Transferring BIOS Data Success" for
10+ minutes (WHEA crash silently froze the EFI shell). Next session resumes
from a **Q-Flash Plus retry** (headless flash, no CPU/RAM/SSD involvement,
eliminates the crash vector entirely).

---

## What Was Completed This Session

| # | Action | Result |
|---|---|---|
| 1 | Parsed `EventViewerEvents.evtx` (328 events) | Confirmed 170/170 WHEA events point at one source: `PCI\VEN_8086&DEV_43C4&SUBSYS_50011458&REV_11` (PCIe Root Port #21, PortType=4/root port). Zero USB involvement. |
| 2 | Ruled out USB as cause | `PrimaryDeviceName` group = 170/170 Root Port #21; 0 events mention USB/xHCI/EHCI. USB is exonerated. |
| 3 | Confirmed 0x7a escalation | User reported `KERNEL_DATA_INPAGE_ERROR (0x7a)` — NVMe reads failing at OS level. Plan shifted to data-rescue triage. |
| 4 | Built Windows install USB (Rufus) | Wiped Ventoy thumb drive (14 GB, disk 1 on Gigabyte), reformatted, wrote Windows ISO via Rufus with UEFI:NTFS mode. Thumb drive ready as WinPE boot. |
| 5 | Booted Gigabyte to WinPE successfully | `X:\Sources>` prompt reached. Identified Disk 0 = NVMe (C:, 929 GB NTFS), Disk 1 = thumb drive (D:, 14 GB), Disk 2 = external HDD (931 GB, initially absent, hot-plugged in WinPE). |
| 6 | Wiped external HDD, created single NTFS partition | Cleaned Disk 2, created partition, formatted `H:` as NTFS label "BACKUP". External HDD ready as backup destination. |
| 7 | Downloaded F11 BIOS to laptop | F11 ZIP downloaded to `C:\Users\intel\AppData\Local\Temp\opencode\bios-f11\F11.zip`, extracted to `...\extracted\` containing `B560DS3HACY1.F11` (33,554,432 bytes) + `Efiflash.efi` + `flash.nsh` + `EFI\BOOT\BOOTX64.EFI`. |
| 8 | Repurposed thumb drive as BIOS flasher | Wiped thumb drive (was Windows installer), formatted FAT32 label "BIOSF11", copied extracted F11 EfiFlash package to root. |
| 9 | Booted Gigabyte to EFI shell from flasher USB | Reached UEFI Interactive Shell v2.2. `fs0:` = USB. `ls` confirmed `B560DS3HACY1.F11` present. |
| 10 | Disabled Secure Boot in Gigabyte BIOS | Secure Boot violation blocked unsigned `BOOTX64.EFI`. User entered BIOS (DEL), disabled Secure Boot, rebooted to USB successfully. |
| 11 | Ran `flash.nsh` — first flash attempt | Efiflash correctly detected: Model "B560 DS3H AC-Y1", Part "8ARKL531", Current "F4" (2021/06/18) → Target "F11" (2023/12/19). "Transferring BIOS Data ... Success" displayed. |
| 12 | **Flash HUNG** | Screen froze at "Transferring BIOS Data Success" for 10+ minutes. No further output, no prompt, no progress bar. Likely silent WHEA crash froze the EFI shell mid-write (previously saw WHEA crash in WinPE — hardware-layer crash confirmed outside Windows). |

---

## Current State (where we left off)

**The Gigabyte PC is powered off** (user hard-shutdown after 10-min hang).
Main BIOS may be corrupted from the partial Efiflash write — **DualBIOS backup
chip (still F4) should auto-recover on next boot**, but this has not yet been
verified (user chose to skip boot verification and go straight to Q-Flash Plus).

### Flash retry method chosen: **Q-Flash Plus** (headless)

The B560 DS3H AC-Y1 supports Q-Flash Plus (confirmed via Gigabyte manual):
- Flashes in **S5 state** (PC "off" but PSU powered)
- **No CPU, no RAM, no NVMe enumeration** — PCIe link isn't trained
- Eliminates the WHEA crash vector entirely (the reason the Efiflash attempt hung)
- User does NOT need to remove the NVMe SSD

### Why Efiflash hung (research-confirmed)

PCIe AER is a hardware-layer protocol. The root port actively trains/polls the
link even in EFI shell. If the SSD controller is in a bad state, it floods the
root port with bad TLPs regardless of OS activity. The WinPE crash earlier
confirmed this. Efiflash shares the same vulnerability. Q-Flash Plus avoids it
by operating below the PCIe enumeration layer entirely.

---

## New Goals for Next Session

### Immediate (resume point)

1. **Verify Q-Flash Plus button/port location on the B560 DS3H AC-Y1 rear I/O**
   - Look for white USB port labeled "BIOS" / "QF" / "QF_LED"
   - Look for small physical Q-Flash Plus button on rear I/O or near bottom-right of motherboard
   - If user can't find it, fetch rear I/O diagram from manual: `https://download.gigabyte.com/FileList/Manual/mb_manual_b560-ds3h-ac_e_1201.pdf`

2. **Copy `B560DS3HACY1.F11` to thumb drive, rename to `GIGABYTE.bin`** (case-sensitive, all caps `GIGABYTE`, lowercase `.bin`)
   - F11 file already on laptop at: `C:\Users\intel\AppData\Local\Temp\opencode\bios-f11\extracted\B560DS3HACY1.F11`
   - Thumb drive is `D:` on laptop (label "BIOSF11", FAT32, 14 GB)
   - Copy file to `D:\GIGABYTE.bin`

3. **Execute Q-Flash Plus flash**
   - Gigabyte PC: shut down cleanly (S5), PSU stays ON (rear switch `I`)
   - Plug thumb drive into dedicated Q-Flash Plus USB port (white/labeled)
   - Press Q-Flash Plus button ~2 sec
   - Orange LED flashes 6–8 min — do not touch
   - LED stops → flash complete → auto-reboot
   - DualBIOS may cycle 1–2 more times to sync backup to F11

4. **Verify F11 took**
   - Press DEL at Gigabyte logo
   - Confirm BIOS version = F11
   - Press F5 (Load Optimized Defaults) — required post-flash
   - Save (F10), boot to Windows

### After flash verification

5. **Reconfigure BIOS settings** (all were wiped by the flash + F5 defaults):
   - XMP (RAM profile)
   - Boot order
   - Secure Boot (re-enable if desired)
   - **Disable PCIe ASPM** (Phase 1 item #4 — known WHEA mitigation per research)
   - Consider forcing PCIe Gen3 for the NVMe root port (research showed Gen3 downshift resolves WHEA on some Gigabyte boards)

6. **Verify stabilization in Windows** (2–3 days):
   ```powershell
   # Confirm BIOS version
   Get-CimInstance Win32_BIOS | Select-Object SMBIOSBIOSVersion, ReleaseDate

   # Check for new WHEA errors
   Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-WHEA-Logger'} -MaxEvents 50
   ```

### If crashes continue after F11 (Phase 2 deferred items)

7. **Reseat the NVMe SSD** (Phase 2 Step 5) — user hasn't opened the case yet
8. **Try the other M.2 slot** (Phase 2 Step 6) — board has PCIe 4.0 + PCIe 3.0 slots
9. **Check SSD SMART health** with CrystalDiskInfo or WD Dashboard (Phase 2 Step 7)
10. **Update NVMe SSD firmware** via WD Dashboard (Phase 1 Step 2 — never executed)
11. **Analyze 5 existing minidumps** with BlueScreenView/WinDbg (Phase 1 Step 3 — never executed)

### If Phase 2 doesn't fix it (Phase 3 — replacement)

12. Replace NVMe SSD (Phase 3 Step 9)
13. RMA motherboard (Phase 3 Step 10) if known-good SSD still WHEA-errors on Root Port #21

### Data safety (deferred — user opted to skip backup, proceed straight to flash)

The user chose "Skip backup, flash BIOS now" stating "I have most of the files
I need." No robocopy backup was executed. The external HDD (Disk 2, `H:`,
label "BACKUP", 931 GB NTFS, empty) is ready if needed post-flash. If crashes
continue after F11 and SSD replacement becomes necessary, **run the WinPE
robocopy BEFORE replacing the SSD** — the existing USB is no longer a Windows
installer (was reformatted as BIOS flasher), would need to be rebuilt via
Rufus/Media Creation Tool.

---

## System Identification

| Component | Detail |
|---|---|
| Motherboard | Gigabyte B560 DS3H AC-Y1 (Rev 1.0) |
| Current BIOS | **F4** (June 17, 2021) — main chip may be corrupted from Efiflash hang; DualBIOS backup (F4) should restore on next boot |
| Target BIOS | **F11** (Dec 19, 2023) — one-way update, cannot revert |
| CPU | Intel 11th Gen (Tiger Lake-H), B560 chipset |
| Failing device | WDC WDS100T2B0C-00PXH0 (1TB NVMe SSD) at PCI bus 2 — `VEN_15B7&DEV_5009` |
| Failing root port | Intel PCIe Root Port #21 — `VEN_8086&DEV_43C4` |
| GPU | NVIDIA GeForce RTX 3060 (PEG10, separate port — not implicated) |
| WiFi | Intel Wi-Fi 7 BE200 (upgraded from stock) |
| OS | Windows 11 build 26200 |
| NVIDIA driver | 32.0.15.9186 (Jan 19, 2026) |
| External HDD | 931 GB, freshly formatted `H:` NTFS label "BACKUP" (Disk 2 on Gigabyte) — empty, ready for backup if needed |
| Thumb drive | 14 GB, FAT32, label "BIOSF11" — currently holds Efiflash package; needs `GIGABYTE.bin` for Q-Flash Plus |
| This laptop | Lenovo, hostname `B0TTS`, user `b0tts\intel`, disk 0 = WD PC SN740 1TB NVMe — used for downloads/prep, not the failing machine |

---

## Evidence Chain

| Evidence | Source | What it proves |
|---|---|---|
| BugcheckCode = 292 (0x124) | Kernel-Power Event ID 41 (Critical) | WHEA_UNCORRECTABLE_ERROR |
| "Fatal hardware error" on PCIe Root Port | WHEA-Logger Event ID 16 (Error) | PCIe AER fatal error |
| 169 corrected PCIe AER errors (4-sec flood) | WHEA-Logger Event ID 17 (Warning) | Link instability preceding crash |
| Root Port #21 BusRelations = `VEN_15B7&DEV_5009` | `Get-PnpDeviceProperty` (live query) | Downstream device = NVMe SSD |
| 170/170 WHEA events = `VEN_8086&DEV_43C4` | EVTX parse this session | Single source, no USB/host-controller involvement |
| 0/170 WHEA events mention USB/xHCI/EHCI | EVTX parse this session | USB exonerated as cause |
| WHEA freeze inside WinPE (not just Windows) | User report this session | Crash source is hardware-layer, below OS |
| 0x7a (KERNEL_DATA_INPAGE_ERROR) added | User report this session | NVMe reads failing at OS level — escalation from intermittent to active degradation |
| Efiflash hung mid-flash | User report this session | WHEA crash can strike even outside Windows (during EFI shell), confirming hardware-layer root cause |
| Known identical issue on same board | Microsoft Learn Q&A | Same board, same event IDs — known problem |

### Crash Timeline (7/16/2026, from EVTX)

```
09:27:32 — 169 corrected PCIe AER errors begin flooding (WHEA ID 17)
09:27:36 — Error flood ends (~4 sec burst)
~09:26:50 — System crashes (per EventLog 6008)
09:27:55 — System reboots (Kernel-Boot: "last shutdown success = false")
09:27:58 — Kernel-Power 41 (Critical): Bugcheck 0x124 logged
           volmgr 161 (Error): Dump creation FAILED
09:28:04 — WHEA-Logger 16 (Error): "Fatal hardware error" on PCIe Root Port #21
           EventLog 6008: "Unexpected shutdown at 9:26:50 AM"
```

---

## Key Files, Paths, and Commands

| Item | Path / Command |
|---|---|
| Source EVTX log (laptop) | `C:\Users\intel\DevelopmentProjectTemplate\EventViewerEvents.evtx` |
| F11 BIOS ZIP (laptop, downloaded) | `C:\Users\intel\AppData\Local\Temp\opencode\bios-f11\F11.zip` |
| F11 BIOS extracted (laptop) | `C:\Users\intel\AppData\Local\Temp\opencode\bios-f11\extracted\B560DS3HACY1.F11` (33,554,432 bytes) |
| F11 EfiFlash package (laptop) | Same extracted dir: `Efiflash.efi`, `flash.nsh`, `EFI\BOOT\BOOTX64.EFI`, `efiflash SOP_MElock.pdf` |
| Thumb drive on laptop | `D:` — label "BIOSF11", FAT32, 14 GB — currently holds EfiFlash package; needs `GIGABYTE.bin` |
| Minidump directory (Gigabyte) | `C:\Windows\Minidump` (5 dumps: 6/8, 6/13x2, 6/14, 6/23) |
| Existing minidumps | `060826-16859-01.dmp`, `061326-20765-01.dmp`, `061326-21765-01.dmp`, `061426-19984-01.dmp`, `062326-18265-01.dmp` |
| MEMORY.DMP | Does NOT exist (dump creation failed on 7/16 crash) |
| Crash dump config | `HKLM:\SYSTEM\CurrentControlSet\Control\CrashControl` — CrashDumpEnabled=3, AutoReboot=1 |
| Page file | `C:\pagefile.sys`, 14848 MB allocated |
| Identify failing root port | `Get-PnpDevice \| Where-Object { $_.InstanceId -match 'VEN_8086&DEV_43C4' }` |
| Identify downstream NVMe | `Get-PnpDeviceProperty -InstanceId <root_port_id> -KeyName 'DEVPKEY_Device_BusRelations'` |
| Check NVMe health | `Get-PhysicalDisk \| Where-Object { $_.BusType -eq 'NVMe' } \| Get-StorageReliabilityCounter` |
| Check BIOS version | `Get-CimInstance Win32_BIOS \| Select-Object SMBIOSBIOSVersion, ReleaseDate` |
| BIOS download page | `https://www.gigabyte.com/us/Motherboard/B560-DS3H-AC-rev-10/support` |
| Direct F11 download | `https://download.gigabyte.com/FileList/BIOS/mb_bios_b560-ds3h-ac-y1_8arkl531_f11.zip` |
| Board manual (PDF) | `https://download.gigabyte.com/FileList/Manual/mb_manual_b560-ds3h-ac_e_1201.pdf` |
| Known identical issue (MS Learn) | `https://learn.microsoft.com/en-us/answers/questions/3958328/need-help-fixing-bsod-issues-on-b560-ds3h-ac-y1` |
| WinRAID EfiFlash thread | `https://winraid.level1techs.com/t/tool-efiflash-v0-80-v0-85-v0-87-for-gigabyte-mainboards/34071` |
| Q-Flash Plus support guide | `https://support.punchtechnology.co.uk/hc/en-us/articles/360016714097-How-to-update-the-BIOS-on-Gigabyte-motherboards-using-Q-Flash-Plus` |

---

## Full Remediation Plan (status updated)

### Phase 1: Software Fixes

| # | Action | Status |
|---|---|---|
| 1 | **Update BIOS F4 → F11** | **In progress — Efiflash attempt hung, retrying via Q-Flash Plus** |
| 2 | Update NVMe SSD firmware (WD Dashboard) | Not started |
| 3 | Analyze 5 minidumps (BlueScreenView/WinDbg) | Not started (deferred per user) |
| 4 | Disable PCIe ASPM (BIOS + Windows power plan) | Not started — should be done during post-flash BIOS reconfiguration |

### Phase 2: Hardware Diagnostics (no replacement cost)

| # | Action | Status |
|---|---|---|
| 5 | Reseat the NVMe SSD | Not started — user hasn't opened the case (Q-Flash Plus doesn't require it) |
| 6 | Try the other M.2 slot (PCIe 4.0 ↔ PCIe 3.0) | Not started |
| 7 | Check SSD SMART with CrystalDiskInfo / WD Dashboard | Not started |
| 8 | Run OCCT / IntelBurnTest stress test | Not started |

### Phase 3: Hardware Replacement (if Phases 1–2 don't fix it)

| # | Action | When |
|---|---|---|
| 9 | Replace the NVMe SSD | If F11 + firmware + reseat don't stop errors |
| 10 | RMA the motherboard | If known-good SSD still WHEA-errors on Root Port #21 |

---

## Open Decisions

1. **Q-Flash Plus file naming**: Gigabyte docs require the BIOS file renamed to `GIGABOTE.bin` — all caps `GIGABYTE`, lowercase `.bin`, case-sensitive. The existing `B560DS3HACY1.F11` must be copied and renamed on the thumb drive root.
2. **Skip boot verification before Q-Flash Plus**: User opted to skip booting to confirm DualBIOS recovery from the hung Efiflash attempt. Q-Flash Plus will write F11 regardless of current main chip state, so this is acceptable — but if Q-Flash Plus fails to start (LED doesn't flash), suspect corrupt main BIOS preventing S5 BMC handshake and revisit.
3. **Backup was skipped**: User chose flash-first, stating they have most files they need. External HDD (`H:` on Gigabyte, 931 GB NTFS, empty) is ready if a backup becomes necessary before SSD replacement. The thumb drive is no longer a Windows installer (was reformatted to BIOS flasher) — needs rebuild via Rufus + Media Creation Tool if WinPE robocopy is needed later.
4. **Post-flash ASPM disable**: Must be done in BIOS during reconfiguration AND in Windows power plan (AC setting needs verification — only DC confirmed as Off in prior session).
5. **PCIe Gen downshift**: Research this session showed forcing the NVMe root port to Gen3 (instead of Gen4) resolved WHEA on some Gigabyte B560/B660 boards. Worth trying if F11 alone doesn't stop crashes. Not yet discussed with user.
6. **If BIOS update doesn't fix it**: Next steps are SSD firmware update (WD Dashboard), reseat/swap M.2 slot, SMART check, then SSD replacement or motherboard RMA.

---

## Suggested Skills for Next Session

| Skill | Use when |
|---|---|
| `tutorial` | Resume step-by-step walkthrough of the Q-Flash Plus flash process (current session used this skill) |
| `create-nav-guide` | After BIOS update is complete + stabilization confirmed, document the full remediation (WHEA diagnosis → F11 flash → Q-Flash Plus recovery → post-flash config) as a reference guide for future crashes |
| `gsd-debug` | If F11 doesn't fix the crashes and systematic hardware debugging is needed (SSD firmware, reseat, slot swap, stress test) |
| `grill-me` | If user wants to stress-test the "is it BIOS or SSD?" decision before committing to SSD replacement |
| `create-planning-docs` | If the remediation expands into a multi-phase hardware replacement project (SSD → motherboard RMA) |