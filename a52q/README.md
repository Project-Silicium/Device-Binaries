## Firmware Info

- Device: Samsung Galaxy A52
- Region: EUX (Europe)
- Version: `A525FXXSCFYF1` / `BOOT.XF.3.1-00589-SM6150LZB-2`

## Patches / Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch Nr. 1: Key code was patched for the power button to be mapped as ENTER instead of Special Samsung Keycode.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### DisplayDxe:

- Reason: To get more Control over the Display in UEFI.
- Patch Nr. 1: The IOMMU Domains have been Removed to avoid a Crash.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### HALIOMMUDxe:

- Reason: IOMMUs for USB and SD Card are already present, If reset again UEFI crashes.
- Patch Nr. 1: IOMMU for USB and SD Card has been patched to always return Success.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux.
- Patch Nr. 1: Exit BootServices routine was patched to not deinit USB after exit boot services.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UFSDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing a crash.
- Patch Nr. 1: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)
