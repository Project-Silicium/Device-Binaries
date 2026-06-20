## Firmware Infos

- **Device:** OnePlus 13
- **Region:** ROW
- **Version:** `CPH2653_16.0.7.201` / `BOOT.MXF.2.5.1`

## Patches / Fixes

> [!WARNING]
> These Patches are Outdated & Unstable!

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Special Qcom Key Code (`0x120`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### CalibrationDxe:

- **Reason:** To properly Configure the CPU Cores.
- **Patch Nr. 1:** Removed FV Decompress Call.
- **Patch Nr. 2:** Changed Early CPU Core Count from `2` to `0`.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22)

### PmicDxe:

> [!NOTE]
> Must be paired with the SPMIDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch Nr. 1:** SPMI Protocol Handle Function has been Removed.
- **Patch Nr. 2:** The Function `EFI_DeadBattery` OnePlus Function has been Removed.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333) & [Robotix22](https://github.com/Robotix22)

### SPMIDxe:

> [!NOTE]
> Must be paired with the PmicDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Removed SPMI Handle Function.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333)

### QcomChargerDxe:

> [!WARNING]
> Patch Nr. 1 is OnePlus only!

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch Nr. 1:** a PMIC Register Function Call has been Removed.
- **Patch Nr. 2:** Some Protocols Calls were Removed <!-- TODO: Get more Infos about this. -->
- **Patch Creator:** [Robotix22](https://github.com/Robotix22)

### QcomWDogDxe:

- **Reason:** To avoid Sudden Reboots.
- **Patch:** Set the WatchDog PCD to `FALSE` instead of `TRUE`.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22)

### TzDxeLA:

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** The Global TZ Applet Variable has been Changed to `TRUE` from `FALSE`.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)

### UFSDxe:

- **Reason:** To make UEFI be able to use the Internal Storage.
- **Patch Nr. 1:** The UFS Sleep call has been Replaced with the UFS Wakeup Call.
- **Patch Nr. 2:** Force UFS Link Wake Up Function to run before Gear Check.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333) & [N1kroks](https://github.com/N1kroks)

### UsbConfigDxe:

- **Reason:** To make USB work in UEFI and the OS.
- **Patch:** The USB Deinit Code has been Removed from Exit Boot Services Event to allow the OS to continue using the USB Port.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- **Reason:** To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks)
