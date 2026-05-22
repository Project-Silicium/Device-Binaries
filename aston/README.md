## Firmware Infos

- **Device:** OnePlus Ace 3
- **Region:** CN (China)
- **Version:** `PJE110_15.0.0.820` / `BOOT.MXF.2.1.1`

## Patches/Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### ClockDxe:

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch:** The DCD Disable Dependencies Function Call has been Removed.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### DisplayDxe:

> [!NOTE]
> This Patch requires `EnableDisplayThread` to be Disabled in the Configuration Map.

- **Reason:** To get more Control over the Display in UEFI.
- **Patch Nr. 1:** A DSI Close Function call has been removed to avoid turning off Display.
- **Patch Nr. 2:** DSI Panel Reset Function has been removed to avoid turning off the Display.
- **Patch Nr. 3 & 4:** DSI Panel Init Function has been modded to not turn off Display.
- **Patch Nr. 5:** DSI SetMode Function has been modded to not change Clock Frequency
- **Patch Nr. 6:** MMU related setup routine was patched to not recreate already existing MMU domains.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000) & [Shandorman](https://github.com/jiganomegsdfdf)

### PmicDxe:

> [!NOTE]
> Must be paired with the SPMIDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch Nr. 1:** Minimal PMIC Init has been Removed.
- **Patch Nr. 2:** Make failing SPMI Function call always return EFI_SUCCESS.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333/), [Shandorman](https://github.com/jiganomegsdfdf/)

### QcomWDogDxe:

- **Reason:** To avoid Sudden Reboots.
- **Patch:** Set the WatchDog PCD to `FALSE` instead of `TRUE`.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22)

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
