input_state = [3,5,2,5,4,3,2,2,3,5,2,3,2,2,2,2,3,5,3,5,5,2,2,3,4,2,3,5,5,3,3,5,2,4,5,4,3,5,3,2,5,4,1,1,1,5,1,4,1,4,3,5,2,3,2,2,2,5,2,1,2,2,2,2,3,4,5,2,5,4,1,3,1,5,5,5,3,5,3,1,5,4,2,5,3,3,5,5,5,3,2,2,1,1,3,2,1,2,2,4,3,4,1,3,4,1,2,2,4,1,3,1,4,3,3,1,2,3,1,3,4,1,1,2,5,1,2,1,2,4,1,3,2,1,1,2,4,3,5,1,3,2,1,3,2,3,4,5,5,4,1,3,4,1,2,3,5,2,3,5,2,1,1,5,5,4,4,4,5,3,3,2,5,4,4,1,5,1,5,5,5,2,2,1,2,4,5,1,2,1,4,5,4,2,4,3,2,5,2,2,1,4,3,5,4,2,1,1,5,1,4,5,1,2,5,5,1,4,1,1,4,5,2,5,3,1,4,5,2,1,3,1,3,3,5,5,1,4,1,3,2,2,3,5,4,3,2,5,1,1,1,2,2,5,3,4,2,1,3,2,5,3,2,2,3,5,2,1,4,5,4,4,5,5,3,3,5,4,5,5,4,3,5,3,5,3,1,3,2,2,1,4,4,5,2,2,4,2,1,4]
#input_state = [3,4,3,1,2]

new_fish_timer = 9
old_fish_timer = 7

def main():
    num_fish = track_states(input_state, days_to_simulate=256)
    print(num_fish)

def track_states(states, days_to_simulate):
    # create initial states
    current_state = {}
    for i in range(10):
        current_state[i] = 0

    for ele in states:
        current_state[ele] += 1

    for day in range(days_to_simulate):
        # count new fish
        new_fish = current_state[0]

        # add new fish
        current_state[9]  = new_fish

        # replace fish with timer 0
        current_state[old_fish_timer] += current_state[0]
        current_state[0]               = 0

        # decrease timer for each fish
        for i in range(len(current_state.keys()) - 1):
            current_state[i] = current_state[i+1]

        current_state[len(current_state.keys())-1] = 0

        # debug output
        print("{0:3d}/{1:3d}".format(day, days_to_simulate), end="\r")

    print("")
    

    return sum(current_state.values())

if __name__ == "__main__":
    main()