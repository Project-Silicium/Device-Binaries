## Firmware Info

- Device: Xiaomi Redmi Note 13 Pro 5G
- Region: EEA
- Version: `OS3.0.301.0.WNREUXM` / `BOOT.MXF.2.0-01018.3-WAIPIO-1`

## Patches / Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### UFSDxe:

- **Reason:** To allow the usage of UFS.
- **Patch:** The UFS Sleep call has been Replaced with the UFS Wakeup Call.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333/)

### UsbMsdDxe:

- **Reason:** For better Mass Storage usage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)
