def hex_to_bin(char):
    return bin(int(char, 16))[2:].zfill(4) if char else ''

def version(padding, file):
    while len(padding) < 3:
        padding += hex_to_bin(f.read(1))
    return int(padding[:3], 2), padding[3:]


def type_id(padding, file):
    while len(padding) < 3:
        padding += hex_to_bin(f.read(1))
    return int(padding[:3], 2), padding[3:]

def litteral(padding, file):
    prefix = '1'
    number = str()
    while prefix == '1':
        while len(padding) < 5:
            padding += hex_to_bin(f.read(1))
        prefix, byte, padding = padding[0], padding[1:5], padding[5:]
        number += byte
    return int(number, 2), padding
    
with open('../inputs/AoC2021-16.txt', 'r') as f:
    versions = 0
    read = f.read(1)
    padding = str()
    while read != '' or len(padding) >= 4:
        padding += hex_to_bin(read)
        ver, padding = version(padding, f)
        versions += ver
        t_id, padding = type_id(padding, f)
        if t_id == 4:
            _, padding = litteral(padding, f)
        else:
            if len(padding) < 1:
                padding += hex_to_bin(f.read(1))
            length_t_id, padding = padding[0], padding[1:]
            length = 15 if length_t_id == '0' else 11
            while len(padding) < length:
                padding += hex_to_bin(f.read(1))
            padding = padding[length:]
        read = f.read(1)
        if read == '\n':
            read = ''

print(versions)
