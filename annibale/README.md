## Firmware Infos

- **Device:** Redmi K90
- **Region:** CN (China)
- **Version:** `OS3.0.307.0.WPKCNXM` / `BOOT.MXF.2.5.1-00265-PAKALA-1.104421.2`

## Patches / Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### PmicDxe:

> [!IMPORTANT]
> Must be paired with the SPMIDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch Nr. 1:** Minimal PMIC Init has been Removed to avoid a Crash.
- **Patch Nr. 2:** Two PMIC Init Function Calls have been Removed.
- **Patch Nr. 3:** The PMIC Peripheral Disable Call has been Removed.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333), [Robotix22](https://github.com/Robotix22)

### QcomChargerDxe:

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Some Protocols Calls were Removed.
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
- **Patch Nr. 3:** The Reset Notification now Returns after the UFS Cache Sync, so the UFS Power Down (START STOP UNIT) that never Completes is Skipped and Power Off no longer Hangs.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333) & [N1kroks](https://github.com/N1kroks) (Nr. 1 & 2), [wljf817](https://github.com/wljf817/) (Nr. 3)

### UsbPwrCtrlDxe:

- **Reason:** To make UEFI not Crash when starting USB Device Mode.
- **Patch:** The Charger Port Type Detection of Port 0 has been Changed from PMIC (`2`) to fixed SDP (`6`), so that the PMIC Charger is not Accessed.
- **Patch Creator:** [wljf817](https://github.com/wljf817/)
