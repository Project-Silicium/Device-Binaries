## Firmware Infos

- **Device:** Xiaomi 11T Pro
- **Region:** EEA (Europe)
- **Version:** `OS1.0.27.0.UKDEUXM` / `BOOT.MXF.1.0-00852-LAHAINA-2.12801.13`

## Patches / Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### ClockDxe:

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch Nr. 1:** The DCD Disable Dependencies Function Call has been Removed.
- **Patch Nr. 2:** The LPM Call Backs Function has been Removed.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/) & [N1kroks](https://github.com/N1kroks/)

### CPRDxe:

- **Reason:** For proper DisplayDxe usage.
- **Patch:** The CPR Cllock Rail Disable Function has been Removed.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22/)

### DisplayDxe:

> [!IMPORTANT]
> This Patch requires `EnableDisplayThread` to be Disabled in the Configuration Map. <br>
> Must also Paired with the CPRDxe Patch.

- **Reason:** To get more Control over the Display in UEFI.
- **Patch Nr. 1:** The IOMMU Domains have been Removed.
- **Patch Nr. 2:** Qcom's Panel Reset Function has been Removed.
- **Patch Nr. 3:** Qcom's DSI Panel Init Function has been Modded.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/) & [Robotix22](https://github.com/Robotix22/)

### FeatureEnablerDxe:

- **Reason:** To not reinit the TZ Appleet which was init by the Bootloader before.
- **Patch:** The TZ Applet Register Function has been Removed.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### UsbConfigDxe:

- **Reason:** To allow the usage of the USB Port.
- **Patch:** Removed IOMMU Detach from Exit Boot Services.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### UsbMsdDxe:

- **Reason:** For better Mass Storage usage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)
