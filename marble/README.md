## Firmware Info

- Device: Xiaomi Poco F5
- Region: Global
- Version: `OS2.0.4.0.VMRMIXM` / `BOOT.MXF.2.0-01018.3-WAIPIO-1`

## Patches / Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch Nr. 1: Key code was patched for the power button to be mapped as ENTER instead of Special Samsung Keycode.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### ClockDxe:

- Reason: MDSS reinitializes and we lose framebuffer.
- Patch: DCD Dependency enablement path was patched to not cause MDSS to reinitialize.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### PmicDxe:

> [!NOTE]
> Must be paired with the SPMIDxe Patch.

- Reason: To make UEFI not Crash during UEFI Boot.
- Patch Nr. 1: Force call of "dead_battery_check" to avoid a crash when using the default value.
- Patch Nr. 2: Make failing SPMI Function call always return EFI_SUCCESS.
- Patch Creator: [Kancy Joe](https://github.com/sunflower2333) & [Shandorman](https://github.com/jiganomegsdfdf)

### SPMIDxe:

> [!NOTE]
> Must be paired with the PmicDxe Patch.

- Reason: To make UEFI not Crash during UEFI Boot.
- Patch: Removed SPMI Handle Function.
- Patch Creator: [Kancy Joe](https://github.com/sunflower2333)

### SdccDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing the driver to crash.
- Patch: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### UFSDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing a crash.
- Patch Nr. 1: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)


### UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux.
- Patch Nr. 1: Exit BootServices routine was patched to not deinit USB after exit boot services.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- Reason: To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)
