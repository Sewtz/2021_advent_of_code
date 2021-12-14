import numpy as np

file = "input.txt"

def main():
    template, rules = read_file(file)
    
    polymer = template
    for step in range(40):
        polymer = run_pair_insertion_step(polymer, rules)

    counts = count_characters(polymer).values()
    print(sorted(counts)[-1] - sorted(counts)[0])

def count_characters(string):
    counts = {}
    for c in string:
        if c in counts.keys():
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

def run_pair_insertion_step(input, rules):
    output = ""
    for i in range(len(input)-1):
        pair = input[i:i+2]
        output += input[i] + rules[pair]

    output += input[-1]
    return output

def read_file(file):
    template = None
    rules = {}
    with open(file, "r") as fp:
        for line in fp.readlines():
            if len(line) >= 3:
                if "->" in line:
                    # it is a rule
                    rule = line.split("->")[0].strip()
                    res  = line.split("->")[1].strip()
                    rules[rule] = res
                else:
                    # it is the template
                    template = line.strip()
    return template, rules

if __name__ == "__main__":
    main()