## Firmware Infos

- Device: realme GT Neo5
- Region: CN
- Version: `RMX3706_15.0.0.500` / `BOOT.MXF.2.0-00925.2-WAIPIO-1.22250.6.39858.1`

## Patches/Fixes

### ButtonsDxe:

- Reason: To make the Power Button usable in UEFI.
- Patch: Map power button Key Code as ENTER instead of SUSPEND.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- Reason: To keep some important clocks on.
- Patch: Removed "Clock_CESTADisableDependencies" function call.
- Patch Creator: [Robotix](https://github.com/Robotix22)

### PmicDxe:

- Reason: To make UEFI not Crash during UEFI Boot.
- Patch Nr. 1: Make failing SPMI Function call always return EFI_SUCCESS.
- Patch Nr. 2: Make some failing functions return 0 (patched on this device only).
- Patch Nr. 3: Do not call some functions (at 0x3eb0), taken from sunflower2333's patch for sheng
- Patch Creator: [Kancy Joe](https://github.com/sunflower2333) & [Shandorman](https://github.com/jiganomegsdfdf) & [artempeshkov](https://github.com/artempeshkov) 

### UFSDxe:

- Reason: To make UEFI be able to use the Internal Storage.
- Patch Nr. 1: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Nr. 2: The UFS Sleep call has been Replaced with the UFS Wakeup Call.
- Patch Nr. 3: Added UFS Gear Wake Up call.
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Kancy Joe](https://github.com/sunflower2333) & [N1kroks](https://github.com/N1kroks)

### UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux.
- Patch: Exit BootServices routine was patched to not deinit USB after exit boot services. Another patch disables recreating IOMMU domains.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- Reason: To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)
