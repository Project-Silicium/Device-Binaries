## Patches/Fixes

### ButtonsDxe:

- Reason: To make the Power Button usable in UEFI.
- Patch: Map power button Key Code as ENTER instead of SUSPEND.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### ClockDxe:

- Reason: To keep Display turned on while UEFI Boot.
- Patch: The DCD Dependency Enablement Path has been patched to not reinitialize MDSS.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### DisplayDxe:

> [!NOTE]
> This Patch requires `EnableDisplayThread` to be Disabled in the Configuration Map.

- Reason: To get more Control over the Display in UEFI.
- Patch Nr. 1: A DSI Close Function call has been removed to avoid turning off Display.
- Patch Nr. 2: DSI Panel Reset Function has been removed to avoid turning off the Display.
- Patch Nr. 3 & 4: DSI Panel Init Function has been modded to not turn off Display.
- Patch Nr. 5: DSI SetMode Function has been modded to not change Clock Frequency
- Patch Nr. 6: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Shandorman](https://github.com/jiganomegsdfdf)

### FeatureEnablerDxe:

- Reason: To not reinit the TZ Appleet which was init by the Bootloader before.
- Patch: The TZ Applet Register Function has been Removed.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### PmicDxe:

> [!NOTE]
> Must be paired with the SPMIDxe Patch.

- Reason: To make UEFI not Crash during UEFI Boot.
- Patch Nr. 1: Force call of "dead_battery_check" to avoid a crash when using the default value.
- Patch Nr. 2: Make failing SPMI Function call always return EFI_SUCCESS.
- Patch Creator: [Kancy Joe](https://github.com/sunflower2333) & [Shandorman](https://github.com/jiganomegsdfdf)

### QcomWDogDxe:

- Reason: To avoid a sudden Reboot in UEFI.
- Patch: Disabled Watchdog Timeout.
- Patch Creator: [Shandorman](https://github.com/jiganomegsdfdf)

### SPMIDxe:

> [!NOTE]
> Must be paired with the PmicDxe Patch.

- Reason: To make UEFI not Crash during UEFI Boot.
- Patch: Removed SPMI Handle Function.
- Patch Creator: [Kancy Joe](https://github.com/sunflower2333)

### UFSDxe:

- Reason: To make UEFI be able to use the Internal Storage.
- Patch Nr. 1: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Nr. 2: The UFS Sleep call has been Replaced with the UFS Wakeup Call.
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Kancy Joe](https://github.com/sunflower2333)

### UsbConfigDxe:

- Reason: To make USB work in UEFI and the OS.
- Patch Nr. 1: ExitBootServices routine was patched to not deinit USB after exit boot services.
- Patch Nr. 2: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### UsbMsdDxe:

- Reason: To make the Internal Storage be recognised as Hard Drives instead of USB Drives in Mass Storage.
- Patch: Changed Removable State to Non-Removable.
- Patch Creator: [N1kroks](https://github.com/N1kroks)
