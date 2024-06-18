## Patches/Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- Reason: MDSS reinitializes and we lose framebuffer.
- Patch: DCD Dependency enablement path was patched to not cause MDSS to reinitialize.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### FeatureEnablerDxe:

- Reason: The TZ applet it already brought up.
- Patch: DXE was patched to not start again the TZ applet.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### PmicDxe:

- Reason: Tries to Set PMIC to Sleep Mode but failes to do so (Incorrect?).
- Patch: The PMIC has been Set to Awake Mode (Incorrect?).
- Patch Creator: [Kancy Joe](https://github.com/sunflower2333)

### UFSDxe:

- Reason: Makes UFS usable in UEFI and in the OSs.
- Patch Nr. 1: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Nr. 2: UFS Sleep Mode Call has been Replaced with UFS Wake Up Call.
- Patch Nr. 3: The UFS Sleep Mode Function has been Removed.
- Patch Nr. 4: Fixed an issue where UFS would not work due to Exit BootServices
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Kancy Joe](https://github.com/sunflower2333) & [N1kroks](https://github.com/N1kroks)

### UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux and UEFI.
- Patch Nr. 1: Exit BootServices routine was patched to not deinit USB after exit boot services.
- Patch Nr. 2: USB Mode has been Changed from Device Mode to Host Mode.
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [CloudSweets](https://github.com/cloudsweets)
