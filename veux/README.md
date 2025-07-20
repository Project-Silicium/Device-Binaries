## Firmware Infos

- Device: Redmi Note 11 Pro 5G
- Region: EEA (Europe)
- Version: `OS1.0.12.0.TKCEUXM` / `BOOT.XF.4.2-00248-MANNARLAZ-1.459413.1`

## Patches / Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- Reason: To keep Display Alive during Boot & Making Windows Boot on Debug Builds.
- Patch Nr. 1: a NPA Function has been Removed.
- Patch Nr. 2: LPM Call Backs Function has been Removed.
- Patch Creator: [Kernel357](https://github.com/Kernel357) & [Robotix22](https://github.com/Robotix22) & [N1kroks](https://github.com/N1kroks)

### HALIOMMU:

- Reason: IOMMUs for USB and eMMC are already present, If re-set again UEFI crashes.
- Patch: IOMMU for USB and eMMC has been patched to always return Success.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### UFSDxe:

- Reason: To make UEFI be able to use the Internal Storage.
- Patch: The IOMMU Domains have been removed to avoid a Crash.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbPwrCtrlDxe (N.r1 is Temporary Patch):

- Reason: Pmic dosen't Init Correct, Causing this Driver to not Load Correct.
- Patch N.r1: The Driver has been Forced to load anyway.
- Patch N.r2: Driver spamming has been hidden in DEBUG builds 
- Patch Creator: [N1kroks](https://github.com/N1kroks) & [index986](https://github.com/index986)

### UsbMsdDxe:

- Reason: To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)
