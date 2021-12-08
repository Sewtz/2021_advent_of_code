#file = "one_line.txt"
#file = "example.txt"
file = "input.txt"

numbers = {
    0 : "abcefg",
    1 : "cf",
    2 : "acdeg",
    3 : "acdfg",
    4 : "bcdf",
    5 : "abdfg",
    6 : "abdefg",
    7 : "acf",
    8 : "abcdefg",
    9 : "abcdfg"
}

def main():
    data = read_data(file)
    print(count_unique_output_digits(data))

    total_number = 0
    for line in data:
        total_number += decode_digits(line)

    print(total_number)

def read_data(file):
    with open(file, "r") as fp:
        data =[]
        for line in fp.readlines():
            input  = [x.strip() for x in line.split("|")[0].strip().split(" ")]
            output = [x.strip() for x in line.split("|")[1].strip().split(" ")]
            data.append({"input":input, "output":output})

    return data

def decode_digits(data_line):
    # create mapping dict 
    segment_mapping = {
        'a':None,
        'b':None,
        'c':None,
        'd':None,
        'e':None,
        'f':None,
        'g':None
    }

    signal_count = count_signals(data_line["input"])
    for signal in signal_count.keys():
        count = signal_count[signal]

        # find e (count == 4)
        if count == 4:
            segment_mapping['e'] = signal

        # find b (count == 6)
        if count == 6:
            segment_mapping['b'] = signal

        
        # find f (count == 9)
        if count == 9:
            segment_mapping['f'] = signal

    for item in data_line["input"]:
        # c is in 1 (len==2) and is not f
        if len(item) == 2:
            a, b = item
            if a == segment_mapping['f']:
                segment_mapping['c'] = b
            else:
                segment_mapping['c'] = a

    for item in data_line["input"]:
        # a is in 7 (len==3) and is not c,f
        if len(item) == 3:
            a,b,c = item
            if a != segment_mapping['c'] and a != segment_mapping['f']:
                segment_mapping['a'] = a
            elif b != segment_mapping['c'] and b != segment_mapping['f']:
                segment_mapping['a'] = b
            else:
                segment_mapping['a'] = c

    # d is only twice in 0 (len=6), 6 (len==6) and 9 (len=6) and is not e,c
    len_6_items = [x for x in data_line["input"] if len(x) == 6]
    for signal in count_signals(len_6_items).keys():
        count =  count_signals(len_6_items)[signal]
        if count == 2:
            if signal != segment_mapping['e'] and signal != segment_mapping['c']:
                segment_mapping['d'] = signal

    # the last missing signal is g
    for signal in segment_mapping.keys():
        if not signal in segment_mapping.values():
            segment_mapping['g'] = signal

    # decode
    #decoded_input  = [decode(x, segment_mapping) for x in data_line["input"]]
    decoded_output = [decode(x, segment_mapping) for x in data_line["output"]]
    
    output_digits = []
    for i in range(len(decoded_output)):
        for n in numbers.keys():
            pattern = numbers[n]
            if decoded_output[i] == pattern:
                output_digits.append(n)
                break
        if len(output_digits) != i+1:
            print("could not decode " + decoded_output[i] + " <- " + data_line["output"][i])
            print(segment_mapping)

    # calc complete number
    out_number = 1000 * output_digits[0] + 100 * output_digits[1] + 10 * output_digits[2] + output_digits[3]
    return out_number
    
def decode(item, mapping):
    decoded_item = ""
    for c in item:
        for real_signal in mapping.keys():
            if c == mapping[real_signal]:
                decoded_item += real_signal

    return "".join(sorted(decoded_item))

def count_signals(input):
    signals = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0
    }

    for item in input:
        for signal in item:
            signals[signal] += 1

    return signals

def count_unique_output_digits(data):
    unique_digits = {2:0, 3:0, 4:0, 7:0}
    for item in data:
        for digit in item["output"]:
            if len(digit) in unique_digits.keys():
                unique_digits[len(digit)] += 1

    return sum(unique_digits.values())

if __name__ == "__main__":
    main()