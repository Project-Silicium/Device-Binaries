## Firmware Infos

- **Device:** Xiaomi Mi A3
- **Region:** ?
- **Version:** ?

## Patches/Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch:** a Call to a NPA Function has been Removed.
- **Patch Creator:** [Kernel357](https://github.com/Kernel357)
