## Firmware Infos

- **Device:** Samsung Galaxy Tab S8+ 5G
- **Region:** EUX (Europe)
- **Version:** `X806BXXS9EYK1` / `BOOT.MXF.2.0-00805-WAIPIO-1`

## Patches / Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch Nr. 1:** The Special Samsung Key Code (`0x80`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Nr. 2:** The Button Handlening has been Modded to allow Unichar Key Codes.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22/)

### ClockDxe:

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch:** The DCD Disable Dependencies Function Call has been Removed.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### DisplayDxe:

> [!IMPORTANT]
> This Patch requires `EnableDisplayThread` to be Disabled in the Configuration Map.

- **Reason:** To get more Control over the Display in UEFI.
- **Patch Nr. 1:** The IOMMU Domains have been Removed.
- **Patch Nr. 2:** Samsung's Panel Powerup Function has been Removed.
- **Patch Nr. 3:** Qcom's Panel Reset Function has been Removed.
- **Patch Nr. 4:** Qcom's DSI Panel Init Function has been Modded.
- **Patch Nr. 5:** Samsung's Panel Reset Function has been Removed.
- **Patch Nr. 6:** A DSI Close Function call has been Removed.
- **Patch Nr. 7:** Panel Configuration has been Changed to Set 120 Hz instead of 30 Hz.
- **Patch Creators:** [Gustave Monce](https://github.com/gus33000/), [Robotix22](https://github.com/Robotix22/)

### FeatureEnablerDxe:

- **Reason:** To not reinit the TZ Appleet which was init by the Bootloader before.
- **Patch:** The TZ Applet Register Function has been Removed.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### PmicDxe:

> [!IMPORTANT]
> Must be paired with the SPMIDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch Nr. 1:** Minimal PMIC Init has been Removed.
- **Patch Nr. 2:** The Invalid Power Button Press Check has been Removed.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333/), [Robotix22](https://github.com/Robotix22/)

### SdccDxe:

> [!IMPORTANT]
> Platform Type must be `WP` for Patch Nr. 2 to Work.

- **Reason:** To allow the Usage of a SD Card.
- **Patch Nr. 1:** Added Power On Code for PM8350C LDO6 and LDO9 Regulator.
- **Patch Nr. 2:** Forced SDHCi Mode to Enable on Exit Boot Services Event.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22/)

### SPMIDxe:

> [!IMPORTANT]
> Must be paired with the PmicDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Removed the SPMI PIC Init Function.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333/)

### UFSDxe:

- **Reason:** To allow the usage of UFS.
- **Patch:** The UFS Sleep call has been Replaced with the UFS Wakeup Call.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333/)

### UsbConfigDxe:

- **Reason:** To allow the usage of the USB Port.
- **Patch:** Removed IOMMU Detach from Exit Boot Services.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### UsbMsdDxe:

- **Reason:** For better Mass Storage usage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)
