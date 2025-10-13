## Firmware Infos

- Device: Samsung Galaxy S20 FE
- Region: EUX (Europe)
- Version: `G780GXXU3CVI1` / `BOOT.XF.3.2-00278-SM8250-2`

## Patches/Fixes

### ButtonsDxe:

- Reason: To make the Power Button usable in UEFI.
- Patch: The special Samsung Power Button mask (0x80) has been changed to the Enter key code (0xD).
- Patch Creator: [olegos2](https://github.com/olegos2)

### ClockDxe:

- Reason: To be able to boot Windows with debug build.
- Patch: Low Power Mode handler registration has been patched so it does not register LPM mode.
- Patch Creator: [N1kroks](https://github.com/N1kroks)

### FeatureEnablerDxe:

- Reason: The clock is already turned on, turning it on again will cause framebuffer loss
- Patch: The function that enables clocks has been patched to always return Success.
- Patch Creator: [N1kroks](https://github.com/N1kroks)

### PmicDxe:

- Reason: To prevent sudden UEFI shutdowns.
- Patch: The invalid Power Button press check has been removed.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### SdccDxe:

- Reason: To make SD Card "work" in UEFI and to Allow SMMU in the OS.
- Patch: The IOMMU Domains have been Removed.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### TzDxeLA:

- Reason: The Common and Keymaster TZ Applets are already loaded, Also we don't have to notify TZ a second time where TZ applets will be loaded to.
- Patch: The global variable has been changed to 0x1 so function that notifies tz and loads applets is not called.
- Patch Creator: [N1kroks](https://github.com/N1kroks)

### UFSDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing a crash.
- Patch: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbConfigDxe:

- Reason: Is important to get USB working in Windows / Linux and UEFI.
- Patch: Exit BootServices routine was patched to not deinit USB after exit boot services.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- Reason: To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)
