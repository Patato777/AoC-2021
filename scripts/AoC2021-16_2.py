from functools import reduce


PACKET_TYPE = {0: sum, 1: lambda l: reduce(lambda i, j: i * j, l), 2: min, 3: max, 5: lambda l: l[0] > l[1], 6: lambda l: l[0] < l[1], 7: lambda l: l[0] == l[1]}


def hex_to_bin(char):
    return bin(int(char, 16))[2:].zfill(4) if char else ''


def packet(binary):
    version, binary = int(binary[:3], 2), binary[3:]
    type_id, binary = int(binary[:3], 2), binary[3:]
    if type_id == 4:
        litteral = str()
        prefix = '1'
        while prefix == '1':
            prefix, byte, binary = binary[0], binary[1:5], binary[5:]
            litteral += byte
        return int(litteral, 2), binary
    else:
        length_type_id, binary = binary[0], binary[1:]
        sub_packets = list()
        if length_type_id == '0':
            length, binary = int(binary[:15], 2), binary[15:]
            sub_binary, binary = binary[:length], binary[length:]
            while sub_binary != str():
                new_packet, sub_binary = packet(sub_binary)
                sub_packets.append(new_packet)
        else:
            number_of_packets, binary = int(binary[:11], 2), binary[11:]
            while len(sub_packets) < number_of_packets:
                new_packet, binary = packet(binary)
                sub_packets.append(new_packet)
        return PACKET_TYPE[type_id](sub_packets), binary


with open('../inputs/AoC2021-16.txt', 'r') as f:
    binary = ''.join([hex_to_bin(c) for c in f.read().strip()])


print(packet(binary))
