## Firmware Infos

- **Device:** Samsung Galaxy Tab A9+ Wi-Fi
- **Region:** EUX (Europe)
- **Version:** `X210RXXS4AYI1` / `BOOT.XF.4.2-00290-MANNARLAZ-2.52377.2`

## Patches / Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- **Reason:** To keep Display turned on while UEFI Boot & To Allow Windows Boot on Debug Builds.
- **Patch Nr. 1:** a Call to a NPA Function has been Removed.
- **Patch Nr. 2:** The LPM Call Backs Function has been Removed.
- **Patch Creator:** [Kernel357](https://github.com/Kernel357) & [N1kroks](https://github.com/N1kroks)

### UsbPwrCtrlDxe (Temporary Patch):

- **Reason:** Pmic dosen't Init Correct, Causing this Driver to not Load Correct.
- **Patch Nr. 1:** The Driver has been Forced to load anyway.
- **Patch Nr. 2:** Driver spamming has been hidden in DEBUG builds 
- **Patch Creator:** [N1kroks](https://github.com/N1kroks) & [index986](https://github.com/index986)

### UsbMsdDxe:

- **Reason:** To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks)
