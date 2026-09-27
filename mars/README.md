## Firmware Info

- **Device:** Meizu 20 Infinity
- **Version:** `BOOT.MXF.2.1.1-00102-KAILUA-1.21534.5`

## Patches / Fixes

### ButtonsDxe

- Maps the Qualcomm power-button key code (`0x102`) to Enter (`0xD`).

### ClockDxe

- Removes the DCD disable-dependencies call so the display remains enabled.

### DisplayDxe

- Skips recreating display IOMMU domains inherited from ABL.
- Skips DSI close, panel reset and clock-changing set-mode paths that turn off or crash the inherited display.
- Requires `EnableDisplayThread` to be disabled in the configuration map.

### PmicDxe

- Skips PMIC initialization paths that conflict with the state inherited from ABL.
- Must be used together with the SPMIDxe patch.

### QcomChargerDxe

- Skips charger operations that access the inherited PMIC through SPMI and cause a synchronous exception.

### SPMIDxe

- Skips SPMI PIC initialization to avoid reinitializing the controller state inherited from ABL.
- Must be used together with the PmicDxe patch.

### TzDxeLA

- Marks the global TZ applet as already initialized.

### UFSDxe

- Replaces the UFS sleep transition with a link wake-up call.

### UsbConfigDxe

- Skips IOMMU detach during ExitBootServices.

### UsbMsdDxe

- Reports mass-storage media as non-removable.
