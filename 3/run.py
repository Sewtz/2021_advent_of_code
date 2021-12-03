import numpy as np

file = "input.txt"

bits = []
with open(file, "r") as fp:
    # read line by line
    for line in fp.readlines():
        # read char by char
        characters = []
        for i in range(len(line)):
            c = line[i]
            if not c == '\n':
                characters.append(int(c))

        bits.append(characters)

def calc_dominant(arr):
    sum_of_cols = np.array(arr).sum(axis=0)
    return [x >= np.array(arr).shape[0]/2 for x in sum_of_cols]

def calc_submissive(arr):
    sum_of_cols = np.array(arr).sum(axis=0)
    return [x < np.array(arr).shape[0]/2 for x in sum_of_cols]

# part 1
bits = np.array(bits)
is_dominant   = calc_dominant(bits)   # [x >= bits.shape[0]/2 for x in bits.sum(axis=0)]
is_submissive = calc_submissive(bits) # [x < bits.shape[0]/2 for x in bits.sum(axis=0)]

# construct binary
def convert_binary(arr):
    value = 0
    reversed = arr[::-1]
    for i in range(len(reversed)):
        if reversed[i]:
            value += 2**i

    return value

gamma = convert_binary(is_dominant)
epsilon = convert_binary(is_submissive)

print(gamma * epsilon)

# part 2
possible_o2_values = bits
position = 0
while position < bits.shape[0] and len(possible_o2_values) > 1:
    dominant_value = [int(x) for x in calc_dominant(possible_o2_values)]
    possible_o2_values = [x for x in possible_o2_values if x[position] == int(calc_dominant(possible_o2_values)[position])]
    position += 1

possible_co2_values = bits
position = 0
while position < bits.shape[0] and len(possible_co2_values) > 1:
    dominant_value = [int(x) for x in calc_submissive(possible_co2_values)]
    possible_co2_values = [x for x in possible_co2_values if x[position] == int(calc_submissive(possible_co2_values)[position])]
    position += 1

o2 = convert_binary(possible_o2_values[0])
co2 = convert_binary(possible_co2_values[0])
print(o2*co2)