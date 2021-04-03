# Sudoku WIP solver
import random


def is_not_valid(empty_slots, slot, guess, board):
    if guess in empty_slots[slot[0]]:
        return True
    columns = list()
    for i in range(9):
        columns.append((i, slot[1]))
    for coord in columns:
        if guess == board[coord[0]][coord[1]]:
            return True
    for row in range(slot[0] // 3):
        for col in range(slot[1] // 3):
            if board[row][col] == guess:
                return True
    return False


# sudoku board
def solver():
    num = 0
    board = [
        [0, 7, 2, 0, 0, 9, 3, 1, 0],
        [5, 1, 0, 0, 0, 2, 0, 8, 9],
        [0, 9, 4, 0, 3, 1, 7, 5, 0],
        [0, 6, 0, 0, 5, 0, 2, 3, 0],
        [2, 0, 1, 0, 0, 0, 5, 0, 0],
        [0, 3, 0, 2, 8, 4, 0, 0, 1],
        [0, 2, 0, 4, 1, 0, 0, 0, 0],
        [0, 0, 7, 0, 2, 8, 1, 0, 5],
        [0, 0, 0, 0, 6, 0, 9, 0, 0]
    ]

    # finds slots need to be solved
    empty_slots = list()
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                empty_slots.append((row, col))
    zero = True
    while zero:
        for slot in empty_slots:
            flag = True
            while flag:
                num = random.randint(1, 10)
                flag = is_not_valid(empty_slots, slot, num, board)
            board[slot[0]][slot[1]] = num
            print(board[slot[0]])
        zero = False
        for row in board:
            for item in row:
                if item == 0:
                    zero = True
                    break
    for row in board:
        print(row)


if __name__ == '__main__':
    solver()
