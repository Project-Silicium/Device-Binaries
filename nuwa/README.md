## Firmware Infos

- **Device:** Xiaomi 13 Pro
- **Region:** EEA (Europe)
- **Version:** `OS2.0.110.0.VMBEUXM` / `BOOT.MXF.2.1.1-00218-KAILUA-1.36233.1`

## Patches / Fixes

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
- **Patch Nr. 1:** The IOMMU Domains have been Removed.
- **Patch Nr. 2:** Qcom's Panel Reset Function has been Removed.
- **Patch Nr. 3:** Qcom's DSI Panel Init Function has been Modded.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/) & [Robotix22](https://github.com/Robotix22/)

### PmicDxe:

> [!NOTE]
> Must be paired with the SPMIDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Minimal PMIC Init has been Removed.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333/)

### SPMIDxe:

> [!NOTE]
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

## Raw File Changes

## Panel_M2_38_0c_0a_dsc_cmd.xml

- **Reason:** To have Proper Display Init in UEFI.
- **Change Nr. 1:** The `DSIAutoRefreshFrameNumDiv` has been Updated from `60` to `1`.
- **Change Nr. 2:** Removed Brightness Commands from `DSIInitSequence`.
- **Change Creator:** [Robotix](https://github.com/Robotix22/), [Aistop](https://github.com/AistopGit/)
