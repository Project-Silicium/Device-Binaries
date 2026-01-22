## Firmware Infos

- **Device:** Realme GT Neo 5
- **Region:** CN
- **Version:** `RMX3706_15.0.0.500` / `BOOT.MXF.2.0-00925.2-WAIPIO-1.22250.6.39858.1`

## Patches/Fixes

### ButtonsDxe:

- **Reason:** To make the Side Buttons usable in UEFI.
- **Patch Nr. 1:** The Special Qcom Key Code (`0x102`) has been Changed to the Key Code Enter (`0xD`).
- **Patch Nr. 2:** Swaped Volume Button Key Codes.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000) & [Rostislav Lastochkin](https://github.com/remtrik)

### ClockDxe:

- **Reason:** To keep Display turned on while UEFI Boot.
- **Patch:** The DCD Dependency Enablement Path has been patched to not reinitialize MDSS.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### PmicDxe:

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch Nr. 1:** Make failing SPMI Function call always return EFI_SUCCESS.
- **Patch Nr. 2:** Make some failing functions return 0 (patched on this device only).
- **Patch Nr. 3:** Do not call some functions (at 0x3eb0), taken from sunflower2333's patch for sheng
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333) & [Shandorman](https://github.com/jiganomegsdfdf) & [artempeshkov](https://github.com/artempeshkov) 

### UFSDxe:

- **Reason:** To make UEFI be able to use the Internal Storage.
- **Patch:** The UFS Sleep call has been Replaced with the UFS Wakeup Call.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333)

### UsbConfigDxe:

- **Reason:** To make USB work in UEFI and the OS.
- **Patch:** The USB Deinit Code has been Removed from Exit Boot Services Event to allow the OS to continue using the USB Port.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- **Reason:** To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks)
