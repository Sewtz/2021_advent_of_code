import math

def main():
    number = ""
    for line in read_file("example.txt"):
        line = line.replace("\n", "")

        if number == "":
            number = reduce_number(line)
        else:
            number = "[" + number + "," + reduce_number(line) + "]"
    
    print(number)
    print(reduce_number(number))

def read_file(file):
    with open(file, "r") as fp:
        return fp.readlines()

def reduce_number(number):
    while(True):
        # first explode
        new_number = explode(number)
        if new_number != number:
            print("e")
            print(number)
            print(new_number)
            print("++")
            number = new_number
            continue

        # then split
        new_number = split(number)
        if new_number != number:
            print("s")
            print(number)
            print(new_number)
            print("++")
            number = new_number
            continue

        # nothing changed
        return number

def explode(number):
    # remove artifacts
    number = number.replace("[0]", "0")

    new_number = ""
    last_num   = None
    last_c_num = False
    level      = 0
    for i in range(len(number)):
        c = number[i]
        
        # check '[]' chars
        if c == "[":
            level += 1
            continue
        elif c == "]":
            level -= 1
            continue
        
        # check for pairs
        if level <= 4:
            if c.isnumeric():
                if not last_c_num:
                    last_num = i
                last_c_num = True
            else:
                last_c_num = False
        else:
            # extract [a,b]
            separator_idx = number.find(",", i)
            closing_idx   = separator_idx

            # find corresponding closing bracket
            levels_of_brackets = 0
            for n in range(separator_idx, len(number)):
                if number[n] == "[":
                    levels_of_brackets += 1
                elif number[n] == "]":
                    closing_idx = n+1
                    levels_of_brackets -=1

                    if levels_of_brackets == 0:
                        break

            a = number[i:separator_idx]
            b = number[separator_idx+1:closing_idx]
            print(separator_idx, closing_idx)
            print("--",a,b)

            # add to left
            if not last_num is None:
                # find span of last number
                left_num = ""
                for n in range(len(number) - last_num):
                    if number[last_num + n].isnumeric():
                        left_num += number[last_num + n]
                    else:
                        break
                left_span = len(left_num)
                
                
                result     = str(int(a) + int(left_num))
                new_number = number[:last_num] + result + number[last_num+left_span:i-1] + "0"
            else:
                new_number = number[:i-1] + "0"

            # find right number
            next_num = None
            for n in range(closing_idx, len(number)):
                if number[n].isnumeric():
                    next_num = n
                    break

            # replace right number
            if not next_num is None:
                right_num = ""
                for n in range(next_num, len(number)):
                    if number[n].isnumeric():
                        right_num += number[n]
                    else:
                        break
                right_span = len(right_num) 

                result = str(int(b) + int(right_num))
                new_number += number[closing_idx+1:next_num] + result + number[next_num+right_span:]
            else:
                new_number += number[closing_idx+1:next_num]

            return new_number

    return number

def split(number):
    new_number = ""
    penalty    = 0
    for i in range(len(number)):
        # check for penalty and decrease it
        if penalty > 0:
            penalty -= 1
            continue

        c = number[i]
        if c.isnumeric():
            # check if number is greater than 10
            num = ""

            # get span of number
            for n in range(i, len(number)):
                if number[n].isnumeric():
                    num += number[n]
                else:
                    break

            num_span = len(num)

            # if smaller, than just continue
            if int(num) < 10:
                new_number += c
                continue

            # now split
            value  = int(num)
            print(value)
            a      = str(math.floor(value/2.))
            b      = str(math.ceil(value/2.))
            result = "[" + a + "," + b + "]"

            # add penalty
            penalty = num_span-1

            # append result
            new_number += result

        else:
            new_number += c
    return new_number

if __name__ == "__main__":
    main()  