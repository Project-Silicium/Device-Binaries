## Firmware Infos

> [!IMPORTANT]
> This Firmware is the Last Firmware that Allows a Unlocked Bootloader. <br>
> Any newer Firmware Version should not be used.

- **Device:** Samsung Galaxy Z Flip5
- **Region:** EUX (Europe)
- **Version:** `F731BXXS5FZA1` / `BOOT.MXF.2.1.1-00218-KAILUA-1`

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
- **Patch Nr. 3:** Qcom's Panel Reset Function has been Removed.
- **Patch Nr. 4:** Qcom's DSI Panel Init Function has been Modded.
- **Patch Nr. 5:** Samsung's Panel Reset Function has been Removed.
- **Patch Nr. 6:** A DSI Close Function Call has been Removed.
- **Patch Nr. 7:** Modified Display Set Power State Protocol Function.
- **Patch Nr. 8:** Modfifed Exit Boot Services Event.
- **Patch Nr. 9:** Removed a Broken Paint Command for the Main Display.
- **Patch Nr. 10:** Removed a Debug Message Call in GOP BLT Function.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/) & [Robotix22](https://github.com/Robotix22/) & [Aistop](https://github.com/AistopGit/)

### PmicDxe:

- **Reason:** To prevent a UEFI Crash during Boot.
- **Patch Nr. 1:** Removed Protected PM COMM Write Calls.
- **Patch Nr. 2:** Removed IRQ Disable Function.
- **Patch Nr. 3:** Removed Lock Config Function.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22/) & [Kancy Joe](https://github.com/sunflower2333/)

### SPMIDxe:

- **Reason:** To prevent a UEFI Crash during Boot.
- **Patch:** Removed the SPMI PIC Init Function.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333/)

### TzDxeLA:

- **Reason:** To prevent the Re-creation of already Existing TZ Applets.
- **Patch:** The Global TZ Applet Variable has been Changed to `TRUE` from `FALSE`.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)

### UFSDxe:

> [!TIP]
> UFS will still enter Sleep State after Exit Boot Services. <br>
> To prevent this, Set `UEFIExitUfsSSURequired` to `0` in the Configuration Map.

- **Reason:** To allow the usage of the UFS.
- **Patch Nr. 1:** The Unit Ready SCSI Command has been Replaced with the Start/Stop Unit SCSI Command.
- **Patch Nr. 2:** Added UFS Link Wake Up.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333/) & [N1kroks](https://github.com/N1kroks/)

### UsbConfigDxe:

- **Reason:** To allow the usage of the USB Port.
- **Patch:** Removed IOMMU Detach from Exit Boot Services.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### UsbMsdDxe:

- **Reason:** For better Mass Storage usage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)
