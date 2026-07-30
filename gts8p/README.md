## Firmware Infos

> [!IMPORTANT]
> This Firmware is the Last Firmware that Allows a Unlocked Bootloader. <br>
> Any newer Firmware Version should not be used.

- **Device:** Samsung Galaxy Tab S8+ 5G
- **Region:** EUX (Europe)
- **Version:** `X806BXXS9EZA3` / `BOOT.MXF.2.0-00805-WAIPIO-1`

## Patches / Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch Nr. 1:** The Key Code `SCAN_VOLUME_UP` has been Changed to the `CHAR_CARRIAGE_RETURN` Key Code.
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
- **Patch Nr. 1:** The IOMMU Domains Register Function has been Removed.
- **Patch Nr. 2:** Samsung's Panel Powerup Function has been Removed.
- **Patch Nr. 3:** Qcom's Panel Reset Function has been Removed.
- **Patch Nr. 4:** Qcom's DSI Panel Init Function has been Modded.
- **Patch Nr. 5:** Samsung's Panel Reset Function has been Removed.
- **Patch Nr. 6:** A DSI Close Function call has been Removed.
- **Patch Nr. 7:** Panel Configuration has been Changed to Set 120 Hz instead of 30 Hz.
- **Patch Creators:** [Gustave Monce](https://github.com/gus33000/), [Robotix22](https://github.com/Robotix22/)

### PmicDxe:

- **Reason:** To prevent a UEFI Crash during Boot.
- **Patch:** Removed a Protected PM COMM Write Call.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22/)

### SdccDxe:

> [!IMPORTANT]
> Platform Type must be `WP` for Patch Nr. 2 to Work.

- **Reason:** To allow the Usage of a SD Card.
- **Patch Nr. 1:** Added Power On Code for PM8350C LDO6 and LDO9 Regulator.
- **Patch Nr. 2:** Forced SDHCi Mode to Enable on Exit Boot Services Event.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22/)

### TzDxeLA:

- **Reason:** To prevent the Re-creation of already Existing TZ Applets.
- **Patch:** The Global TZ Applet Variable has been Changed to `TRUE` from `FALSE`.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)

### UFSDxe:

- **Reason:** To allow the usage of the UFS.
- **Patch:** The Unit Ready SCSI Command has been Replaced with the Start/Stop Unit SCSI Command.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333/)

### UsbConfigDxe:

- **Reason:** To allow the usage of the USB Port.
- **Patch:** Removed IOMMU Detach from Exit Boot Services.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### UsbMsdDxe:

- **Reason:** For better Mass Storage usage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)
