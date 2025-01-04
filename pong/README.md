## Patches/Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu)
- Patch: Key code was patched for the power button to be mapped as ENTER instead of Special Samsung Keycode.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### ClockDxe:

- Reason: MDSS reinitializes and we lose framebuffer.
- Patch: DCD Dependency enablement path was patched to not cause MDSS to reinitialize.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### FeatureEnablerDxe:

- Reason: The TZ applet it already brought up.
- Patch: Both DXEs were patched to not start again the TZ applet.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### PmicDxe:

- Reason: To clean up Mass Storage Mode (MSM) output by removing unnecessary spamming
- Patch: Replaced the ```BL``` instruction calling ```EFI_PmicUsbGetChargerPresence``` with a NOP to skip the function entirely.
- Patch Creator: [index986](https://github.com/index986)

### UFSDxe:

- Reason: Makes UFS usable in UEFI and in the OSs.
- Patch Nr. 1: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Nr. 2: UFS Sleep Mode Call has been Replaced with UFS Wake Up Call.
- Patch Nr. 3: The UFS Sleep Mode Function has been Removed.
- Patch Nr. 4: Fixed an issue where UFS would not work due to Exit BootServices
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Kancy Joe](https://github.com/sunflower2333) & [N1kroks](https://github.com/N1kroks)

### UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux.
- Patch: Exit BootServices routine was patched to not deinit USB after exit boot services. Another patch disables recreating IOMMU domains.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- Reason: To Make Device Non-Removeable in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)
