# Handoff: BSOD 0x124 WHEA PCIe Crash Diagnosis & Remediation Plan

## Date
07-16-2026

## Summary

Diagnosed the cause of daily PC crashes from an exported Event Viewer log
(`EventViewerEvents.evtx`, 328 events). The system is bugchecking with
**0x124 (WHEA_UNCORRECTABLE_ERROR)** due to a fatal PCIe hardware error on
**Intel PCI Express Root Port #21** (device `VEN_8086&DEV_43C4`), whose
downstream device is the **WDC WDS100T2B0C-00PXH0 1TB NVMe SSD**
(`VEN_15B7&DEV_5009`).

A full remediation plan was produced. **No remediation steps have been
started yet.** The user selected "BIOS update first" as the preferred path
but has not yet begun flashing.

---

## System Identification

| Component | Detail |
|---|---|
| Motherboard | Gigabyte B560 DS3H AC-Y1 (Rev 1.0) |
| Current BIOS | **F4** (June 17, 2021 — launch version, 5 years old) |
| CPU | Intel 11th Gen (Tiger Lake-H), B560 chipset |
| Failing device | WDC WDS100T2B0C-00PXH0 (1TB NVMe SSD) at PCI bus 2 |
| Failing root port | Intel PCIe Root Port #21 — `VEN_8086&DEV_43C4` |
| GPU | NVIDIA GeForce RTX 3060 (NOT the issue — on PEG10, separate port) |
| WiFi | Intel Wi-Fi 7 BE200 (upgraded from stock) |
| OS | Windows 11 build 26200 |
| NVIDIA driver | 32.0.15.9186 (Jan 19, 2026) |

---

## Evidence Chain

| Evidence | Source | What it proves |
|---|---|---|
| BugcheckCode = 292 (0x124) | Kernel-Power Event ID 41 (Critical) | WHEA_UNCORRECTABLE_ERROR |
| "Fatal hardware error" on PCIe Root Port | WHEA-Logger Event ID 16 (Error) | PCIe AER fatal error |
| 169 corrected PCIe AER errors (4-sec flood) | WHEA-Logger Event ID 17 (Warning) | Link instability preceding crash |
| Root Port #21 BusRelations = `VEN_15B7&DEV_5009` | `Get-PnpDeviceProperty` (live query) | Downstream device = NVMe SSD |
| "Previous shutdown was unexpected" | EventLog ID 6008 | Confirms crash, not clean shutdown |
| Dump creation failed (0x00040049) | volmgr Event ID 161 (Error) | No minidump for 7/16 crash |
| 5 prior minidumps (6/8, 6/13x2, 6/14, 6/23) | `C:\Windows\Minidump` | Recurring crashes over 38+ days |
| Known identical issue reported by another user | Microsoft Learn Q&A | Same board, same event IDs — known problem |

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

## Full Remediation Plan (NOT YET STARTED)

### Phase 1: Software Fixes (no cost, highest impact)

| # | Action | Why | Status |
|---|---|---|---|
| 1 | **Update BIOS from F4 to F11** | Launch BIOS has known PCIe/NVMe WHEA bugs; F6+ has CPU microcode 0x34 fixing PCIe controller errata; F11 adds security fixes | **Selected by user, not started** |
| 2 | **Update NVMe SSD firmware** | WD may have released firmware fixing PCIe link stability | Not started |
| 3 | **Analyze 5 minidumps with BlueScreenView/WinDbg** | Confirm all prior crashes are 0x124 or find other bugcheck codes | Not started |
| 4 | **Disable PCIe ASPM** in BIOS and Windows power plan | Prevents link state transitions that trigger AER errors | Not started |

### Phase 2: Hardware Diagnostics (no replacement cost)

| # | Action | Why | Status |
|---|---|---|---|
| 5 | Reseat the NVMe SSD (remove and reinsert M.2) | Fixes poor contact causing link errors | Not started |
| 6 | Try a different M.2 slot (board has 2: PCIe 4.0 + 3.0) | Rules out a bad slot | Not started |
| 7 | Check SSD SMART health with CrystalDiskInfo or WD Dashboard | Detects drive degradation/failure | Not started |
| 8 | Run OCCT/IntelBurnTest stress test | See if errors reproduce predictably | Not started |

### Phase 3: Hardware Replacement (if Phases 1-2 don't fix it)

| # | Action | When |
|---|---|---|
| 9 | Replace the NVMe SSD | If firmware + BIOS + reseating don't stop errors |
| 10 | RMA the motherboard | If known-good SSD still produces WHEA errors on Root Port #21 |

---

## BIOS Update Plan: F4 -> F11 (Detail)

### Why F11

- F6 (Nov 2021): CPU microcode 0x34 — fixes CPU PCIe controller errata
- F8/F9 (2023): Stability improvements
- F11 (Dec 2023): Capsule BIOS + security vulnerability fixes
- **Warning**: F11+ cannot be reverted to earlier versions (one-way update)
- F11b (Jun 2025) is a beta with additional CVE patches — available as fallback

### Download

- Gigabyte support page: `https://www.gigabyte.com/us/Motherboard/B560-DS3H-AC-rev-10/support`
- Direct F11 link: `https://download.gigabyte.com/FileList/BIOS/mb_bios_b560-ds3h-ac-y1_8arkl531_f11.zip`

### Steps

1. Back up critical data to external drive/cloud
2. Note current BIOS settings (photos): XMP, boot order, Secure Boot, etc.
3. Format USB flash drive to FAT32 (4GB+)
4. Download F11 ZIP, extract, copy BIOS file to USB root (not in subfolder)
5. Reboot -> press DEL to enter BIOS
6. Press F8 for Q-Flash (or Save & Exit tab -> Q-Flash)
7. Select "Update BIOS From Drive" -> choose USB -> select F11 file
8. Confirm and flash — DO NOT power off — takes 1-3 min
9. System reboots automatically (may reboot 2-3 times)
10. Clear CMOS: power off, unplug, remove CR2032 battery for 30 sec, reinsert
11. Boot into BIOS (DEL), reconfigure: XMP, boot order, Secure Boot, **disable ASPM**
12. Save & exit (F10), boot to Windows

### Verify

```powershell
# Confirm BIOS version
Get-CimInstance Win32_BIOS | Select-Object SMBIOSBIOSVersion, ReleaseDate

# Check for new WHEA errors after 2-3 days
Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-WHEA-Logger'} -MaxEvents 50
```

---

## Key Files, Paths, and Commands

| Item | Path / Command |
|---|---|
| Source EVTX log | `C:\Users\Jonah\DevelopmentTemplate\EventViewerEvents.evtx` |
| Minidump directory | `C:\Windows\Minidump` (5 dumps: 6/8, 6/13x2, 6/14, 6/23) |
| Existing minidumps | `060826-16859-01.dmp`, `061326-20765-01.dmp`, `061326-21765-01.dmp`, `061426-19984-01.dmp`, `062326-18265-01.dmp` |
| MEMORY.DMP | Does NOT exist (dump creation failed on 7/16 crash) |
| Crash dump config | `HKLM:\SYSTEM\CurrentControlSet\Control\CrashControl` — CrashDumpEnabled=3 (small minidump), AutoReboot=1 |
| Page file | `C:\pagefile.sys`, 14848 MB allocated |
| Identify failing root port | `Get-PnpDevice \| Where-Object { $_.InstanceId -match 'VEN_8086&DEV_43C4' }` |
| Identify downstream NVMe | `Get-PnpDeviceProperty -InstanceId <root_port_id> -KeyName 'DEVPKEY_Device_BusRelations'` |
| Check NVMe health | `Get-PhysicalDisk \| Where-Object { $_.BusType -eq 'NVMe' } \| Get-StorageReliabilityCounter` |
| Check BIOS version | `Get-CimInstance Win32_BIOS \| Select-Object SMBIOSBIOSVersion, ReleaseDate` |
| BIOS download page | `https://www.gigabyte.com/us/Motherboard/B560-DS3H-AC-rev-10/support` |
| Known identical issue (MS Learn) | `https://learn.microsoft.com/en-us/answers/questions/3958328/need-help-fixing-bsod-issues-on-b560-ds3h-ac-y1` |

---

## Open Decisions

1. **BIOS target version**: F11 (stable, Dec 2023) chosen. F11b (beta, Jun 2025) available with additional CVE patches if F11 doesn't resolve crashes.
2. **Whether to analyze the 5 existing minidumps first** before flashing BIOS — could confirm all crashes share the same 0x124 bugcheck. User chose BIOS-first; minidump analysis is deferred to Phase 1 item #3.
3. **ASPM disable**: Should be done in BIOS during post-flash reconfiguration AND in Windows power plan (AC setting needs verification — only DC was confirmed as Off).
4. **If BIOS update doesn't fix it**: Next steps are SSD firmware update (WD Dashboard), reseat/swap M.2 slot, SMART check, then SSD replacement or motherboard RMA.

---

## Suggested Skills for Next Session

| Skill | Use when |
|---|---|
| `create-nav-guide` | After BIOS update is complete, document the full remediation as a reference guide for future crashes |
| `tutorial` | If user wants step-by-step guided walkthrough of the BIOS flash process |
| `gsd-debug` | If BIOS update doesn't fix the crashes and systematic debugging is needed |
| `create-planning-docs` | If the remediation expands into a multi-phase hardware replacement project |
