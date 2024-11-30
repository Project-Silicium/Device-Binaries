## Patches/Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- Reason: MDSS reinitializes and we lose framebuffer, Makes Windows Boot work on Debug Builds.
- Patch Nr. 1: DCD Dependency enablement path was patched to not cause MDSS to reinitialize.
- Patch Nr. 2: LPM Call Backs Function has been Removed.
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [N1kroks](https://github.com/N1kroks)

### FeatureEnablerDxe:

- Reason: The TZ applet it already brought up.
- Patch: Both DXEs were patched to not start again the TZ applet.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UFSDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing a crash.
- Patch: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux.
- Patch Nr. 1: USB0/1 IOMMU Domains got Removed.
- Patch Nr. 2: Removed USB Deinit from Exit Boot Services.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- Reason: To Make Device Non-Removeable in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)
