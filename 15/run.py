import queue
import numpy as np

from graph import Graph

file = "input.txt"

def main():
    map = read_file(file)
    map = expand_map(map, 5)

    graph_list = {}
    for x in range(map.shape[0]):
        for y in range(map.shape[1]):
            graph_list[(x,y)] = []
            for offset in [[-1,0], [1,0], [0,-1], [0,1]]:
                x_n = x + offset[0]
                y_n = y + offset[1]
                if x_n >= 0 and y_n >= 0 and x_n < map.shape[0] and y_n < map.shape[1]:
                    node = [(x_n, y_n), map[x_n,y_n]]
                    graph_list[(x,y)].append(node)

    g = Graph(graph_list)
    path = g.a_star_algorithm((0,0), (map.shape[0]-1, map.shape[1]-1))
    render = np.zeros_like(map)
    score = 0
    for node in path:
        render[node] = map[node]
        score += map[node]

    render[0,0] = 0

    print(sum(sum(render)))

def expand_map(map, times):
    new_map = np.zeros((map.shape[0] * times, map.shape[1] * times))
    tile = map.copy()
    new_map[0:map.shape[0], 0:map.shape[1]] = map
    for r in range(1,times):
        c = 0
        new_tile = new_map[map.shape[0]*(r-1):map.shape[0]*r, 0:map.shape[1]].copy()
        new_tile += np.ones_like(new_tile)
        new_tile[new_tile>9] = 1
        new_map[map.shape[0]*r:map.shape[0]*(r+1), 0:map.shape[1]] = new_tile
    for c in range(1,times):
        r = 0
        new_tile = new_map[0:new_map.shape[0], map.shape[1]*(c-1):map.shape[1]*c].copy()
        new_tile += np.ones_like(new_tile)
        new_tile[new_tile>9] = 1
        new_map[0:new_map.shape[0], map.shape[1]*(c):map.shape[1]*(c+1)] = new_tile


    return new_map

def read_file(file):
    map = []
    with open(file, "r") as fp:
        for line in fp.readlines():
            map.append([int(x) for x in line if x != "\n"])
    return np.array(map)

if __name__ == "__main__":
    main()