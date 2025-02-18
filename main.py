''' Main sudoku solver program - TRY 2
- main area for solving sudoku puzzle

--- TRY 1 ---
- Initial attempt; solving puzzle with functions

--- TRY 2 ---
- Implementing classes and objects for puzzle solving

--- Variables ---
- puzzle: 9x9 numpy array
    - 0: empty cell
    - 1-9: filled cell
- possible_values: 9x9x9 numpy array
    - sorted by value, row, column
    - 0: impossible value
    - 1: possible value


'''

# import numpy as np

class Sudoku:
    def __init__(self, b):
        self.board = b

    def print_board(self):
        ''' Print sudoku board '''
        for r in range(9): # print rows
            if r % 3 == 0:
                print("+ - - - + - - - + - - - +", end="\n")

            for c in range(9): # print columns
                if c % 3 == 0:
                    print("|", end=" ")
                print(f"{self.board[r][c]}", end=" ")

            print("|", end="\n")
        print("+ - - - + - - - + - - - +", end="\n")
        

    def find_empty_cell(self):
        ''' Find cell with value 0 '''

    def is_value(self, n, r, c):
        ''' Check if proposed value is valid '''

    def solve(self):
        ''' Solve sudoku puzzle '''




# --------------------- Initialisation --------------------- #

puzzle_unsolved = [[0, 0, 0, 4, 0, 0, 8, 0, 0],
                   [0, 1, 0, 8, 0, 5, 0, 0, 6],
                   [5, 0, 0, 0, 0, 0, 4, 1, 0],
                   [0, 0, 0, 0, 0, 0, 3, 0, 0],
                   [0, 0, 4, 0, 0, 0, 1, 0, 7],
                   [0, 6, 7, 0, 0, 0, 0, 5, 0],
                   [0, 0, 0, 0, 0, 7, 0, 8, 0],
                   [0, 0, 0, 3, 0, 0, 6, 0, 0],
                   [3, 0, 0, 0, 9, 6, 7, 0, 2]]



# --------------------- Main --------------------- #
sudoku = Sudoku(puzzle_unsolved)
print("Original Sudoku Board:")
sudoku.print_board()

