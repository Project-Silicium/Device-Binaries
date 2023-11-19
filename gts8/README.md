## Patches/Fixes

### ClockDxe:

- Reason: MDSS reinitializes and we lose framebuffer.
- Patch: DCD Dependency enablement path was patched to not cause MDSS to reinitialize.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)

### ParserDxe:

- Reason: ParsrLck can't be found by the Driver causing the Driver not to load.
- Patch: ParsrLck check has ben patched to not fail.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### PmicDxe (Temporary Patch):

- Reason: Tries to find SPMI handle but failes causing an crash.
- Patch: SPMI handle checks has ben patched to always return success.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### HALIOMMU (Temporary Patch):

- Reason: A DTB Protocol can't be found, causing the driver to crash.
- Patch: DTB Protocol check has be patched to always return Success.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### SdccDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing the driver to crash.
- Patch: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Creator: [Robotix22](https://github.com/Robotix22)

### UFSDxe:

- Reason: An MMU Domain is already setup by the previous firmware and gets re-set again, causing the driver to crash.
- Patch Nr. 1: MMU related setup routine was patched to not recreate already existing MMU domains.
- Patch Nr. 2: An Invalid Return Value has been Removed (Temporary Patch)
- Patch Creator: [Gustave Monce](https://github.com/gus33000) & [Robotix22](https://github.com/Robotix22)

### UsbConfigDxe:

- Reason: Is Important to get USB working in Windows / Linux.
- Patch: Exit BootServices routine was patched to not deinit USB after exit boot services. Another patch disables recreating IOMMU domains.
- Patch Creator: [Gustave Monce](https://github.com/gus33000)
