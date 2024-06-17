## Patches/Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### ClockDxe:

- Reason: MDSS reinitializes and we lose framebuffer.
- Patch: DCD Dependency enablement path was patched to not cause MDSS to reinitialize.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### FeatureEnablerDxe:
- Reason: The TZ applet it already brought up.
- Patch: DXE was patched to not start again the TZ applet.
- Patch Creator: [Robotix22](https://github.com/Robotix22)


### PmicDxe (Temporary Patch):

- Reason: Tries to find SPMI handle but failes causing an crash.
- Patch: SPMI handle checks has been patched to always return success.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### UFSDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing the driver to crash.
- Patch Nr. 1: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Nr. 2: An Invalid Return Value has been Removed (Temporary Patch)
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Robotix22](https://github.com/Robotix22)

### UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux.
- Patch Nr1: Exit BootServices routine was patched to not deinit USB after exit boot services.
- Patch Nr2: Disables recreating IOMMU domains.
- Patch Creator: [Robotix22](https://github.com/Robotix22)
