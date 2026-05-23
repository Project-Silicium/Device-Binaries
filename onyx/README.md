## Firmware Infos

- **Device:** Xiaomi POCO F7
- **Region:** Global
- **Version:** `OS3.0.7.0.WOLMIXM` / `BOOT.MXF.2.5.1-00265-PAKALA-1.104421.2`

## Patches / Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch** The CESTA Init Function has been Removed.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22)

### FeatureEnablerDxe:

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch:** Removed the Display Clock Init Function.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks)

### PmicDxe:

> [!IMPORTANT]
> Must be paired with the SPMIDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Minimal PMIC Init has been Removed.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333/)

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
