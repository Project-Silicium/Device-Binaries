## Patches/Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- Reason: To keep Display Alive during Boot & Making Windows Boot on Debug Builds.
- Patch Nr. 1: a NPA Function has been Removed.
- Patch Nr. 2: LPM Call Backs Function has been Removed.
- Patch Creator: [Kernel357](https://github.com/Kernel357) & [Robotix22](https://github.com/Robotix22) & [N1kroks](https://github.com/N1kroks)

### HALIOMMU:

- Reason: IOMMUs for USB and eMMC are already present, If reset again UEFI crashes.
- Patch: IOMMU for USB and eMMC has been patched to always return Success.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### UsbConfigDxe:

- Reason: Usefull for Navigating UEFI and the OSs.
- Patch: A Check for Platform CLS was Patched to Check for IDP instead.
- Patch Creator: [Robotix22](https://github.com/Robotix22)
