# Secure Boot for Warzone — Gigabyte F11 BIOS Fix

## Goal

Enable Secure Boot on this PC so Call of Duty: Warzone launches without the
"Secure Boot not enabled" error from RICOCHET Anti-Cheat.

## System Summary

| Detail | Value |
|---|---|
| Motherboard / BIOS | Gigabyte, F11 BIOS |
| OS | Windows 11 |
| BIOS Mode | UEFI |
| Disk Partition Style | GPT |
| TPM 2.0 | Enabled (fTPM / PTT) |
| CSM | Disabled |
| Secure Boot in BIOS | Enabled (but triggers boot error) |

## What's Been Done

1. ✅ Confirmed UEFI + GPT in `msinfo32` and Disk Management
2. ✅ Enabled TPM 2.0 in BIOS (Settings → Peripherals → fTPM/PTT)
3. ✅ CSM was already disabled in Boot tab
4. ✅ Enabled Secure Boot in Boot tab
5. ❌ Hit **"Invalid Signature Detected"** error on boot with Secure Boot on
6. ✅ Tried **Restore Factory Keys** (Secure Boot Mode → Custom → Restore Factory Keys → back to Standard) — still got the error
7. ❌ Attempted `bcdboot` from regular Command Prompt — got **"Failure when attempting to copy boot files"** — this was **not** run as Administrator, which is the likely cause
8. ❌ Attempted `bootrec` from within Windows — doesn't exist there (`bootrec` only lives in Windows Recovery Environment)

## Where We're Stuck

- Windows boots fine **with Secure Boot disabled**
- With Secure Boot enabled → "Invalid Signature Detected" at boot
- The Windows EFI boot files likely need to be refreshed so their signatures match what Secure Boot expects
- We haven't yet successfully run the refresh because of the admin CMD issue

## Next Steps (pick one)

### Option A: bcdboot from Admin CMD (simpler, try first)

1. Open Command Prompt **as Administrator** (Win key → type `cmd` → right-click → Run as administrator)
2. Run these in order:

```cmd
diskpart
list disk
select disk 0
list volume
```

3. Find the small FAT32 volume (usually 100–500 MB). Note its volume number.
4. Assign it a letter:

```cmd
select volume X          (replace X with the volume number)
assign letter=S:
exit
```

5. Verify it mounted:

```cmd
dir S:\
```

You should see an `EFI` folder. If not, you picked the wrong volume — go back to diskpart.

6. Rebuild the boot files:

```cmd
bcdboot C:\Windows /s S: /f UEFI
```

If that still fails, try:

```cmd
bcdboot C:\Windows /s S: /f ALL
```

7. Should say **"Boot files successfully created."**
8. Reboot → enter BIOS (Del) → confirm Secure Boot = Enabled, Mode = Standard
9. F10 to save & exit → boot Windows → `msinfo32` → confirm Secure Boot State: **On**
10. Launch Warzone

### Option B: bootrec from Windows Recovery (if Option A doesn't fix it)

1. Hold **Shift** while clicking **Restart** in the Start menu
2. Keep holding Shift until the blue recovery screen appears
3. Navigate: **Troubleshoot → Advanced options → Command Prompt**
4. PC will reboot — select your account and enter password
5. In the recovery command prompt:

```cmd
bootrec /fixboot
bootrec /rebuildbcd
```

6. Reboot → enter BIOS → verify Secure Boot enabled → F10 → test

### Nuclear option

If both fail: disable Secure Boot in BIOS → boot Windows → create a Windows 11
installation USB → boot from it → **Repair your computer → Troubleshoot →
Command Prompt** and run the bootrec commands from there. The installation
media WinRE sometimes works when the local one doesn't.

## Key Commands Reference

| Command | Where | Purpose |
|---|---|---|
| `msinfo32` | Windows Run | Check BIOS Mode & Secure Boot State |
| `diskpart` + `list volume` | Admin CMD | Identify EFI partition |
| `bcdboot C:\Windows /s S: /f UEFI` | Admin CMD | Refresh EFI boot files |
| `bootrec /fixboot` | WinRE CMD only | Repair boot sector |
| `bootrec /rebuildbcd` | WinRE CMD only | Rebuild BCD store |

## Suggested Skills for Next Session

- `tutorial` — if they want step-by-step pacing through the fix
- `explain-it-v2` — if they want to understand *why* the signature error happens
