## Firmware Infos

- Device: Samsung Galaxy Tab S8+ 5G
- Region: EUX (Europe)
- Version: `X806BOXM9DYDC` / `BOOT.MXF.2.0-00805-WAIPIO-1`

## Patches / Fixes

### ButtonsDxe:

- Reason: To make the Power Button usable in UEFI.
- Patch Nr. 1: The Special Samsung Key Code (`0x80`) has been Changed to the Key Code Enter (`0xD`).
- Patch Nr. 2: The Button Handlening has been Modded to allow Unichar Key Codes.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### ClockDxe:

- Reason: To keep Display turned on while UEFI Boot.
- Patch: The DCD Dependency Enablement Path has been patched to not reinitialize MDSS.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### DisplayDxe:

> [!NOTE]
> This Patch requires `EnableDisplayThread` to be Disabled in the Configuration Map.

- Reason: To get more Control over the Display in UEFI.
- Patch Nr. 1: The IOMMU Domains have been Removed to avoid a Crash.
- Patch Nr. 2: Samsung's Panel Powerup Function has been Removed to avoid Turning off Display.
- Patch Nr. 3: Qcom's Panel Reset Function has been removed to avoid turning off the Display.
- Patch Nr. 4: Qcom's DSI Panel Init Function has been Modded to not turn off Display.
- Patch Nr. 5: Samsung's Panel Reset Function has been Removed to avoid turning off Display.
- Patch Nr. 6: A DSI Close Function call has been Removed to avoid turning off Display.
- Patch Nr. 7: Panel Configuration has been Changed to Enable 120 Hz Display.
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Robotix22](https://github.com/Robotix22)

### FeatureEnablerDxe:

- Reason: To not reinit the TZ Appleet which was init by the Bootloader before.
- Patch: The TZ Applet Register Function has been Removed.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### PmicDxe:

> [!NOTE]
> Must be paired with the SPMIDxe Patch.

- Reason: To make UEFI not Crash during UEFI Boot.
- Patch Nr. 1: Minimal PMIC Init has been Removed to avoid a Crash.
- Patch Nr. 2: The Invalid Power Button Press Check has been to Remove to avoid a sudden Shutdown.
- Patch Creator: [Kancy Joe](https://github.com/sunflower2333) & [Robotix22](https://github.com/Robotix22)

### SdccDxe:

- Reason: To make SD Card "work" in UEFI and to Allow SMMU in the OS.
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
