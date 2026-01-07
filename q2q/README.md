## Firmware Infos

- **Device:** Samsung Galaxy Z Fold3 5G
- **Region:** DTM (Germany)
- **Version:** `F926BXXS1CVCA` / `BOOT.MXF.1.0-00815-LAHAINA-1`

## Patches/Fixes

### ClockDxe:

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch:** The DCD Dependency Enablement Path has been patched to avoid reinitialize MDSS.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### FeatureEnablerDxe:

- **Reason:** To not reinit the TZ Appleet which was init by the Bootloader before.
- **Patch:** The TZ Applet Register Function has been Removed.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### UsbConfigDxe:

- **Reason:** To make USB work in the OS.
- **Patch:** The USB Deinit Code has been Removed from Exit Boot Services Event to allow the OS to continue using the USB Port.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)
