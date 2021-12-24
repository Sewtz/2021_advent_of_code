class Player():
    def __init__(self, name, init_position):
        self.name       = name
        self.position   = init_position
        self.score      = 0
        self.roll_count = 0

    def roll(self, rolls):
        for roll in rolls:
            self.position += roll

        self.position = ((self.position - 1) % 10) + 1
        self.score += self.position
        self.roll_count += len(rolls)

    def __repr__(self) -> str:
        return "Player {2:} Position: {0:} Score: {1:} Rolls: {3:}".format(self.position, self.score, self.name, self.roll_count)

def main():
    p1 = Player(init_position=6, name="1")
    p2 = Player(init_position=1, name="2")

    i         = 1
    end_score = 1000
    while not p1.score >= end_score or not p2.score >= end_score:
        # player 1 
        p1.roll([i, i+1, i+2])
        i += 3

        if p1.score >= end_score:
            break

        # player 2
        p2.roll([i, i+1, i+2])
        i += 3

    i -= 1 # correct number
    print(i)
    print("")

    print(p1)
    print(p1.score * i)

    print("")

    print(p2)
    print(p2.score * i)

if __name__ == "__main__":
    main()