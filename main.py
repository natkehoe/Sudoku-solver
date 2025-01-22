''' Main sudoku solver program
- main area for solving sudoku puzzle

--- Variables ---
- puzzle: 9x9 numpy array
    - 0: empty cell
    - 1-9: filled cell
- possible_values: 9x9x9 numpy array
    - sorted by value, row, column
    - 0: impossible value
    - 1: possible value


'''

import numpy as np

# ---- Initialisation ---- #

puzzle_unsolved = np.array([[0, 0, 0, 4, 0, 0, 8, 0, 0],
                   [0, 1, 0, 8, 0, 5, 0, 0, 6],
                   [5, 0, 0, 0, 0, 0, 4, 1, 0],
                   [0, 0, 0, 0, 0, 0, 3, 0, 0],
                   [0, 0, 4, 0, 0, 0, 1, 0, 7],
                   [0, 6, 7, 0, 0, 0, 0, 5, 0],
                   [0, 0, 0, 0, 0, 7, 0, 8, 0],
                   [0, 0, 0, 3, 0, 0, 6, 0, 0],
                   [3, 0, 0, 0, 9, 6, 7, 0, 2]])

puzzle = puzzle_unsolved.copy()

# ---- Functions ---- #

possible_values = np.ones((9, 9, 9), dtype=bool)

def eliminate_values(puzzle, possible_values):
    # Eliminate possible rows and columns from possible_values
    for row in range(9):
        for col in range(9):
            # if cell is occupied, remove possibility
            if puzzle[row, col] != 0:
                possible_values[:, row, col] = False # eliminate position
                possible_values[puzzle[row, col]-1, row, :] = False # eliminate row
                possible_values[puzzle[row, col]-1, :, col] = False # eliminate column

                # eliminate box
                box_row = row // 3
                box_col = col // 3
                possible_values[puzzle[row, col]-1, box_row*3:box_row*3+3, box_col*3:box_col*3+3] = False

def find_single_values(puzzle, possible_values):
    '''
    - count number of possible values for each cell
    - if one cell only has one possible value, assign it to puzzle
    - if it's the only '''
    for row in range(9):
        for col in range(9):
            # if only one value possible, assign to puzzle
            if np.sum(possible_values[:, row, col]) == 1: # if only one value possible, assign it to puzzle
                puzzle[row, col] = np.argmax(possible_values[:, row, col]) + 1
                print("New value assigned!")

    # # if only one cell in row/column/box has a possible value, assign it to puzzle
    # for value in range(9):
    #     if
    #         # 


# # Find cells where only one possibility exists
# for row in range(9):
#     for col in range(9):
#         if np.sum(possible_values[:, row, col]) == 1: # if only one value possible, assign it to puzzle

def print_puzzle(txtfile, puzzle):
    # Create a printable puzzle text fil
    with open(txtfile, "w") as f:
        # Write puzzle in readable format
        for row in range(9):
            if row % 3 == 0:
                f.write("+ - - - - - + - - - - - + - - - - - +\n")

            for col in range(9):
                if col % 3 == 0:
                    f.write("|  ")
                f.write(f"{puzzle[row, col]}  ")

            f.write("|\n")
        f.write("+ - - - - - + - - - - - + - - - - - +\n")
        f.close()
            

            


# ---- Main ---- #
# while True:
for i in range(1000): # while some values exist, keep eliminating
    eliminate_values(puzzle, possible_values)
    find_single_values(puzzle, possible_values)


# If all cells are filled, break
if all(puzzle.flatten() != 0):
    print("All cells filled!")
    # break
else:
    print("Not all cells filled!")


print(f"Final solution: \n{puzzle}")

print_puzzle("puzzle.txt", puzzle)