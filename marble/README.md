## Firmware Info

- Device: Xiaomi Poco F5
- Region: Global
- Version: `OS2.0.4.0.VMRMIXM` / `BOOT.MXF.2.0-01018.3-WAIPIO-1`

## Patches / Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch Nr. 1: Key code was patched for the power button to be mapped as ENTER instead of Special Samsung Keycode.
- Patch Creator: [Robotix22](https://github.com/Robotix22)


### UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux.
- Patch Nr. 1: Exit BootServices routine was patched to not deinit USB after exit boot services.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UFSDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing a crash.
- Patch Nr. 1: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)
