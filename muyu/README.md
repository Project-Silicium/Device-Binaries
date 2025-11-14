## Firmware Infos

- Device: Xiaomi Pad 7 Pro
- Region: Global
- Version: `muyu_global_images_OS3.0.3.0.WOYMIXM_16.0` / `BOOT.MXF.2.1-01919.2-LANAI-1.78639.7.93787.2`

## Patches/Fixes

### ClockDxe:

- Reason: To allow Mu-Silicium to boot successfully
- Patch: The Clock_InitCESTA function has been patched to always return 0
- Patch Creator: [ungeskriptet](https://github.com/ungeskriptet)

### PmicDxe:

> [!NOTE]
> Must be paired with the SPMIDxe Patch.

- Reason: To make UEFI not Crash during UEFI Boot.
- Patch Nr. 1: Minimal PMIC Init has been Removed to avoid a Crash.
- Patch Nr. 2: The Invalid Power Button Press Check has been to Remove to avoid a sudden Shutdown.
- Patch Nr. 3: Remove peripheral id checks to prevent an assertion.
- Patch Creator: [Kancy Joe](https://github.com/sunflower2333) & [Robotix22](https://github.com/Robotix22) & [PugzAreCute](https://github.com/PugzAreCute)

### SPMIDxe:

> [!NOTE]
> Must be paired with the PmicDxe Patch.

- Reason: To make UEFI not Crash during UEFI Boot.
- Patch: Removed SPMI Handle Function.
- Patch Creator: [Kancy Joe](https://github.com/sunflower2333)

### UFSDxe:

- Reason: To make UEFI be able to use the Internal Storage.
- Patch Nr. 1: The IOMMU Domains have been removed to avoid a Crash.
- Patch Nr. 2: The UFS Sleep call has been Replaced with the UFS Wakeup Call.
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Kancy Joe](https://github.com/sunflower2333)

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu)
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbConfigDxe:

- Reason: To make USB work in UEFI and the OS.
- Patch Nr. 1: The IOMMU Domains have been removed to avoid a Crash.
- Patch Nr. 2: The USB Deinit Code has been Removed from Exit Boot Services Event to allow the OS to continue using the USB Port.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- Reason: To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- Patch Nr. 1: Changed Removable State to Non-Removable.
- Patch Nr. 2: Changed the USB PID to avoid MTP problems.
- Patch Creator: [N1kroks](https://github.com/N1kroks) & [Sinetek](https://github.com/philmb3487)
