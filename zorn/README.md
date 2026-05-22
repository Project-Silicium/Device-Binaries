## Firmware Info

- **Device:** Xiaomi Redmi K80
- **Codename:** zorn

## Patches / Fixes

### ClockDxe

- **Reason:** To avoid early Qualcomm clock initialization hangs during UEFI boot.
- **Patch:** `Clock_InitCESTA` has been patched to return success immediately.
- **Source:** Ported from the same patch class used by peridot/muyu.

### PmicDxe

> [!IMPORTANT]
> Must be paired with the SPMIDxe patch.

- **Reason:** To avoid PMIC initialization crashes or silent hangs during UEFI boot.
- **Patch Nr. 1:** Selected early PMIC constructor calls have been NOPed.
- **Patch Nr. 2:** Minimal PMIC init style routines have been patched to return immediately.
- **Source:** Ported from the same patch class used by peridot/muyu.

### SPMIDxe

> [!IMPORTANT]
> Must be paired with the PmicDxe patch.

- **Reason:** To avoid SPMI init/handle routines crashing or hanging during UEFI boot.
- **Patch:** SPMI handle style routines have been patched to return immediately.
- **Source:** Ported from the same patch class used by peridot/muyu.

### UFSDxe

- **Reason:** To avoid stable hangs or crashes during Qualcomm UFS initialization.
- **Patch Nr. 1:** The UFS Sleep call in the D0 path has been replaced with the UFS Wakeup call.
- **Patch Nr. 2:** The UFS SMMU/IOMMU configuration routine has been patched to return success immediately.
- **Source:** Ported from the same patch class used by peridot/muyu and applied to zorn's own original binary.

### DisplayDxe

> [!IMPORTANT]
> This patch requires `EnableDisplayThread` to be disabled in the configuration map.

- **Reason:** To avoid the display being reset or reinitialized during UEFI boot.
- **Patch Nr. 1:** Selected Qualcomm panel reset and DSI panel init calls have been NOPed.
- **Patch Nr. 2:** The Display IOMMU domain configuration routine has been patched to return success immediately.
- **Source:** Ported from the same patch class used by nuwa and applied to zorn's own original binary.

### ButtonsDxe

- **Reason:** To make the power button usable as Enter in UEFI menus.
- **Patch:** The Qualcomm suspend key code has been changed to the Enter key code.
- **Source:** Ported from the common Xiaomi button workaround and applied to zorn's own original binary.

### UsbConfigDxe

- **Reason:** To avoid USB IOMMU/deinit issues during UEFI bring-up and later boot handoff.
- **Patch Nr. 1:** The USB IOMMU setup routine has been patched to return immediately.
- **Patch Nr. 2:** Selected USB deinit paths have been redirected away from teardown.
- **Source:** Ported from the same patch class used by peridot/muyu and applied to zorn's own original binary.

### UsbMsdDxe

- **Reason:** To improve USB mass-storage behavior in UEFI.
- **Patch:** The removable flag has been changed to non-removable.
- **Source:** Ported from the common Xiaomi USB MSD workaround and applied to zorn's own original binary.

### ACPI Bring-Up Workaround

- **Reason:** zorn currently has no usable ACPI payload, so Pineapple ACPI update loops only produce repeated table lookup failures during bring-up.
- **Patch:** `AcpiPlatformUpdateLib` is overridden with the null implementation and `AcpiPlatformDxe` is not packed into the zorn FV for now.
