file = "input.txt"

cmds = []

with open(file, "r") as fp:
    for line in fp.readlines():
        cmd, step = line.split(" ")
        cmds.append((cmd, int(step)))

# part 1

horizontal = 0
depth      = 0

for cmd, step in cmds:
    if cmd.strip() == "forward":
        horizontal += step

    elif cmd.strip() == "down":
        depth += step

    elif cmd.strip() == "up":
        depth -= step

    else:
        print("Unknown: " + cmd)


print(horizontal)
print(depth)
print(horizontal * depth)

# part 2

horizontal = 0
depth      = 0
aim        = 0

for cmd, step in cmds:
    if cmd.strip() == "forward":
        horizontal += step
        depth      += aim * step

    elif cmd.strip() == "down":
        aim += step

    elif cmd.strip() == "up":
        aim -= step

    else:
        print("Unknown: " + cmd)

print(horizontal)
print(depth)
print(aim)
print(horizontal * depth)