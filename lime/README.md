## Firmware Infos

- **Device:** Xiaomi Redmi 9T
- **Region:** Global
- **Version:** `V13.0.6.0.SJQMIXM` / `BOOT.XF.4.1-00335-KAMORTALAZ-1.572417.1.586717.1`

## Patches/Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Key Code `SCAN_SUSPEND` has been Changed to the `CHAR_CARRIAGE_RETURN` Key Code.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### ClockDxe:

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch:** Removed `/clk/mmrt` from ClockBSP.
- **Patch Creator:** [Robotix](https://github.com/Robotix22/)

### UsbMsdDxe:

- **Reason:** For better Mass Storage usage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)
