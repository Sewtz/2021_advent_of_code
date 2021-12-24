file = "input.txt"

def main():
    # read instructions
    instructions = read_file(file)

    # execute states
    state = {}
    i     = 0
    for instruction in instructions:
        i += 1
        print("{0:}/{1:}".format(i, len(instructions)), end="\r")
        state = switch_on_off(instruction, state)

    # count "on" states
    print("")
    print("Counting...")
    on_states = 0
    for x in range(-50, 51):
        for y in range(-50, 51):
            for z in range(-50, 51):
                coord = (x,y,z)
                if coord in state:
                    if "on" in state[coord]:
                        on_states += 1

    print(on_states)

def switch_on_off(instruction, state):
    cmd, x_range, y_range, z_range = instruction
    for x in range(max([x_range[0], -50]), min([x_range[1], 50])+1):
        for y in range(max([y_range[0], -50]), min([y_range[1], 50])+1):
            for z in range(max([z_range[0], -50]), min([z_range[1], 50])+1):
                coord = (x,y,z)
                state[coord] = cmd
    return state
    
def read_file(file):
    lines = []
    with open(file, "r") as fp:
        for line in fp.readlines():
            cmd, ranges = line.replace("\n","").split(" ")
            x_part, y_part, z_part = ranges.strip().split(",")
            x_range = (int(x_part.split("=")[1].split("..")[0]), int(x_part.split("=")[1].split("..")[1]))
            y_range = (int(y_part.split("=")[1].split("..")[0]), int(y_part.split("=")[1].split("..")[1]))
            z_range = (int(z_part.split("=")[1].split("..")[0]), int(z_part.split("=")[1].split("..")[1]))
            lines.append((cmd, x_range, y_range, z_range))
    return lines

if __name__ == "__main__":
    main()