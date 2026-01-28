## Firmware Infos

- **Device:** OnePlus 13s
- **Region:** IN (India)
- **Version:** `CPH2723_16.0.3.501` / `BOOT.MXF.2.5.1-00265-PAKALA-1.104700.16`

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

### ClockDxe:

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch** The CESTA Disable Dependencies Function Call has been Removed.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22)

### FeatureEnablerDxe:

- **Reason:** To not reinit the TZ Applet which was init by the Bootloader before.
- **Patch:** The TZ Applet Register Function has been Removed.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### PmicDxe:

> [!WARNING]
> Patch Nr. 2 & 3 is OnePlus only!

> [!IMPORTANT]
> Must be paired with the SPMIDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch Nr. 1:** Minimal PMIC Init has been Removed to avoid a Crash.
- **Patch Nr. 2:** Some Battery Function call has been Removed. <!-- TODO: Figure out what that Function actually was. -->
- **Patch Nr. 3:** Removed Battery Presence Protocol Function.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333), [Robotix22](https://github.com/Robotix22)

### QcomChargerDxe:

> [!WARNING]
> Patch Nr. 1 is OnePlus only!

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch Nr. 1:** a PMIC Register Function Call has been Removed.
- **Patch Nr. 2:** Some Protocols Calls were Removed <!-- TODO: Get more Infos about this. -->
- **Patch Creator:** [Robotix22](https://github.com/Robotix22)

## QcomWDogDxe:

- **Reason:** To avoid Sudden Reboots.
- **Patch:** Set the WatchDog PCD to `FALSE` instead of `TRUE`.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22)

### SPMIDxe:

> [!IMPORTANT]
> Must be paired with the PmicDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Removed the SPMI PIC Init Function.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333)

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
