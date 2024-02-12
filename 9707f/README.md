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

- Reason: To use USB Port in UEFI for Keyboard, Mouse, etc.
- Patch: USB Mode has been Changed from Device Mode to Host Mode.
- Patch Creator: [CloudSweets](https://github.com/cloudsweets)

- Reason: Is Important to get USB working in Windows / Linux.
- Patch: Exit BootServices routine was patched to not deinit USB after exit boot services.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)
