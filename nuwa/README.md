## Firmware Infos

- Device: Xiaomi 13 Pro
- Region: EEA (Europe)
- Version: `OS2.0.110.0.VMBEUXM` / `BOOT.MXF.2.1.1-00218-KAILUA-1.36233.1`

## Patches / Fixes

### ButtonsDxe:

- Reason: To make the Power Button usable in UEFI.
- Patch: The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- Reason: To keep Display turned on while UEFI Boot.
- Patch: The DCD Dependency Enablement Path has been patched to not reinitialize MDSS.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### DisplayDxe:

> [!NOTE]
> This Patch requires `EnableDisplayThread` to be Disabled in the Configuration Map.

- Reason: To get more Control over the Display in UEFI.
- Patch Nr. 1: The IOMMU Domains have been Removed to avoid a Crash.
- Patch Nr. 2: Qcom's Panel Reset Function has been removed to avoid turning off the Display.
- Patch Nr. 3: Qcom's DSI Panel Init Function has been Modded to not turn off Display.
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Robotix](https://github.com/Eobotix22)

### FeatureEnablerDxe:

- Reason: To not reinit the TZ Appleet which was init by the Bootloader before.
- Patch: The TZ Applet Register Function has been Removed.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### PmicDxe:

> [!NOTE]
> Must be paired with the SPMIDxe Patch.

- Reason: To make UEFI not Crash during UEFI Boot.
- Patch: Minimal PMIC Init has been Removed to avoid a Crash.
- Patch Creator: [Kancy Joe](https://github.com/sunflower2333)

### SdccDxe:

- Reason: To allow the usage of SMMU in the OS.
- Patch: The IOMMU Domains have been Removed.
- Patch Creator: [Robotix](https://github.com/Robotix22)

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

### UsbConfigDxe:

- Reason: To make USB work in UEFI and the OS.
- Patch Nr. 1: The IOMMU Domains have been removed to avoid a Crash.
- Patch Nr. 2: The USB Deinit Code has been Removed from Exit Boot Services Event to allow the OS to continue using the USB Port.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- Reason: To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)

## Raw File Changes

## Panel_M2_38_0c_0a_dsc_cmd.xml

- Reason: To have Proper Display Init in UEFI.
- Change Nr. 1: The `DSIAutoRefreshFrameNumDiv` has been Updated to Force 60 Hz instead of 1 Hz.
- Change Nr. 2: `DSIInitSequence` has been Modded to Avoid Changing the Brightness to 0.
- Change Creator: [Robotix](https://github.com/Robotix22) & [Aistop](https://github.com/AistopGit/)
