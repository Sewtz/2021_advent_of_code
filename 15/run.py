import queue
import numpy as np

file = "example.txt"

class Node():
    def __init__(self, position, score, heuristic, parent):
        self.position = position
        self.score = score
        self.heuristic = heuristic
        self.total = score + heuristic
        self.parent = parent

    def __repr__(self):
        return str(self.position) + ": S=" + str(self.score) + " H=" + str(self.heuristic)

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __eq__(self, other):
        return self.position == other.position

def main():
    map  = read_file(file)
    shape = np.array(map).shape
    score, path = astar(map, start=(0,0), end=(shape[0]-1, shape[1]-1))
    print(score)
    
    for node in path:
        print(map[node.position], node)

def astar(map, start, end):
    open_list  = queue.PriorityQueue()
    path_nodes = {}

    open_list.put((0,Node(position=start, score=map[start], parent=None, heuristic=heuristic(end,start))))
    while not open_list.empty():
        # pop next element
        current_node = open_list.get()[1]
        path_nodes[current_node.position] = current_node

        # check if element is end node
        if current_node.position == end:
            path = [current_node]
            next = current_node.parent
            while not next is None:
                path.append(path_nodes[next])
                next = path_nodes[next].parent

            return current_node.score, path[::-1]

        # get neighbors
        for offset in [[-1,0],[1,0],[0,-1],[0,1]]:
            x_n = current_node.position[0] + offset[0]
            y_n = current_node.position[1] + offset[1]

            # check coords are valid
            if x_n >= 0 and x_n < map.shape[0] and y_n >= 0 and y_n < map.shape[1]:
                # check that coord is not already used
                if (x_n, y_n) in path_nodes.keys():
                    continue

                # calc score as this score + next score
                next_score = map[x_n,y_n] + current_node.score
                next_node  = Node(position=(x_n, y_n), score=next_score, parent=current_node.position, heuristic=heuristic((x_n, y_n), end))

                # add to open list and sort by distance
                open_list.put((next_node.score, next_node))
        

def heuristic(pt1, pt2):
    # Manhattan distance (L1)
    return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])

def read_file(file):
    map = []
    with open(file, "r") as fp:
        for line in fp.readlines():
            map.append([int(x) for x in line if x != "\n"])
    return np.array(map)

if __name__ == "__main__":
    main()