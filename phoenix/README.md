## Firmware Info

- Device: POCO X2 / Redmi K30
- Region: China
- Version: `V13.0.6.0.SGHCNXM` / `BOOT.XF.3.1.c3-00001-SM6150LZB-1`

## Patches/Fixes

### ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu)
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### DisplayDxe:

- Reason: MMU Domains for MDP is already setup by the previous firmware and gets re-set again, causing a crash.
- Patch: DisplayDxe setup routine was patched to call MDP Init without initing MMU
- Patch Creator: [Rostislav Lastochkin](https://github.com/remtrik)

### UFSDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing a crash.
- Patch: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)
- Note: UFSDxe from phoenix FW fails to boot due to an unknown reason, use for now surya UFSDxe

### ClockDxe:

- Reason: To be able to boot Windows with debug build.
- Patch: Low Power Mode handler registration has been patched so it does not register LPM mode
- Patch Creator: [N1kroks](https://github.com/N1kroks)

### UsbMsdDxe:

- Reason: To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)

### HALIOMMUDxe:

- Reason: MMU Domains for SDC1, SDC2, SDC4 and USB is already setup by the previous firmware and gets re-set again, causing a crash.
- Patch: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Creator: [N1kroks](https://github.com/N1kroks)

### QcomChargerDxeLA:

- Reason: WatchDog gets enabled, causing a crash with random chance.
- Patch: Patch ChargerPlatform Init function to not enable WatchDog
- Patch Creator: [Rostislav Lastochkin](https://github.com/remtrik)
