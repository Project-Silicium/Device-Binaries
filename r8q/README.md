## Firmware Infos

- Device: Samsung Galaxy S20 FE
- Region: DBT (Germany)
- Version: `G780GXXSHEYJ1` / `BOOT.XF.3.2-00278-SM8250-2`

## Patches/Fixes

- **Reason:** To make the Power Button usable in UEFI.
- **Patch Nr. 1:** The Special Samsung Key Code (`0x80`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Nr. 2:** The Button Handlening has been Modded to allow Unichar Key Codes.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22/)

### TzDxeLA:

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** The Global TZ Applet Variable has been Changed to `TRUE` from `FALSE`.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)

### UsbConfigDxe:

- **Reason:** To allow the usage of the USB Port.
- **Patch:** Removed IOMMU Detach from Exit Boot Services.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000/)

### UsbMsdDxe:

- **Reason:** For better Mass Storage usage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)
