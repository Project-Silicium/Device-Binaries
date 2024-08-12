# Patches/Fixes

## CardhuBds:

- Reason: To Enable New Button Combo Options.
- Patch: Boot Option Key Codes were Set to the Correct Value.
- Patch Creator: [Robotix](https://github.com/Robotix22)

# UEFI Applications

> [!NOTE]
> Most of these Apps **need** to be Executed from EBL.

## BoardInfo:

This App Shows you some Infos about the Main Board in your Device.

## BootOrder:

This App Shows the Boot Orders and Can Modify them.

## debug:

It does nothing when Executed so `¯\_(ツ)_/¯`.

## DeviceInfo:

Prints Device Specific Infos like Serial Number, Model, etc.

## ECTool:

> [!WARNING]
> Flashing Incorect EC Firmware can Damage your Device. <br>
> The Device will not Charge anymore or Power On.

This App Can Dump the current EC Firmware or Can Write a New EC Firmware from a File to the EC Chip.

## EmmcTest:

> [!CAUTION]
> This App will Wipe your eMMC USER Section. <br>
> Which means you will **LOSSE ALL YOUR DATA!**

It Tests the Emmc Performance and someother Things.

## FlashEfi:

> [!WARNING]
> Flashing Wrong UEFI Firmware can break your Device! <br>
> Only Recoverable thru APX Boot.

Can Dump UEFI Firmware or Write UEFI Firmware to the SPI Chip.

## Gpio:

This App Can Read or Set the Level of defined GPIO.

## HMACTest:

I couldn't Test this Sadly.

## I2cScan:

Scans for I2C Devices on the current Device and prints the Resoults.

## IDBoard;

> [!CAUTION]
> Changing the ID to something Invalid will Break UEFI Boot! <br>
> Only Recoverable thru APX Boot.

Can Change the ID of the Main Board.

## IDNS:

Can Change the ID of the Serial Number? Not Really sure here.

## InitEmmc:

> [!CAUTION]
> This App will Wipe your eMMC USER Section. <br>
> Which means you will **LOSSE ALL YOUR DATA!**

This App will Init the eMMC, I have no Idea why it Exists.

## LabDeployTest:

This App is just a Simpler Version to Test Things like Memory or eMMC using the other Apps.

## MemTest:

It Tests the Memory.

## NvACPIView:

The Nvidia Version of `AcpiView` from UEFI Shell wich Reads/Dumps the ACPI Tables.

## NvI2CRW:

This App Can Read from I2C Registers or Write to them.

## NvSecureToggle:

> [!NOTE]
> This dosen't seem to do anything on Retail Models. <br>
> Also Only Works when Executed within BDS Phase.

It Toggles the Current Secure Mode of the Device.

## NvSmbiosView:

This is the Nvida Version of `SmbiosView` from UEFI Shell wich Reads SmBios Entries.

## PerfTest:

It Tests the Performance of some Devices like: Memory, eMMC, etc.

## PlatformTest:

This is probally a Simpler Version of Tests wich uses other Test Apps, I couldn't Test this one.

## Pmu:

This App does the same as `NvI2CRW` but wich Simpler Parameters.

## RngTest:

It Tests the RNG Driver.

## SecureBootSetting:

> [!NOTE]
> This App can't Change Secure Boot Settings when not Executed wihin the BDS Phase. <br>
> Debug Policy might Break Windows Boot, So be carefull.

This is a Scraped UEFI Menu wich has Settings for Secure Boot, RPMB, etc.

## SecureVar:

Displays UEFI Variables and can Modify them.

## TimeStampApp:

This App Basicly prints APRIORI.

## TrEEfi:

I also wasn't able to Test this one Sadly.

## UnitTest:

Its basicly just `PlatformTest` under a diffrent Name.

## Variable

Prints all UEFI Variables.

