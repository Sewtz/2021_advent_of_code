import numpy as np

version_sum = 0

def main():
    global version_sum
    input  = read_file("input.txt")
    packet = hex2bin(input)

    # iterate over every packet
    for packet in [hex2bin(input)]:
        res, _ = parse_packet(packet)
        print(res)
    
    #print(version_sum)

def read_file(file):
    with open(file, "r") as fp:
        return fp.readline()

def parse_packet(packet):
    global version_sum
    v,t,_,_ = split_packet(packet)

    # add to version sum
    version_sum += v
    if t == 4:
        result, read_bits = parse_literal_value(packet)        
    else:
        result, read_bits = parse_operator(packet)

    return result, read_bits

def parse_literal_value(packet):
    _,_,_,payload = split_packet(packet)
    number = ""
    # convert payload to number
    read_bits = 6
    for item in chunks(payload, 5):
        number += item[1:]
        read_bits += len(item)
        if item[0] == "0":
            break

    return int(number, 2), read_bits

def parse_operator(packet):
    _,type,length, payload = split_packet(packet)

    results      = []
    read_bits    = 0
    read_packets = 0
    max_bits     = 0
    max_packets  = 0

    # read length field
    if length == '0':
        length_bits = 15
        max_bits    = int(payload[:length_bits],2)
        sub_payload = payload[length_bits:length_bits+max_bits]
    else:
        length_bits = 11
        max_packets = int(payload[:length_bits],2)
        sub_payload = payload[length_bits:]

    # loop while not end condition reached
    while (length == '0' and read_bits < max_bits) or (length == '1' and read_packets < max_packets):
        subpacket_result, subpacket_read_bits = parse_packet(sub_payload[read_bits:])
        
        # append result
        results.append(subpacket_result)

        # add read bits
        read_bits    += subpacket_read_bits

        # increase packet counter
        read_packets += 1

    # calc operator
    result =0
    if type == 0:
        result = sum(results)
    elif type == 1:
        result = np.prod(results)
    elif type == 2:
        result = min(results)
    elif type == 3:
        result = max(results)
    elif type == 5:
        if results[0] > results[1]:
            result = 1
        else:
            result = 0
    elif type == 6:
        if results[0] < results[1]:
            result = 1
        else:
            result = 0
    elif type == 7:
        if results[0] == results[1]:
            result = 1
        else:
            result = 0

    # update bits and return
    total_bits = 7 + length_bits + read_bits
    return result, total_bits

def split_packet(packet):
    version = get_packet_version(packet)
    type    = get_packet_type(packet)
    if type == 4:
        length  = None
        payload = packet[6:]
    else:
        length  = packet[6]
        payload = packet[7:]
    return version, type, length, payload

def get_packet_version(packet):
    return int(packet[0:3], 2)

def get_packet_type(packet):
    return int(packet[3:6], 2)

def hex2bin(hex):
    mapping = {
        '0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111'
    }

    # convert char-by-char
    bin = ""
    for c in hex:
        bin += mapping[c]
    return bin

def chunks(lst, n):
    chks = []
    for i in range(0, len(lst), n):
        chks.append(lst[i:i + n])
    return chks

if __name__ == "__main__":
    main()