import numpy as np

file = "input.txt"

def main():
    # read file
    coords = read_file(file)

    # find size of map
    map_size   = get_map_size(coords)
    empty_map  = np.zeros((map_size[1][0] + 1, map_size[1][1] + 1))

    # fill in all lines
    complete_map = empty_map
    for l1, l2 in coords:
        complete_map = put_line(complete_map, l1, l2, diagonal=True)

    # count all values greater or equal than 2
    ge_2 = (np.asarray(complete_map) >= 2).sum()
    print(ge_2)

def put_line(map, l1, l2, diagonal=False):
    min_x = min(l1[0], l2[0])
    max_x = max(l1[0], l2[0])
    min_y = min(l1[1], l2[1])
    max_y = max(l1[1], l2[1])
    
    # vertical
    if l1[0] == l2[0]:
        map[l1[0], min_y:max_y+1] += 1
        return map

    # horizontal
    if l1[1] == l2[1]:
        map[min_x:max_x+1, l1[1]] += 1
        return map

    if diagonal:
        # test for diagonal
        if abs(l1[0] - l2[0]) == abs(l1[1] - l2[1]):
            step_x = 1
            if l1[0] > l2[0]:
                step_x = -1

            step_y = 1
            if l1[1] > l2[1]:
                step_y = -1
            
            current_pt = l1
            while(not current_pt == l2):
                map[current_pt] += 1
                current_pt = (current_pt[0] + step_x, current_pt[1] + step_y)

            map[current_pt] += 1
            return map

    return map

def get_map_size(coords):
    min_x = None
    min_y = None
    max_x = None
    max_y = None
    for l1, l2 in coords:
        if min_x is None or min(l1[0], l2[0]) < min_x: 
            min_x = min(l1[0], l2[0])

        if min_y is None or min(l1[1], l2[1]) < min_y: 
            min_y = min(l1[1], l2[1])

        if max_x is None or max(l1[0], l2[0]) > max_x: 
            max_x = max(l1[0], l2[0])

        if max_y is None or max(l1[1], l2[1]) > max_y: 
            max_y = max(l1[1], l2[1])

    return ((min_x, min_y), (max_x, max_y))

def read_file(file_name):
    coords = []
    with open(file_name, "r") as fp:
        for line in fp.readlines():
            start, _, end = line.split(" ")
            x1, y1 = start.split(",")
            x2, y2 = end.split(",")

            coords.append(((int(x1), int(y1)),(int(x2), int(y2))))

    return coords

if __name__ == "__main__":
    main()