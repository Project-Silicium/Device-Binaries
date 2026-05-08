## Firmware Infos

- **Device:** OnePlus 6
- **Region:** Global
- **Version:** OxygenOS 11.1.2.2

## Patches/Fixes

> [!IMPORTANT]
> PmicDxe and UsbConfigDxe were taken from QTI WP firmware for USB Dual Role in UEFI.

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- **Reason:** To allow Windows to boot on Debug Builds.
- **Patch:** The LPM Call Backs Function has been Removed.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks)

### DisplayDxe:

- **Reason:** To get more Control over the Display in UEFI.
- **Patch Nr. 1:** Qcom's Panel Reset Function has been Removed.
- **Patch Nr. 2:** Qcom's DSI Panel Init Function has been Modded.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/) & [Robotix22](https://github.com/Robotix22/)

### UsbMsdDxe:

- **Reason:** To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks)

