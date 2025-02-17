''' For testing purposes only - test functions, ideas. '''
### Reading image ###
# import cv2 as cv
# from matplotlib import pyplot as plt

# img = cv.imread("unsolved_puzzle.png")


# # Show grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# # Show edges only
# canny = cv.Canny(img, 125, 175)

# # Resize image
# # resized = cv.resize(img, None)


# cv.imshow('Unsolved puzzle', img)

# cv.waitKey(0)



### Objects and Classes ###
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

class Sudoku:
    def __init__(self, board):
        """Initialize the Sudoku board."""
        self.board = board  # 9x9 grid

    def print_board(self):
        """Print the Sudoku board in a readable format."""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)  # Horizontal separator
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")  # Vertical separator
                print(self.board[i][j] if self.board[i][j] != 0 else ".", end=" ")
            print()

    def find_empty_cell(self):
        """Find an empty cell (represented by 0). Returns (row, col) or None if full."""
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None  # No empty cells

    def is_valid(self, num, row, col):
        """Check if placing 'num' at board[row][col] is valid."""
        # Check row
        if num in self.board[row]:
            return False

        # Check column
        if num in [self.board[i][col] for i in range(9)]:
            return False

        # Check 3x3 box
        box_x, box_y = row // 3 * 3, col // 3 * 3
        for i in range(3):
            for j in range(3):
                if self.board[box_x + i][box_y + j] == num:
                    return False

        return True

    def solve(self):
        """Solve the Sudoku puzzle using backtracking."""
        empty = self.find_empty_cell()
        if not empty:
            return True  # Solved

        row, col = empty

        for num in range(1, 10):  # Numbers 1 to 9
            if self.is_valid(num, row, col):
                self.board[row][col] = num

                if self.solve():  # Recursive step
                    return True

                self.board[row][col] = 0  # Undo and backtrack

        return False  # No solution found

# Example Sudoku board (0 represents empty spaces)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

puzzle_unsolved = [[0, 0, 0, 4, 0, 0, 8, 0, 0],
                   [0, 1, 0, 8, 0, 5, 0, 0, 6],
                   [5, 0, 0, 0, 0, 0, 4, 1, 0],
                   [0, 0, 0, 0, 0, 0, 3, 0, 0],
                   [0, 0, 4, 0, 0, 0, 1, 0, 7],
                   [0, 6, 7, 0, 0, 0, 0, 5, 0],
                   [0, 0, 0, 0, 0, 7, 0, 8, 0],
                   [0, 0, 0, 3, 0, 0, 6, 0, 0],
                   [3, 0, 0, 0, 9, 6, 7, 0, 2]]

sudoku = Sudoku(puzzle_unsolved)
print("Original Sudoku Board:")
sudoku.print_board()

if sudoku.solve():
    print("\nSolved Sudoku Board:")
    sudoku.print_board()
else:
    print("\nNo solution exists.")
