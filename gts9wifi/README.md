## Firmware Infos

- **Device:** Samsung Galaxy Tab S9 Wi-Fi (SM-X710)
- **Region:** EUX
- **Version:** `X710XXS5BYA5` / `BOOT.MXF.2.1.1-00218-KAILUA-1`

## Patches / Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Power Key now sends `CHAR_CARRIAGE_RETURN` instead of Scan Code `0x80`.
- **Patch Creator:** [nacht20-de](https://github.com/nacht20-de), based on the gts8p Patch by [Robotix22](https://github.com/Robotix22/)

### ClockDxe:

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch:** The DCD Disable Dependencies Function Call has been Removed.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### PmicDxe:

> [!NOTE]
> Must be paired with the SPMIDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Minimal PMIC Init has been Removed to avoid a Crash.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333)

### SPMIDxe:

> [!NOTE]
> Must be paired with the PmicDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Removed the SPMI PIC Init Function.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333)

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
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- **Reason:** For better Mass Storage usage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks)
