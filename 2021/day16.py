from functools import reduce


def hex_2_bin(hex_str):
    bin_str = ''
    for char in hex_str:
        bin_str += bin(int(char, 16))[2:].zfill(4)
    return bin_str

def decode_literal(subpacket):
    bin_str = ''
    while subpacket[0] == '1':
        bin_str += subpacket[1:5]
        subpacket = subpacket[5:]
    bin_str += subpacket[1:5]
    subpacket = subpacket[5:]
    return int(bin_str, 2), subpacket

def decode_packet(packet):
    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)
    packet = packet[6:]
    count = version
    subpackets = []
    if type_id == 4:
        value, packet = decode_literal(packet)
        subpackets.append(value)
    else:
        len_type = packet[0]
        packet = packet[1:]
        if len_type == '0':
            length = int(packet[:15], 2)
            packet = packet[15:]
            subpacket = packet[:length]
            packet = packet[length:]
            while subpacket:
                version, subpacket, value = decode_packet(subpacket)
                count += version
                subpackets.append(value)
        else:
            length = int(packet[:11], 2)
            packet = packet[11:]
            for i in range(length):
                version, packet, value = decode_packet(packet)
                count += version
                subpackets.append(value)

        if type_id == 0:
            value = sum(subpackets)
        elif type_id == 1:
            value = reduce((lambda x, y: x * y), subpackets)
        elif type_id == 2:
            value =  min(subpackets)
        elif type_id == 3:
            value =  max(subpackets)
        elif type_id == 5:
            value = subpackets[0] > subpackets[1]
        elif type_id == 6:
            value = subpackets[0] < subpackets[1]
        elif type_id == 7:
            value = subpackets[0] == subpackets[1]
    return count, packet, value


with open('inputs/input_day16.txt') as f:
    lines = f.read()

packet = hex_2_bin(lines)
# print(packet)
count, _, value = decode_packet(packet)
print('Part one: ', count)
print('Part two: ', value)
