## Firmware Infos

- **Device:** Realme GT Neo6
- **Region:** CN
- **Version:** `RMX3852_15.0.0.1350` / `BOOT.MXF.2.1-01933-LANAI-1.78403.24`

## Patches/Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** Map power button Key Code as ENTER instead of SUSPEND.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- **Reason:** To keep some important clocks on.
- **Patch:** Removed "Clock_CESTADisableDependencies" function call.
- **Patch Creator:** [Robotix](https://github.com/Robotix22)

### PmicDxe:

> [!NOTE]
> Must be paired with the SPMIDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch Nr. 1:** Force call of "dead_battery_check" to avoid a crash when using the default value.
- **Patch Nr. 2:** Make failing SPMI Function call always return EFI_SUCCESS.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333) & [Shandorman](https://github.com/jiganomegsdfdf)

### QcomWDogDxe:

- **Reason:** To avoid a sudden Reboot in UEFI.
- **Patch:** Disabled Watchdog Timeout.
- **Patch Creator:** [Shandorman](https://github.com/jiganomegsdfdf)

### SPMIDxe:

> [!NOTE]
> Must be paired with the PmicDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Removed SPMI Handle Function.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333)

### TzDxeLA:

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** The Global TZ Applet Variable has been Changed to `TRUE` from `FALSE`.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks/)

### UFSDxe:

- **Reason:** To make UEFI be able to use the Internal Storage.
- **Patch Nr. 1:** The UFS Sleep call has been Replaced with the UFS Wakeup Call.
- **Patch Nr. 2:** Added UFS Gear Wake Up call.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333) & [N1kroks](https://github.com/N1kroks)

### UsbConfigDxe:

- **Reason:** To make USB work in UEFI and the OS.
- **Patch:** ExitBootServices routine was patched to not deinit USB after exit boot services.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- **Reason:** To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks)

