## Firmware Infos

- Device: Samsung Galaxy S22 5G
- Region: International
- Version: `S901EXXUCFYDA` / `BOOT.MXF.2.0-00805-WAIPIO-1`

## Patches / Fixes

### ClockDxe:

- Reason: To keep Display turned on while UEFI Boot.
- Patch: The DCD Dependency Enablement Path has been patched to not reinitialize MDSS.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### PmicDxe:

> [!NOTE]
> Must be paired with the SPMIDxe Patch.

- Reason: To make UEFI not Crash during UEFI Boot.
- Patch Nr. 1: Minimal PMIC Init has been Removed to avoid a Crash.
- Patch Nr. 2: The Invalid Power Button Press Check has been to Remove to avoid a sudden Shutdown.
- Patch Creator: [Kancy Joe](https://github.com/sunflower2333) & [Robotix22](https://github.com/Robotix22)

### SdccDxe:

- Reason: To make SD Card "work" in UEFI and to Allow SMMU in the OS.
- Patch: The IOMMU Domains have been Removed.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### SPMIDxe:

> [!NOTE]
> Must be paired with the PmicDxe Patch.

- Reason: To make UEFI not Crash during UEFI Boot.
- Patch: Removed SPMI Handle Function.
- Patch Creator: [Kancy Joe](https://github.com/sunflower2333)

### UFSDxe:

- Reason: To make UEFI be able to use the Internal Storage.
- Patch Nr. 1: The IOMMU Domains have been removed to avoid a Crash.
- Patch Nr. 2: The UFS Sleep call has been Replaced with the UFS Wakeup Call.
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Kancy Joe](https://github.com/sunflower2333)

### UsbConfigDxe:

- Reason: To make USB work in UEFI and the OS.
- Patch Nr. 1: The IOMMU Domains have been removed to avoid a Crash.
- Patch Nr. 2: The USB Deinit Code has been Removed from Exit Boot Services Event to allow the OS to continue using the USB Port.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- Reason: To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)
