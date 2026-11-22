## Firmware Infos

- **Device:** ZTE Nubia Z80 Ultra
- **Region:** EEA / Global
- **Version:** `BOOT.MXF.2.5.3-00131-KAANAPALI-1.124266.24`

## Patches / Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Creator:** [maroo812](https://github.com/maroo812)

### PmicDxe:

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Minimal PMIC Init has been Removed to avoid a Crash.
- **Patch Creator:** [maroo812](https://github.com/maroo812)

### SPMIDxe:

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Removed the SPMI PIC Init Function.
- **Patch Creator:** [maroo812](https://github.com/maroo812)

### UFSDxe:

- **Reason:** To allow the usage of UFS.
- **Patch Nr. 1:** The UFS Sleep call has been Replaced with the UFS Wakeup Call.
- **Patch Nr. 2:** Added UFS Link Wake Up.
- **Patch Creator:** [maroo812](https://github.com/maroo812)
