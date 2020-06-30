sudoku_board = [
    [4, 0, 0, 0, 9, 6, 0, 0, 8],
    [0, 5, 9, 0, 2, 4, 0, 0, 6],
    [0, 6, 0, 3, 0, 0, 0, 9, 4],
    [0, 0, 2, 0, 0, 0, 0, 6, 0],
    [6, 8, 0, 0, 0, 0, 4, 5, 1],
    [0, 7, 0, 0, 0, 0, 0, 8, 0],
    [8, 1, 5, 4, 0, 0, 6, 2, 7],
    [7, 0, 0, 0, 0, 0, 8, 0, 0],
    [2, 0, 0, 0, 6, 8, 0, 1, 5],
]


def solve(board):
    find = find_first_empty_block(board)
    if not find:
        return True
    else:
        row, column = find

    for index in range(1, 10):
        if valid(board, index, (row, column)):
            board[row][column] = index

            if solve(board):
                return True

            board[row][column] = 0
    return False


def valid(board, number, position):
    # Check row 
    for i in range(0, len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
            # Check column
    for i in range(0, len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

            # Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_x * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 1):
            if board[i][j] == number and (i, j) != position:
                return False
    return True


# Print the sudoku board 
def print_sudoku_solver(board):
    for row in range(0, len(board)):
        if (row % 3 == 0) and (row != 0):
            print("------------------------")

        for column in range(0, len(board[0])):
            if (column % 3 == 0) and (column != 0):
                print(" | ", end="")
            if (column == 8):
                print(board[row][column])
            else:
                print(str(board[row][column]) + " ", end="")


# Find the first empty block
def find_first_empty_block(board):
    for row in range(0, len(board)):

        for column in range(0, len(board[0])):
            if (board[row][column] == 0):
                return (row, column)

    return None


print_sudoku_solver(sudoku_board)
# first_empty_block = find_first_empty_block(sudoku_board)
# print("First empty block:", first_empty_block) 

print()
print()
solve(sudoku_board)
print_sudoku_solver(sudoku_board)
