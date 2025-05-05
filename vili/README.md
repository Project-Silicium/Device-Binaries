## Firmware Infos

- Device: Xiaomi 11T Pro
- Region: EEA (Europe)
- Version: `OS1.0.16.0.UKDEUXM` / `BOOT.MXF.1.0-00852-LAHAINA-2.12801.13`

## Patches / Fixes

### ButtonsDxe:

- Reason: To make the Power Button usable in UEFI.
- Patch: The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- Reason: To keep Display turned on while UEFI Boot.
- Patch Nr. 1: The DCD Dependency Enablement Path has been patched to avoid reinitialize MDSS.
- Patch Nr. 2: The LPM Call Backs Function has been Removed to allow Windows Boot on Debug Builds.
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [N1kroks](https://github.com/N1kroks)

### CPRDxe:

> [!NOTE]
> DisplayDxe requires this Driver (It just needs the Memory Region that gets Registerd here).

- Reason: To make it map the Memory Map `MMCX_CPR3` properly.
- Patch: The CPR Cllock Rail Disable Function has been Removed to avoid a Crash.
- Patch Creator: [Robotix22](https://github.com/Eobotix22)

### DisplayDxe:

> [!NOTE]
> This Patch requires `EnableDisplayThread` to be Disabled in the Configuration Map.

- Reason: To get more Control over the Display in UEFI.
- Patch Nr. 1: The IOMMU Domains have been Removed to avoid a Crash.
- Patch Nr. 2: Qcom's Panel Reset Function has been removed to avoid turning off the Display.
- Patch Nr. 3: Qcom's DSI Panel Init Function has been Modded to not turn off Display.
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Robotix22](https://github.com/Eobotix22)

### FeatureEnablerDxe:

- Reason: To not reinit the TZ Appleet which was init by the Bootloader before.
- Patch: The TZ Applet Register Function has been Removed.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### SdccDxe:

- Reason: To avoid a Crash in the Windows SMMU Driver.
- Patch: The IOMMU Domains have been Removed.
- Patch Creator: [Robotix22](https://github.com/Eobotix22)

### UFSDxe:

- Reason: To make UEFI be able to use the Internal Storage.
- Patch: The IOMMU Domains have been removed to avoid a Crash.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbConfigDxe:

- Reason: To make USB work in UEFI and the OS.
- Patch Nr. 1: The IOMMU Domains have been removed to avoid a Crash.
- Patch Nr. 2: The USB Deinit Code has been Removed from Exit Boot Services Event to allow the OS to continue using the USB Port.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- Reason: To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)
