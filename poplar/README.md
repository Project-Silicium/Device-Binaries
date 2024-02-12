## Patches/Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch Nr. 1: Key Code was Patched for the Power Button to be mapped as ENTER instead of SUSPEND.
- Patch Nr. 2: Key Code was Patched for the Kamera Button to be mapped as ESC instead of ENTER.
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Robotix22](https://github.com/Robotix22)

### ClockDxe:

- Reason: Help Avoiding Being Stuck at this Driver.
- Patch: Some Calls to Display Clocks have been Removed.
- Patch Creator: [Sheep Sun](https://github.com/fxsheep)

### UsbConfigDxe:

- Reason: Usefull for Navigating UEFI and the OSs.
- Patch Nr. 1: A Check for Platform CLS was Patched to Check for MTP instead.
- Patch Nr. 2: Exit Boot Services Event has been Removed to Have working USB in the OSs
- Patch Creator: [Robotix22](https://github.com/Robotix22)
