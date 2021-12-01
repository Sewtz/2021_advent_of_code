from argparse import ArgumentParser
import os

def main():
    # get input
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True)
    args = parser.parse_args()

    # part 1
    if os.path.exists(args.input):
        last = None
        times_increased = 0

        # open file and read line-by-line
        with open(args.input, "r") as fp:
            for line in fp.readlines():
                if not last is None:
                    current = int(line)

                    # check if line has increased
                    if current > last:
                        times_increased += 1
                
                # save for next round
                last = int(line)

        print(times_increased)

    # part 2
    if os.path.exists(args.input):
        times_increased = 0
        values = []
        last = None
        with open(args.input, "r") as fp:
            for line in fp.readlines():
                # create sliding window
                values.append(int(line))

                # calc window
                if len(values) >= 3:
                    current = values[-1] + values[-2] + values[-3]

                    # check if window increased
                    if not last is None:
                        if current > last:
                            times_increased += 1

                    last = current  

        print(times_increased)

if __name__ == "__main__":
    main()