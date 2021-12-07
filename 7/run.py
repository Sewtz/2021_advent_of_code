file = "example.txt"
#file = "input.txt"

# read file
crab_positions = []
with open(file, "r") as fp:
    line = fp.readline()
    crab_positions = [int(str(x)) for x in line.split(",")]

def find_minimum(dict):
    min_value = None
    for value in dict.values():
        if min_value is None or value < min_value:
            min_value = value
    return min_value

def calc_fuel(crab_positions, cost_function):
    fuel_per_position = {}
    for i in range(len(crab_positions)):
        # calc fuel
        fuel_for_position = 0
        for n in range(len(crab_positions)):
            step_fuel = cost_function(crab_positions[i], i)
            fuel_for_position += step_fuel

        # add fuel to dict
        fuel_per_position[i] = fuel_for_position

    return find_minimum(fuel_per_position)

# part 1
def lin_fuel_cost(A,B):
    return abs(A-B)

fuel1 = calc_fuel(crab_positions, lin_fuel_cost)
print(fuel1)

# part 2
def progressive_fuel_cost(A, B):
    fuel = 0
    for i in range(abs(A-B)):
        fuel += i+1
    return fuel

fuel2 = calc_fuel(crab_positions, progressive_fuel_cost)
print(fuel2)