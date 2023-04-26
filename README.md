# MU-Qcom Binaries from Qualcomm Snapdragon Devices

## Patches

### Galaxy Tab S8 5G

```
ClockDxe:

- Reason: MDSS reinitializes and we lose framebuffer.
- Patch: DCD Dependency enablement path was patched to not cause MDSS to reinitialize.

HALIOMMU:

- Reason: A DTB Protocol can't be found, causing the driver to crash.
- Patch: DTB Protocol check has be patched to always return Success.

SdccDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing the driver to crash.
- Patch: MMU related setup routine was patched to not recreate already existing MMU domains, another Patch removes an ASSERT Function.

UFSDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing the driver to crash.
- Patch: MMU related setup routine was patched to not recreate already existing MMU domains.
```

### Galaxy Z Fold 3 5G

```
ClockDxe:

- Reason: MDSS reinitializes and we lose framebuffer.
- Patch: DCD Dependency enablement path was patched to not cause MDSS to reinitialize.

FeatureEnablerDxe & MinidumpTADxe:

- Reason: The TZ applet it already brought up.
- Patch: Both DXEs were patched to not start again the TZ applet.

QcomWDogDxe:

- Reason: ReturnStatusCodeHandler implementation is different.
- Patch: Dependency check routine was patched to not fail.

UFSDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing a crash.
- Patch: MMU related setup routine was patched to not recreate already existing MMU domains.

UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux.
- Patch: Exit BootServices routine was patched to not deinit USB after exit boot services. Another patch disables recreating IOMMU domains.
```

### Xiaomi 11T Pro

```
ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu)
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.

ClockDxe:

- Reason: MDSS reinitializes and we lose framebuffer.
- Patch: DCD Dependency enablement path was patched to not cause MDSS to reinitialize.

FeatureEnablerDxe & MinidumpTADxe:

- Reason: The TZ applet it already brought up.
- Patch: Both DXEs were patched to not start again the TZ applet.

PmicDxe:

- Reason: The PMIC AUX chip is already powered on by the previous firmware.
- Patch: PMIC AUX (LEICA) init sequence was patched to not fail.

QcomWDogDxe:

- Reason: ReturnStatusCodeHandler implementation is different.
- Patch: Dependency check routine was patched to not fail.

UFSDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing a crash.
- Patch: MMU related setup routine was patched to not recreate already existing MMU domains.

UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux.
- Patch: Exit BootServices routine was patched to not deinit USB after exit boot services. Another patch disables recreating IOMMU domains.
```

### Mi A3

```
ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu)
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.

ClockDxe:

- Reason: Functions already set up something causing a crash trying to reset them again.
- Patch: The code that was causing the problem has been removed (we don't know what it does at the moment, but this patch allows you to run ClockDxe)
```

### Redmi Note 8/8T

```
ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu)
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.

ClockDxe:

- Reason: Functions already set up something causing a crash trying to reset them again.
- Patch: The code that was causing the problem has been removed (we don't know what it does at the moment, but this patch allows you to run ClockDxe)
```

### Redmi 9T

```
ButtonsDxe:

- Reason: Helps navigating Menus (e.g. UEFI Menu)
- Patch: Key code was patched for the power button to be mapped as ENTER instead of SUSPEND.

ClockDxe:

- Reason: Functions already set up something causing a crash trying to reset them again.
- Patch: The code that was causing the problem has been removed (we don't know what it does at the moment, but this patch allows you to run ClockDxe)
```
