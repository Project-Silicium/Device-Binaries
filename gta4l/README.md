## Patches/Fixes

### ClockDxe (Temporary Patch):

- Reason: A Npa Node gets Registert wich kills Display.
- Patch: That Node Register has been removed to avoid killing Display.
- Patch Creator: [Kernel357](https://github.com/Kernel357) & [Robotix22](https://github.com/Robotix22)

### HALIOMMU:

- Reason: IOMMUs for USB, eMMC and SD Card are already present, If reset again UEFI crashes.
- Patch: IOMMU for USB, eMMC and SD Card has been patched to always return Success.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### UsbConfigDxe:

- Reason: Usefull for Navigating UEFI and the OSs.
- Patch: A Check for Platform CLS was Patched to Check for every other Platform instead.
- Patch Creator: [Robotix22](https://github.com/Robotix22)
