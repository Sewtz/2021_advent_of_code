import numpy as np

file = "input.txt"
steps = 100000

def main():
    data = read_file(file)
    total_flashes = 0
    for step in range(steps):
        data, flashes = model_energy(data)
        total_flashes += flashes

        if not np.any(data):
            print("Sync at " + str(step+1))

            # who does not like shitty breaks xD
            break

    print(total_flashes)

def model_energy(data):
    # increase by 1
    data += 1
    flashes = 0

    flash_index = np.ones_like(data)
    stop = False
    while not stop:
        new_flash_found = False
        for x in range(data.shape[0]):
            for y in range(data.shape[1]):
                if data[x,y] > 9:
                    # check if already flashed 
                    if flash_index[x,y] != 0:
                        # mark as flashed
                        flash_index[x,y] = 0
                        flashes += 1

                        # increase adjacents
                        for j,k in get_adjacent((x,y), data.shape):
                            data[j,k] += 1

                        # mark loop as found
                        new_flash_found = True

        # if we reach this and no new flash was found
        # we converged
        if not new_flash_found:
            stop = True
            
    # reset all flashed data
    data = data * flash_index
    return data, flashes

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
    if x > 0 and y > 0:
        adjacent.append((x-1, y-1))
    if x > 0 and y < map_shape[1]-1:
        adjacent.append((x-1,y+1))
    if x < map_shape[0]-1 and y < map_shape[1]-1:
        adjacent.append((x+1,y+1))
    if x < map_shape[0]-1 and y > 0:
        adjacent.append((x+1, y-1))
    return adjacent

def read_file(file):
    lines = []
    with open(file, "r") as fp:
        for line in fp.readlines():
            row = [int(x) for x in line if x != "\n"]
            lines.append(row)

    return np.array(lines)

if __name__ == "__main__":
    main()