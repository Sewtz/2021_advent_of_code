import numpy as np

def main():
    # define target
    target = ((235,259),(-118,-62))

    # inital states
    max_y = -1
    hits  = 0

    # test range (based on target)
    x_values = range(0,260)
    y_values = range(-118,200)

    # iterate
    step     = 1
    for vx in x_values:
        for vy in y_values:
            hit, possible_y, poses = shoot(((0,0), (vx, vy)), target)
            if hit:
                hits += 1

            if hit and possible_y > max_y:
                max_y = possible_y
                
            print("{0:5d}/{1:5d}\t{2:}".format(step, len(x_values)*len(y_values), max_y), end="\r")
            step += 1

    print("")
    print(max_y)
    print(hits)

def shoot(initial, target):
    # some stats
    max_y = initial[0][1]

    # check if initial is already a hit
    if hit(initial[0], target):
        return True, max_y [initial[0]]

    # simulate shoot
    current = initial
    steps   = 0
    poses   = [current[0]]
    while steps < distance(initial[0], target):
        # apply step
        current = step(current)
        steps  += 1
        poses.append(current[0])

        # update stats
        if current[0][1] > max_y:
            max_y = current[0][1]

        # check if hit
        if hit(current[0], target):
            #print(initial[1], max_y, current[0])
            return True, max_y, poses

    # if we reach this, we missed
    return False, max_y, poses

def hit(x1, target):
    if x1[0] >= min(target[0]) and x1[0] <= max(target[0]):
        if x1[1] >= min(target[1]) and x1[1] <= max(target[1]):
            return True
    return False

def distance(x1,target):
    target_center = [np.mean(target[0]), np.mean(target[1])]
    distance = np.sqrt((x1[0]-target_center[0])**2 + (x1[1]-target_center[1])**2)
    return distance

def step(current):
    # update position
    x  = current[0][0]
    y  = current[0][1]
    x += current[1][0]
    y += current[1][1]

    # update velocity
    vx = current[1][0]
    vy = current[1][1]
    if vx < 0:
        vx += 1
    elif vx > 0:
        vx -= 1
    vy -= 1
    return ((x,y), (vx,vy))

if __name__ == "__main__":
    main()