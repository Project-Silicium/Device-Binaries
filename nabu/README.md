## Firmware Info

- Device: Xiaomi Pad 5
- Region: Global
- Version: `OS1.0.6.0.TKXMIXM` / `BOOT.XF.3.0-00571-SM8150LZB-4.402715.1`

## Patches/Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- Reason: Makes Windows Boot work on Debug Builds.
- Patch: LPM Call Backs Function has been Removed.
- Patch Creator: [N1kroks](https://github.com/N1kroks)

### DALSYSDxe:

- **Reason:** To avoid Mismatched Cached Copies.
- **Patch:** Enabled Cache Coherence for UFS.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### UsbConfigDxe:

- Reason: To Make USB Usable in the OS.
- Patch: Removed USB Deinit from Exit Boot Services.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- Reason: To Make Device Non-Removeable in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)
