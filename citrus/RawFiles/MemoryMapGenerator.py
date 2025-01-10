from argparse import ArgumentParser
from typing import Any

def ParseArgs():
    parser = ArgumentParser()
    parser.add_argument('-i', dest="UefiPlatPath", required=True)
    return parser.parse_args()

class MemoryDescriptor:
    def __init__(self, name, space, base, size, hob_option, resource_attribute, arm_attribute, resource_type, cache_type):
        self.name = str(name)
        self.space = str(space)
        self.base = int(base, 16)
        self.size = int(size, 16)
        self.hob_option = str(hob_option)
        self.resource_attribute = str(resource_attribute)
        self.arm_attribute = str(arm_attribute)
        self.resource_type = str(resource_type)
        self.cache_type = str(cache_type)
    
    def toMessage(self):
        return "{{{},{}0x{:08X}, 0x{:08X}, {}, {}, {}, {}, {}}},".format(self.name, self.space, self.base, self.size, self.hob_option, self.resource_attribute, self.arm_attribute, self.resource_type, self.cache_type)
        
def ParseLineToMemoryDescriptor(line):
    if line[-1] == "\n":
        line = line[0:-1]
    base, size, name, hob, resource_attribute, arm_attribute, resource_type, cache_type = line.split(',')
    while name[0] == " ":
        name = name[1:]
    while resource_attribute[0] == " ":
        resource_attribute = resource_attribute[1:]
    while arm_attribute[0] == " ":
        arm_attribute = arm_attribute[1:]
    while resource_type[0] == " ":
        resource_type = resource_type[1:]
    while cache_type[0] == " ":
        cache_type = cache_type[1:]
    

    space_count = hob.count(' ')
    hob = hob[(space_count):]

    return MemoryDescriptor(name, ' ' * space_count, base, size, hob, resource_attribute, arm_attribute, resource_type, cache_type)

def GapChecker(inDescriptors):
    result = inDescriptors.copy()
    descriptors = inDescriptors.copy()

    last_desc = descriptors[0]
    descriptors.pop(0)
    for desc in descriptors:
        if last_desc.base + last_desc.size < desc.base:
            ram_region = MemoryDescriptor("\"RAM Partition\"", "     ", "0x0", "0x0", "AddMem", "SYS_MEM", "SYS_MEM_CAP", "Conv", "WRITE_BACK_XN")
            ram_region.base = last_desc.base + last_desc.size
            ram_region.size = desc.base - (last_desc.base + last_desc.size)
            if ram_region.size:
                result.append(ram_region)
        last_desc = desc
    
    result.sort(key=lambda r: r.base)
    return result
    
def ParseLineToConfig(line):
    if line[-1] == "\n":
        line = line[0:-1]
    name, value = line.split(' = ')
    while name[-1] == " ":
        name = name[:-1]
    while value[-1] == " ":
        value = value[:-1]
    if value[0] == '\"' or name == "ConfigParameterCount":
        return ''
    msg = "{{\"{}\", {}}},\n".format(name, value)
    return msg

def Main(UefiPlatPath):
    file = open(UefiPlatPath, "r", encoding="utf-8")
    this_line = None

    # Find [MemoryMap]
    while this_line != "[MemoryMap]\n":
        this_line = file.readline()
        if this_line == '':
            print("Invalid UefiPlat.cfg")
            break
        if this_line[0] == "#":
            continue

    # Parse [MemoryMap]
    regions = []
    while True:
        this_line = file.readline()
        if this_line == '' or this_line[0] == '[':
            break
        if this_line[0] == '\n' or this_line[0] == '#' and this_line[0:2] != '#-':
            continue
        if this_line[0:2] == "#-":
            this_line = this_line.replace("-", "")[1:-1]
            while this_line[-1] == " " or this_line[-1] == "\n":
                this_line = this_line[:-1]
            this_line = "//" + this_line + " Regions"
            print(this_line)
            continue
        regions.append(ParseLineToMemoryDescriptor(this_line))

    # Sort regions by base
    regions.sort(key=lambda r: r.base)

    regions = GapChecker(regions)

    for region in regions:
        print(region.toMessage())

    # Find [RegisterMap]
    while this_line != "[RegisterMap]\n":
        this_line = file.readline()
        if this_line == '':
            print("Invalid UefiPlat.cfg")
            break
        if this_line[0] == "#":
            continue

    # Parse [RegisterMap]
    while True:
        this_line = file.readline()
        if this_line == '' or this_line[0] == '[':
            break
        if this_line[0] == '\n' or this_line[0] == '#' and this_line[0:2] != '#-':
            continue
        if this_line[0:2] == "#-":
            this_line = this_line.replace("-", "")[1:-1]
            while this_line[-1] == " " or this_line[-1] == "\n":
                this_line = this_line[:-1]
            this_line = "\n//" + this_line + " Regions"
            print(this_line)
            continue
        print(ParseLineToMemoryDescriptor(this_line).toMessage())

    print("\n// Configuration Map")

    # Find [ConfigParameters]
    while this_line != "[ConfigParameters]\n":
        this_line = file.readline()
        if this_line == '':
            print("Invalid UefiPlat.cfg")
            break
        if this_line[0] == "#":
            continue
    
    # Parse [ConfigParameters]
    while True:
        this_line = file.readline()
        if this_line == '' or this_line[0] == '[':
            break
        if this_line[0] == '\n' or this_line[0] == '#' and this_line[0:2] != '#-':
            continue
        print(ParseLineToConfig(this_line), end='')

    print("\nDynamic RAM Start Address: 0x{:08X}".format(regions[-1].base + regions[-1].size))

    file.close()

if __name__ == '__main__':
    Main(**vars(ParseArgs()))