## Firmware Info

- Device: LG G8x ThinQ
- Region: Global
- Version: `V85040d OPEN_EU_DS` / `BOOT.XF.3.0.c4-00001-SM8150LZB-2`

## Patches/Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu).
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### DALSYSDxe:

- Reason: To avoid Mismatched Cached Copies.
- Patch: Enabled Cache Coherence for UFS.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbConfigDxe:

- Reason: To Make USB Usable in the OS.
- Patch: Removed USB Deinit from Exit Boot Services.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- Reason: To Make Device Non-Removeable in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)