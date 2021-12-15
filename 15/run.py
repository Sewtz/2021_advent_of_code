import queue
import numpy as np

from graph import Graph

file = "example.txt"

def main():
    map = read_file(file)

    # part 1
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
    

    # part 2
    map = expand_map(map, 5)
    print(expand_map(np.ones((2,2)), 5))

def expand_map(map, times):
    new_map = map.copy()
    for t in range(times):
        new_tile = map + np.ones_like(map) * t
        new_map  = np.concatenate((new_map, new_tile), axis=0)

    inter_map = new_map.copy()
    for t in range(times):
        new_tile = inter_map + np.ones_like(inter_map) * t
        new_map  = np.concatenate((new_map, new_tile), axis=1)

    return new_map

def read_file(file):
    map = []
    with open(file, "r") as fp:
        for line in fp.readlines():
            map.append([int(x) for x in line if x != "\n"])
    return np.array(map)

if __name__ == "__main__":
    main()