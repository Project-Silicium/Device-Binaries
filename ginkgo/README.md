## Patches/Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### ClockDxe (Temporary Patch):

- Reason: A Npa Node gets Registert wich kills Display.
- Patch: That Node Register has been removed to avoid killing Display.
- Patch Creator: [Kernel357](https://github.com/Kernel357) & [Robotix22](https://github.com/Robotix22)

### HALIOMMU:

- Reason: IOMMUs for USB and eMMC are already present, If reset again UEFI crashes.
- Patch: IOMMU for USB and eMMC has been patched to always return Success.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### UsbConfigDxe:

- Reason: Usefull for Navigating UEFI and the OSs.
- Patch: A Check for Platform CLS was Patched to Check for IDP instead.
- Patch Creator: [Robotix22](https://github.com/Robotix22)
