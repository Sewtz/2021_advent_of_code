from queue import LifoQueue
from statistics import median

file = "example.txt"
file = "input.txt"

def main():
    # read files
    lines = read_file(file)
    #lines = ["<{([{{}}[<[[[<>{}]]]>[]]"]

    pts = []
    correct = []
    for line in lines:
        result = check_syntax(line)
        if not result is None:
            pts.append(calc_points(result))
        else:
            correct.append(line)

    print(sum(pts))

    scores = []
    for line in correct:
        result = check_syntax(line, return_missing=True)
        print(result)
        score = 0
        if not result is None:
            for missing in result:
                score *= 5
                score += calc_points_2(missing)
            scores.append(score)

    print(scores)
    print(median(scores))
            
def calc_points_2(result):
    if result == '(':
        return 1
    if result == '[':
        return 2
    if result == '{':
        return 3
    if result == '<':
        return 4
        
def calc_points(result):
    if result == ')':
        return 3
    if result == ']':
        return 57
    if result == '}':
        return 1197
    if result == '>':
        return 25137

def check_syntax(line, return_missing=False):
    stack = LifoQueue()
    last_opening = None
    for char in line:
        # check for opening 
        if char in ['(', '[', '<', '{']:
            stack.put(char)

        # closing
        else:
            last_opening = stack.get()
            if char == ')' and last_opening != '(':
                if not return_missing:
                    return char

            elif char == ']' and last_opening != '[':
                if not return_missing:
                    return char

            elif char == '}' and last_opening != '{':
                if not return_missing:
                    return char

            elif char == '>' and last_opening != '<':
                if not return_missing:
                    return char
                    

    if return_missing:
        list_of_missing = [last_opening]
        while not stack.empty():
            list_of_missing.append(stack.get())
        return list_of_missing
    else:
        return None

def read_file(file):
    lines = None
    with open(file, "r") as fp:
        lines = fp.readlines()
    return lines

if __name__ == "__main__":
    main()