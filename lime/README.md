## Firmware Infos

- **Device:** Xiaomi Redmi 9T
- **Region:** Global
- **Version:** `V13.0.6.0.SJQMIXM` / `BOOT.XF.4.1-00335-KAMORTALAZ-1.572417.1.586717.1`

## Patches/Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- **Reason:** To keep Display turned on while UEFI Boot & To Allow Windows Boot on Debug Builds.
- **Patch Nr. 1:** a Call to a NPA Function has been Removed.
- **Patch Nr. 2:** The LPM Call Backs Function has been Removed.
- **Patch Creator:** [Kernel357](https://github.com/Kernel357) & [N1kroks](https://github.com/N1kroks)

### DALSYSDxe:

- **Reason:** To avoid Mismatched Cached Copies.
- **Patch:** Enabled Cache Coherence for UFS.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- **Reason:** To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks)
