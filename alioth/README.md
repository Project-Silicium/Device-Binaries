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
