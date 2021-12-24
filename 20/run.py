file = "input.txt"

def main():
    # read file
    algo, img = read_file(file)

    # init image
    pixels = set(
        (i, j)
        for i, row in enumerate(img)
        for j, ch in enumerate(row)
        if ch == '#'
    )

    # ehance image
    for i in range(2):
        pixels = step(pixels, algo, i & 1 & algo[0])

    # count lit pixels
    print(len(pixels))

def read_file(file):
    algorithm, _, *image = open(file, 'r').read().split('\n')
    algorithm = [int(ch == '#') for ch in algorithm]
    return algorithm, image

def step(pixels, algo, inf):
    min_i, max_i = min(p[0] for p in pixels), max(p[0] for p in pixels)
    min_j, max_j = min(p[1] for p in pixels), max(p[1] for p in pixels)

    enhanced_pixels = set()

    for i in range(min_i - 1, max_i + 2):
        for j in range(min_j - 1, max_j + 2):
            index = 0
            for di in range(i - 1, i + 2):
                for dj in range(j - 1, j + 2):
                    index = index << 1 | (
                        int((di, dj) in pixels)
                        if (min_i <= di <= max_i and min_j <= dj <= max_j)
                        else inf
                    )

            if (algo[index]):
                enhanced_pixels.add((i, j))

    return enhanced_pixels

if __name__ == "__main__":
    main()