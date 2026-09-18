## Firmware Infos

- **Device:** OnePlus 11
- **Region:** EU (Europe)
- **Version:** `CPH2449_16.0.5.1002` / `BOOT.MXF.2.1.1-00317-KAILUA-1.53303.15`

## Patches / Fixes

### ButtonsDxe

> [!IMPORTANT]
> Patch Nr. 2 is OnePlus only.

- **Reason:** To make the Power Button usable in UEFI.
- **Patch Nr. 1:** The Key Code `SCAN_SUSPEND` has been Changed to the `CHAR_CARRIAGE_RETURN` Key Code.
- **Patch Nr. 2:** Removed S4 Reset Enable Function.
- **Patch Creators:** [Gustave Monce](https://github.com/gus33000/), [Robotix](https://github.com/Robotix22/)

### ClockDxe

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch Nr. 1:** The DCD Enable Dependencies Function Call has been Removed.
- **Patch Nr. 2:** The DCD Disable Dependencies Function Call has been Removed.
- **Patch Creators:** [Robotix](https://github.com/Robotix22/), [Gustave Monce](https://github.com/gus33000/)

### PmicDxe

> [!IMPORTANT]
> Patch Nr. 4 is OnePlus only.

- **Reason:** To prevent a UEFI Crash during Boot.
- **Patch Nr. 1:** Removed PMIC Post Init.
- **Patch Nr. 2:** Removed IRQ Disable Function.
- **Patch Nr. 3:** Removed Lock Config Function.
- **Patch Nr. 4:** Forced Charger Init Finish Flag to `TRUE` instead of `FALSE`.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333/), [Robotix](https://github.com/Robotix22/)

### QcomChargerDxe

> [!IMPORTANT]
> Patch Nr. 2 & 3 are OnePlus only.

- **Reason:** To prevent a UEFI Crash during Boot.
- **Patch Nr. 1:** Removed PMIC Charger Watchdog Toggle.
- **Patch Nr. 2:** Removed Protected PMIC Register Write.
- **Patch Nr. 3:** Removed Charger IC Init Function.
- **Patch Creator:** [Robotix](https://github.com/Robotix22/)

### RscDxe

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch:** Removed Camera Clock Init Call.
- **Patch Creator:** [Robotix](https://github.com/Robotix22/)

### SPMIDxe

- **Reason:** To prevent a UEFI Crash during Boot.
- **Patch:** Removed the SPMI PIC Init Function.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333/)

### TzDxeLA

- **Reason:** To prevent the Re-creation of already Existing TZ Applets.
- **Patch:** The Global TZ Applet Variable has been Changed to `TRUE` from `FALSE`.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)

### UFSDxe

- **Reason:** To allow the usage of the UFS.
- **Patch:** The Unit Ready SCSI Command has been Replaced with the Start/Stop Unit SCSI Command.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333/)

### UsbConfigDxe

- **Reason:** To allow the usage of the USB Port.
- **Patch:** Removed IOMMU Detach from Exit Boot Services.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### UsbMsdDxe

- **Reason:** For better Mass Storage usage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)
