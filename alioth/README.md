## Patches/Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu)
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UFSDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing a crash.
- Patch: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux and UEFI.
- Patch: Exit BootServices routine was patched to not deinit USB after exit boot services.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- Reason: To be able to boot Windows with debug build.
- Patch: Low Power Mode handler registration has been patched so it does not register LPM mode
- Patch Creator: [N1kroks](https://github.com/N1kroks)

### TzDxeLA:

- Reason: The Common and Keymaster TZ Applets are already loaded, Also we don't have to notify TZ a second time where TZ applets will be loaded to
- Patch: The global variable has been changed to 0x1 so function that notifies tz and loads applets is not called
- Patch Creator: [N1kroks](https://github.com/N1kroks)

### FeatureEnablerDxe:

- Reason: The clock is already turned on, turning it on again will cause framebuffer lose
- Patch: The function that enables clocks has been patched to always return Success.
- Patch Creator: [N1kroks](https://github.com/N1kroks)

### UsbMsdDxe:

- Reason: To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)
