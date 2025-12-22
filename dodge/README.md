## Firmware Infos

- Device: OnePlus 13
- Region: EEA
- Version: `CPH2653_16.0.1.304` / `BOOT.MXF.2.5.1`

## Patches / Fixes

### ButtonsDxe:

- Reason: To make the Power Button usable in UEFI.
- Patch: The Special Qcom Key Code (`0x120`) has been Changed to the Key Code Enter (`0xD`).
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### FeatureEnablerDxe:

- Reason: To not reinit the TZ Appleet which was init by the Bootloader before.
- Patch: The TZ Applet Register Function has been Removed.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### PhoenixDxe:

- Reason: To avoid sudden Shutdownws and Crashes.
- Patch Nr. 1: Removed Watchdog Related Stuff from Driver.
- Patch Nr. 2: Forced a Protocol Function to always return `0` and `EFI_SUCCESS`.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### PmicDxe:

> [!NOTE]
> Must be paired with the SPMIDxe Patch.

- Reason: To make UEFI not Crash during UEFI Boot.
- Patch Nr. 1: SPMI Protocol Handle Function has been Removed.
- Patch Nr. 2: The Function `EFI_DeadBattery` OnePlus Function has been Removed.
- Patch Creator: [Kancy Joe](https://github.com/sunflower2333) & [Robotix22](https://github.com/Robotix22)

### SdccDxe:

- Reason: To Allow SMMU in the OS.
- Patch: The IOMMU Domains have been Removed.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

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
- Patch Nr. 3: Force UFS Link Wake Up Function to run before Gear Check.
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Kancy Joe](https://github.com/sunflower2333) & [N1kroks](https://github.com/N1kroks)

### UsbConfigDxe:

- Reason: To make USB work in UEFI and the OS.
- Patch Nr. 1: The IOMMU Domains have been removed to avoid a Crash.
- Patch Nr. 2: The USB Deinit Code has been Removed from Exit Boot Services Event to allow the OS to continue using the USB Port.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- Reason: To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)
