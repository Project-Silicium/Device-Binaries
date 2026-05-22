## Firmware Infos

- **Device:** Samsung Galaxy S21 FE 5G
- **Region:** INS (India)
- **Version:** `G990B2XXS8GXF3` / `BOOT.MXF.1.0-00872-LAHAINA-2`

## Patches/Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch Nr. 1:** The Special Samsung Key Code (`0x80`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Nr. 2:** The Button Handlening has been Modded to allow Unichar Key Codes.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22)

### ClockDxe:

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch:** The DCD Dependency Enablement Path has been patched to avoid reinitialize MDSS.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### TzDxeLA:

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** The Global TZ Applet Variable has been Changed to `TRUE` from `FALSE`.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)

### UsbConfigDxe:

- **Reason:** To make USB work in the OS.
- **Patch:** The USB Deinit Code has been Removed from Exit Boot Services Event to allow the OS to continue using the USB Port.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)
