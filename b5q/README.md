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
- **Patch Nr. 1:** The IOMMU Domains have been Removed to avoid a Crash.
- **Patch Nr. 2:** Qcom's Panel Reset Function has been removed to avoid turning off the Main Display.
- **Patch Nr. 3:** Qcom's DSI Panel Init Function has been Modded to not turn off the Displays.
- **Patch Nr. 4:** Samsung's Panel Reset Function has been Removed to avoid turning off the Displays.
- **Patch Nr. 5:** A DSI Close Function call has been Removed to avoid turning off the Main Display.
- **Patch Nr. 6:** Forced LPM Function Call to Unregister the Event instead of Registering it.
- **Patch Nr. 7:** Modified Display Set Power State Protocol Function to not Deinit Clocks on Turn Off.
- **Patch Nr. 8:** Modfifed Exit Boot Services Event to Only Turn off Cover Display instead of Both.
- **Patch Nr. 9:** Removed a Broken Paint Command for the Main Display to Avoid Trash on the Display.
- **Patch Nr. 10:** Removed a Debug Message Call in GOP BLT Function.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000) & [Robotix22](https://github.com/Robotix22) & [Aistop](https://github.com/AistopGit)

### PmicDxe:

> [!IMPORTANT]
> Must be paired with the SPMIDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Minimal PMIC Init has been Removed.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333/)

### QcomWDogDxe:

- **Reason:** To Avoid Sudden Reboots.
- **Patch:** Set the WatchDog PCD to `FALSE` instead of `TRUE`.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22/)

### SPMIDxe:

> [!IMPORTANT]
> Must be paired with the PmicDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Removed the SPMI PIC Init Function.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333/)

### TzDxeLA:

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** The Global TZ Applet Variable has been Changed to `TRUE` from `FALSE`.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)

### UFSDxe:

> [!TIP]
> UFS will still enter Sleep State after Exit Boot Services. <br>
> To prevent this, Set `UEFIExitUfsSSURequired` to `0` in the Configuration Map.

- **Reason:** To allow the usage of UFS.
- **Patch Nr. 1:** The UFS Sleep call has been Replaced with the UFS Wakeup Call.
- **Patch Nr. 2:** Added UFS Link Wake Up.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333) & [N1kroks](https://github.com/N1kroks)

### UsbConfigDxe:

- **Reason:** To allow the usage of the USB Port.
- **Patch:** Removed IOMMU Detach from Exit Boot Services.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### UsbMsdDxe:

- **Reason:** For better Mass Storage usage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)
