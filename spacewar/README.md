## Patches/Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### FeatureEnablerDxe & MinidumpTADxe:

- Reason: The TZ applet it already brought up.
- Patch: Both DXEs were patched to not start again the TZ applet.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux and UEFI.
- Patch Nr. 1: Exit BootServices routine was patched to not deinit USB after exit boot services.
- Patch Nr. 2: USB Mode has been Changed from Device Mode to Host Mode (use host patch dxe).
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [CloudSweets](https://github.com/cloudsweets)
