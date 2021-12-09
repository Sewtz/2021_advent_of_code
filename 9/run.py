import numpy as np
from queue import Queue

file = "example.txt"
file = "input.txt"

def main():
    map = read_file(file)
    pts = find_low_points(map)
    print(calc_risk(pts, map))

    basin_values = []
    for pt in pts:
        basin_values.append(len(explore_basin(map, pt)))

    product = 1
    for idx in np.argpartition(basin_values, -3)[-3:]:
        product *= basin_values[idx]
    print(product)

def calc_risk(pts, map):
    return sum([map[x[0],x[1]]+1 for x in pts])

def explore_basin(map, start_pt):
    basin = [start_pt]
    search_list = Queue()
    search_list.put(start_pt)
    while not search_list.empty():
        if search_list.full():
            print("Queue full... should not happen")
            exit(-1)

        current = search_list.get()
        for adjacent in get_adjacent(current, map.shape):
            # only consider if not 9
            if map[adjacent[0], adjacent[1]] != 9:
                # check if not already in basin
                if not adjacent in basin:
                    basin.append(adjacent)
                    search_list.put(adjacent)

    return basin

def find_low_points(map):
    map = np.array(map)
    low_pts = []
    
    # iterate over all elements of map
    for x in range(map.shape[0]):
        for y in range(map.shape[1]):
            # find ajacent points
            adjacent = get_adjacent((x,y), map.shape)

            # test if all adjacents are higher
            if all([map[item[0], item[1]] > map[x,y] for item in adjacent]):
                low_pts.append((x,y))

    return low_pts

def get_adjacent(pt, map_shape):
    x = pt[0]
    y = pt[1]
    adjacent = []
    if x > 0:
        adjacent.append((x-1, y))
    if x < map_shape[0]-1:
        adjacent.append((x+1, y))
    if y > 0:
        adjacent.append((x, y-1))
    if y < map_shape[1]-1:
        adjacent.append((x, y+1))
    return adjacent

def read_file(file):
    map = []
    with open(file, "r") as fp:
        for line in fp.readlines():
            row = []
            for element in line:
                if element != "\n":
                    row.append(int(element))
            map.append(row)
    return np.array(map)

if __name__ == "__main__":
    main()