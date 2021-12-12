from os import pardir

file = "input.txt"

def main():
    map = parse_file(file)
    paths = find_paths(map, 1)
    print(len(paths))
    
    paths = find_paths(map, 2)
    print(len(paths))

def find_paths(map, small_caves_visit=1):
    all_paths = [["start"]]
    
    # iterate while not all paths ended
    while not all([True if p[-1] == "end" else False for p in all_paths]):
        new_paths = []
        for path in all_paths:
            # check if open
            if path[-1] != "end":
                # get possible connections
                for connection in map[path[-1]]:
                    # big caves can always be appended
                    if connection[0].isupper(): 
                        new_path = path.copy()
                        new_path.append(connection)
                        if new_path not in new_paths:
                            new_paths.append(new_path)

                    # small caves are only allowed once
                    elif connection not in path:
                        new_path = path.copy()
                        new_path.append(connection)
                        if new_path not in new_paths:
                            new_paths.append(new_path)

                    # 1 cave may be visited twice
                    elif connection not in ["start", "end"] and count_small_caves(path) < small_caves_visit:
                        new_path = path.copy()
                        new_path.append(connection)
                        if new_path not in new_paths:
                            new_paths.append(new_path)

            else:
                # keep this path
                new_paths.append(path)
                            
        all_paths = new_paths.copy()

    return all_paths

def count_small_caves(path):
    caves = [x for x in path if x.islower()]
    times = []
    for cave in caves:
        times.append(caves.count(cave))
    return max(times)

def parse_file(file):
    # read file
    lines = None
    with open(file, "r") as fp:
        lines = fp.readlines()

    # parse lines
    map = {}
    for line in lines:
        A = line.split("-")[0].strip()
        B = line.split("-")[1].strip()

        # add connection
        if A not  in map.keys():
            map[A] = []

        map[A].append(B)

        # add new B if not known
        if not B in map.keys():
            map[B] = [A]

        # add back connection
        else:
            if A not in map[B]:
                map[B].append(A)

    return map



if __name__ == "__main__":
    main()