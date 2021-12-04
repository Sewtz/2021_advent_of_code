import numpy as np

def main():
    file = "input.txt"

    draws  = []
    boards = []

    # read data
    with open(file, "r") as fp:
        lines = fp.readlines()

        # first line are draws
        for number in lines[0].split(","):
            draws.append(int(number))

        new_board = []
        for line in lines[2:]:
            if len(line.strip()) > 0:
                # still in board
                new_board.append([int(x) for x in line.strip().split(" ") if len(x) > 0])

            else:
                boards.append(np.array(new_board))
                new_board = []

        boards.append(np.array(new_board))

    # part 1
    bingo = False
    for i in range(len(draws)):
        if bingo:
            break
        for board in boards:
            if bingo:
                break
            test, result = test_board(board, draws[:i])
            if test:
                print(result)
                bingo = True
    
    # part 2
    last_result = 0
    while len(boards) > 0:
        bingo = False
        for i in range(len(draws)):
            if bingo:
                break
            for b in range(len(boards)):
                if bingo:
                    break
                board = boards[b]
                test, result = test_board(board, draws[:i])
                if test:
                    boards = remove(boards, b)
                    last_result = result
                    bingo = True

    print(last_result)


def remove(arr, idx):
    new_arr = []
    for i in range(len(arr)):
        if not i == idx:
            new_arr.append(arr[i])

    return new_arr


def test_board(board, draws):
    # must have at least 5 draws
    if(len(draws) < 5):
        return (False, 0)

    draw_board = np.zeros(shape=board.shape)
    found      = []
    not_found  = []
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            if board[x,y] in draws:
                draw_board[x,y] = 1
                found.append(board[x,y])
            else:
                not_found.append(board[x,y])

    #print(draw_board)
    # test for each row and col
    bingo = False
    for r in range(draw_board.shape[0]):
        sum = draw_board[r,:].sum()
        if sum >= 5:
            bingo = True

    for c in range(draw_board.shape[1]):
        sum = draw_board[:,c].sum()
        if sum >= 5:
            bingo = True

    if bingo:
        a = np.array(not_found).sum()
        b = draws[-1]

        return (True, a*b)
    return (False, 0)


if __name__ == "__main__":
    main()