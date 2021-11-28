import numpy as np
import matplotlib.pyplot as plt

def main():
    # create sine wave
    x = [x for x in range(0,360)]
    y = [np.sin(y * np.pi / 180.) for y in x]

    # plot
    plt.figure()
    plt.plot(x,y,"-k")
    plt.show()

if __name__ == "__main__":
    main()