import math

def main():
    op_a = [[[[4,3],4],4],[7,[[8,4],9]]]
    op_b = [1,1]
    result = [op_a, op_b]
    result = "[[[[[9,8],1],2],3],4]"
    result = reduce_number(result)
    
    print(result)

def reduce_number(number):
    while(True):
        print(number)
        # first explode
        new_number = explode(number)
        if new_number != number:
            number = new_number
            continue

        # then split
        new_number = split(number)
        if new_number != number:
            number = new_number
            continue

        # nothing changed
        return number

def explode(number):
    item, _, _ =  try_explode(number, level=0)
    return item

def try_explode(item, level, number_to_add=None, allow_explode=True):
    # if this number is set, we have to add
    # this number to the first int
    if number_to_add is None:
        number_to_add = 0
    a,b = item
    if level < 4:
        left  = None
        right = None

        # left element
        if type(a) == int:
            a += number_to_add

        else:
            a, left, right = try_explode(a, level+1, number_to_add)

        # right element
        if type(b) == int:
            if not right is None:
                b += right
                right = None

        else:
            b, left, right = try_explode(b, level+1, left)

            if not left is None and type(a) == int:
                a += left
                left = None

        return [a,b], left, right

    else:
        # this item must explode
        a += number_to_add
        return 0, a, b

def split(number):
    if type(number) == int:
        if number >= 10:
            a = math.floor(float(number) / 2.)
            b = math.ceil(float(number) / 2.)
            return [a,b]
        else:
            return number
    else:
        a,b = number
        return [split(a), split(b)]

if __name__ == "__main__":
    main()  