from queue import Queue
from collections import Counter
from itertools import permutations

file = "input.txt"

def main():
    # parse input 
    instructions = parse_file(file)

    # model
    highest_model = "0"
    digits = [str(i) for i in range(1,10)]
    digits = digits + digits
    models = sorted(permutations(digits, 14))[::-1]
    print(len(models))

    for model in models:
        #model = "{0:014d}".format(i)
        #if i%1000 == 0:
        #    print(model, end="\r")
        
        # zero is not allowed
        #if "0" in model:
        #    continue
        
        # check if all any number appears more than n times
        #max_count = 0
        #n = 3
        #c = Counter(model)
        #for item in c.values():
        #    if item >= max_count:
        #        max_count = item

        #if max_count >= n:
        #    continue

        if check_model(model, instructions):
            highest_model = model
            break
    
    # print ALU state
    print(model)

def check_model(model, instructions):
    # run 
    alu = ALU()
    for digit in model:
        alu.add_input(digit)

    for cmd, a, b in instructions:
        alu.execute_instruction(cmd, a, b)

    return alu.register["z"] == 0

class ALU(object):
    def __init__(self):
        # init register
        self.register = {
            "x":0,
            "y":0,
            "z":0,
            "w":0
        }

        # init input FIFO
        self.input = Queue()

    def add_input(self, input):
        self.input.put(input)

    def execute_instruction(self, cmd, a, b):
        # switch to correct command
        if cmd == "inp":
            self.exe_input(a)
        elif cmd == "add":
            self.exe_add(a,b)
        elif cmd == "mul":
            self.exe_mul(a,b)
        elif cmd == "mod":
            self.exe_mod(a,b)
        elif cmd == "eql":
            self.exe_eql(a,b)
        elif cmd == "div":
            self.exe_div(a,b)
        else:
            print("Error: " + cmd)

    def exe_mul(self, a, b):
        int_a = self.replace_register(a)
        int_b = self.replace_register(b)

        self.register[a] = int_a * int_b

    def exe_div(self, a, b):        
        int_a = self.replace_register(a)
        int_b = self.replace_register(b)

        self.register[a] = int(int_a / int_b)

    def exe_mod(self, a, b):
        int_a = self.replace_register(a)
        int_b = self.replace_register(b)

        self.register[a] = int_a % int_b

    def exe_eql(self, a, b):
        int_a = self.replace_register(a)
        int_b = self.replace_register(b)

        self.register[a] = int(int_a == int_b)
            
    def exe_add(self, a, b):
        int_a = self.replace_register(a)
        int_b = self.replace_register(b)

        self.register[a] = int_a + int_b

    def exe_input(self, a):
        self.register[a] = self.input.get()

    def replace_register(self, a):
        # take negative numbers into account
        factor = 1
        if "-" in a:
            factor = -1
            a = a.replace("-", "")

        # replace with register content
        if not a.isnumeric():
            a = self.register[a]
        
        # intify
        return int(a) * factor

    def __repr__(self) -> str:
        return str(self.register)

def parse_file(file):
    lines = []
    with open(file, "r") as fp:
        for line in fp.readlines():
            # split instruction line
            items = line.replace("\n","").split(" ")

            # parse instruction line
            cmd = items[0]
            a   = items[1]
            if len(items) > 2:
                b = items[2]
            else:
                b = None

            lines.append((cmd, a, b))
    return lines

if __name__ == "__main__":
    main()