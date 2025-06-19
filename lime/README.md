## Firmware Infos

- Device: Xiaomi Redmi 9T
- Region: Global
- Version: `V13.0.6.0.SJQMIXM` / `BOOT.XF.4.1-00335-KAMORTALAZ-1.572417.1.586717.1`

## Patches/Fixes

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

### UsbMsdDxe:

- Reason: To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)
