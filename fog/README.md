## Firmware Infos

- **Device:** Xiaomi Redmi 10C
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

### UsbPwrCtrlDxe (Temporary Patch):

- **Reason:** Pmic dosen't Init Correct, Causing this Driver to not Load Correct.
- **Patch:** The Driver has been Forced to load anyway.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks)

### UsbConfigDxe:

- **Reason:** Usefull for Navigating UEFI and the OSs.
- **Patch:** A Check for Platform CLS was Patched to Check for IDP instead.
- **Patch Creator:** [Robotix22](https://github.com/Robotix22)
