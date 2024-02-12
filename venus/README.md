## Patches/Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### ClockDxe:

- Reason: MDSS reinitializes and we lose framebuffer.
- Patch: DCD Dependency enablement path was patched to not cause MDSS to reinitialize.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### FeatureEnablerDxe & MinidumpTADxe:

- Reason: The TZ applet it already brought up.
- Patch: Both DXEs were patched to not start again the TZ applet.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### QcomWDogDxe:

- Reason: ReturnStatusCodeHandler implementation is different.
- Patch: Dependency check routine was patched to not fail.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UFSDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing a crash.
- Patch: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux and UEFI.
- Patch Nr. 1: Exit BootServices routine was patched to not deinit USB after exit boot services. Another patch disables recreating IOMMU domains.
- Patch Nr. 2: USB Mode has been Changed from Device Mode to Host Mode.
- Patch Nr. 3: USB Power has been Forced to be Enabled
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [CloudSweets](https://github.com/cloudsweets) & [N1kroks](https://github.com/N1kroks)
