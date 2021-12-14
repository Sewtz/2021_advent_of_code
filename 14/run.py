import numpy as np

file  = "input.txt"
steps = 40

def main():
    template, rules = read_file(file)
    
    # convert to polymer
    polymer = {}
    for i in range(len(template)-1):
        pair = template[i:i+2]
        if not pair in polymer.keys(): 
            polymer[pair] = 0
        polymer[pair] += 1

    # run insertion
    for step in range(steps):
        polymer = run_pair_insertion_step(polymer, rules)
        print("{0:d}/{1:d}".format(step+1, steps), end="\r")
    print("")

    # count all elements
    counts = count_elements(polymer)

    # count for last element (missing in calc)
    counts[template[-1]] += 1
    
    # sort and print diff
    counts = [x for x in sorted(counts.values())]
    print(counts[-1] - counts[0])

def polymer2str(polymer):
    str = ""
    for pair, count in polymer.items():
        str += pair * count
    return str

def count_elements(polymer):
    counts = {}
    for pair, pair_count in polymer.items():
        c = pair[0]
        if not c in counts.keys(): 
            counts[c] = 0 # insert 0 count
        counts[c] += pair_count
    return counts

def run_pair_insertion_step(input, rules):
    output = {}
    for cur_pair, count in input.items():
        if cur_pair in rules:
            # direct pair
            direct_pair = cur_pair[0] + rules[cur_pair]
            if not direct_pair in output.keys():
                output[direct_pair] = 0 # insert 0 count
            output[direct_pair] += count

            # consecutive pair
            consec_pair = rules[cur_pair] + cur_pair[1]
            if not consec_pair in output.keys():
                output[consec_pair] = 0 # insert 0 count
            output[consec_pair] += count

        else:
            if not cur_pair in output.keys():
                output[cur_pair] = 0
            output[cur_pair] += count
    return output

    #output = ""
    #for i in range(len(input)-1):
    #    pair = input[i:i+2]
    #    output += input[i] + rules[pair]
    #
    #output += input[-1]
    #return output

def apply(pairs):
    new_pairs = {}
    #print(pairs)
    for k,v in pairs.items():
        #print("KV: ", k,v)
        if k in rules:
            c = rules[k]
            p1 = k[0] + c
            p2 = c + k[1]
            if not p1 in new_pairs: new_pairs[p1] = 0
            new_pairs[p1] += v
            if not p2 in new_pairs: new_pairs[p2] = 0
            new_pairs[p2] += v
        else:
            if not k in new_pairs: new_pairs[k] = 0
            new_pairs[k] += v
    return new_pairs

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