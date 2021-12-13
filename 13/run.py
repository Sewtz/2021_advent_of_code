from os import X_OK, read
import numpy as np

file = "example.txt"
file = "input.txt"

def main():
    coords, folds = read_file(file)
    map = parse(coords, folds[0:1])
    print(sum(sum(map)))
    map = parse(coords, folds)
    print_map(map)

def print_map(map):
    for y in range(map.shape[1]):
        for x in range(map.shape[0]):
            if not x%5:
                print(" ", end='')
            if map[x,y] == 1:
                print("#", end='')
            else:
                print(" ", end='')
        print("")


def parse(coords, folds):
    shape = (np.array(coords).max(axis=0)[0]+1, np.array(coords).max(axis=0)[1]+1)
    map = np.zeros(shape, dtype=np.int8)

    # mark all coords
    for x,y in coords:
        map[x,y] = 1

    for fold in folds:
        map = apply_fold(map, fold)

    return map

def apply_fold(map, fold):  
    if fold[0] == 'x':
        part1 = map[:fold[1],:]
        part2 = map[fold[1]+1:,:]
        part2 = np.flip(part2, axis=0)
    else:
        part1 = map[:,:fold[1]]
        part2 = map[:,fold[1]+1:]

        part2 = np.flip(part2, axis=1)

    folded_map = np.bitwise_or(part1, part2)
    return folded_map
            
    

def read_file(file):
    state  = "coords" 
    coords = []
    folds  = []
    with open(file, "r") as fp:
        for line in fp.readlines():
            if len(line.strip()) >= 3:
                if not line.startswith("fold"):
                    # coords
                    coords.append([int(x) for x in line.split(",") if x != "\n"])
                else:
                    # folding
                    axis  = line.split(" ")[-1].split("=")[0]
                    value = int(line.split(" ")[-1].split("=")[1])
                    folds.append((axis, value))

    return coords, folds

if __name__ == "__main__":
    main()