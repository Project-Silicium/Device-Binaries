## Firmware Infos

- **Device:** OnePlus 15
- **Region:** Global
- **Version:** `CPH2747_16.0.3.501` / `BOOT.MXF.2.5.3-00131-KAANAPALI-1.124230.19`

## Patches / Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### CalibrationDxe:

- **Reason:** To properly Configure the CPU Cores.
- **Patch Nr. 1:** Removed FV Decompress Call.
- **Patch Nr. 2:** Changed Early CPU Core Count from `2` to `0`.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22)

### PmicDxe:

> [!WARNING]
> Patch Nr. 2 is OnePlus only!

> [!IMPORTANT]
> Must be paired with the SPMIDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch Nr. 1:** Minimal PMIC Init has been Removed to avoid a Crash.
- **Patch Nr. 2:** Removed Battery Presence Protocol Function.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333), [Robotix22](https://github.com/Robotix22)

### QcomChargerDxe:

> [!WARNING]
> This Patch is OnePlus only!

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Removed PMIC Register Writes.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22)

### QcomWDogDxe:

- **Reason:** To avoid Sudden Reboots.
- **Patch:** Set the WatchDog PCD to `FALSE` instead of `TRUE`.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22)

### SPMIDxe:

> [!IMPORTANT]
> Must be paired with the PmicDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Removed the SPMI PIC Init Function.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333)

### TzDxeLA:

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** The Global TZ Applet Variable has been Changed to `TRUE` from `FALSE`.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)

### UFSDxe:

- **Reason:** To allow the usage of UFS.
- **Patch Nr. 1:** The UFS Sleep call has been Replaced with the UFS Wakeup Call.
- **Patch Nr. 2:** Added UFS Link Wake Up.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333) & [N1kroks](https://github.com/N1kroks)

### UsbConfigDxe:

- **Reason:** To allow the usage of the USB Port.
- **Patch:** Removed IOMMU Detach from Exit Boot Services.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- **Reason:** For better Mass Storage usage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks)
