## Firmware Infos

- **Device:** OnePlus 13R
- **Region:** IN
- **Version:** `CPH2691_16.0.2.400(EX01)` / `BOOT.MXF.2.1-01933-LANAI-1.78403.38`

## Patches/Fixes

### ButtonsDxe:

- **Reason:** To make the Power Button usable in UEFI.
- **Patch:** Map power button Key Code as ENTER instead of SUSPEND.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- **Reason:** To keep some important clocks on.
- **Patch:** Removed "DCDDisableDependencies" function call.
- **Patch Creator:** [Robotix](https://github.com/Robotix22)

### PmicDxe:

> [!NOTE]
> Patch Nr. 2 is OnePlus only!

> [!IMPORTANT]
> Must be paired with the SPMIDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch Nr. 1:** Make failing SPMI function immediately return EFI_SUCCESS.
- **Patch Nr. 2:** Make check dead battery function immediately return success.
- **Patch Creators:** [Kancy Joe](https://github.com/sunflower2333), [Robotix22](https://github.com/Robotix22)

### QcomWDogDxe:

- **Reason:** To avoid a sudden Reboot in UEFI.
- **Patch:** Disabled Watchdog Timeout.
- **Patch Creator:** [Shandorman](https://github.com/jiganomegsdfdf)

### SPMIDxe:

> [!IMPORTANT]
> Must be paired with the PmicDxe Patch.

- **Reason:** To make UEFI not Crash during UEFI Boot.
- **Patch:** Removed SPMI Handle Function.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333)

### UFSDxe:

- **Reason:** To make UEFI be able to use the Internal Storage.
- **Patch:** The UFS Sleep call has been Replaced with the UFS Wakeup Call.
- **Patch Creator:** [Kancy Joe](https://github.com/sunflower2333)

### UsbConfigDxe:

- **Reason:** To make USB work in UEFI and the OS.
- **Patch:** ExitBootServices routine was patched to not deinit USB after exit boot services.
- **Patch Creator:** [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- **Reason:** To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- **Patch:** Changed Removable State to Non-Removable.
- **Patch Creator:** [N1kroks](https://github.com/N1kroks)

