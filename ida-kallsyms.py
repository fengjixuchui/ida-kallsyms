from idaapi import get_bytes, get_inf_structure
from ida_name import set_name
from ida_segment import get_segm_by_name

from find_kallsyms import find_kallsyms_in_rodata

rodata_segm = get_segm_by_name('.rodata')
rodata_size = rodata_segm.end_ea - rodata_segm.start_ea + 1
rodata = bytearray(get_bytes(rodata_segm.start_ea, rodata_size))
inf = get_inf_structure()
endianness = '>' if inf.is_be() else '<'
for address, name in find_kallsyms_in_rodata(rodata, endianness):
    if name[0] != 'A':
        set_name(address, str(name[1:]))
