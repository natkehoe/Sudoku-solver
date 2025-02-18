''' Main sudoku solver program - TRY 1
- main area for solving sudoku puzzle

--- TRY 1 ---
- Initial attempt; solving puzzle with functions

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

# --------------------- Initialisation --------------------- #

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

# --------------------- Functions --------------------- #

possible_values = np.ones((9, 9, 9), dtype=bool)

def init_eliminate_values(puzzle, possible_values):
    '''
    ONLY RUN ONCE - at beginning of script
    '''
    # Eliminate all possible rows and columns from possible_values
    for row in range(9):
        for col in range(9):
            # if cell is occupied, remove possibility
            if puzzle[row, col] != 0:
                possible_values[:, row, col] = False # eliminate position
                possible_values[puzzle[row, col]-1, row, :] = False # eliminate row
                possible_values[puzzle[row, col]-1, :, col] = False # eliminate column

                # eliminate box
                possible_values[puzzle[row, col]-1, row//3*3:row//3*3+3, col//3*3:col//3*3+3] = False

def eliminate_value(pos, puzzle, possible_values):
    '''
    Eliminate a new value as one appears 
    - pos = position of value [row, col]
    - puzzle = existing puzzle
    - possible_values = 9x9x9 array of possible values
    '''
    possible_values[:, pos[0], pos[1]] = False # eliminate position
    possible_values[puzzle[pos[0], pos[1]]-1, pos[0], :] = False # eliminate row
    possible_values[puzzle[pos[0], pos[1]]-1, :, pos[1]] = False # eliminate column

    # eliminate box
    possible_values[puzzle[pos[0], pos[1]]-1, pos[0]//3*3:pos[0]//3*3+3, pos[1]//3*3:pos[1]//3*3+3] = False



def eliminate_rowscols(puzzle, possible_values):
    ''' 
    Eliminate all rows if possible values exist 
    in a subgrid in only one row/column 
    '''

    # Eliminate any rows/cols where values can only exist on that row/col in a subgrid
    for srow in range(3):
        for scol in range(3):
            
            # select subgrid
            subgrid = possible_values[:, srow*3:srow*3+3, scol*3:scol*3+3]

            # eliminate values that ############################################



            # find values aligned in rows/cols
            rowValues = np.where(np.sum(np.sum(subgrid, axis=2)!=0, axis=1) == 1)
            colValues = np.where(np.sum(np.sum(subgrid, axis=1)!=0, axis=1) == 1)
            Values = np.append(rowValues, colValues) # a full list of values that only exist in rows/cols

            if np.any(rowValues):
                for value in rowValues:
                    # find which row it is, and eliminate all other values outside of grid
                    row = np.argmax(np.sum(subgrid[value,:,:], axis=2) != 0)

                    # delete all possible values along row outside of subgrid
                    possible_values[value, srow*3+row, 0:scol*3] = False
                    possible_values[value, srow*3+row, (scol+1)*3:] = False
                # pass # delete

            if np.any(colValues):
                for value in colValues:
                    # find which column it is, and eliminate all other values outside of grid
                    col = np.argmax(np.sum(subgrid[value,:,:], axis=1) != 0)

                    # delete all possible values along column outside of subgrid
                    possible_values[value, 0:srow*3, scol*3+col] = False
                    possible_values[value, (srow+1)*3:, scol*3+col] = False

            # find values with rows only
            # find which row it is
            # eliminate all other values outside of grid


def find_single_values(puzzle, possible_values):
    '''
    - count number of possible values for each cell
    - if one cell only has one possible value, assign it to puzzle
    - if it's the only '''
    for row in range(9):
        for col in range(9):
            if puzzle[row, col] == 0:
                if np.sum(possible_values[:, row, col]) == 1: # if only one value possible, assign it to puzzle
                    puzzle[row, col] = np.argmax(possible_values[:, row, col]) + 1
                    print(f"New value assigned: {puzzle[row, col]} at [{row+1}, {col+1}]")

                # if only one cell in subgrid is possible, assign it to puzzle
                subgrid = possible_values[:, row//3*3:row//3*3+3, col//3*3:col//3*3+3]
                srow = row%3
                scol = col%3

                # if np.sum(subgrid) == 1:
                #     puzzle[row, col] = np.argmax(possible_values[:, row, col]) + 1
                #     print(f"New value assigned: {puzzle[row, col]} at [{row+1}, {col+1}]")

                if np.sum(np.sum(subgrid, axis=1), axis=1)[srow+scol] == 1:
                    puzzle[row, col] = np.argmax(possible_values[:, row, col]) + 1
                    print(f"New value assigned: {puzzle[row, col]} at [{row+1}, {col+1}]")

def assign_value(value, pos, puzzle, possible_values):
    '''
    - Assigns new value to puzzle
    - Deletes rows/columns/subgrids associated with that value in possible_values
    - Prints value and position of assigned value to console 

    Inputs:
    - value = value to be assigned
    - pos = position of value [row, col]
    - puzzle = existing puzzle
    - possible_values = possible potential values on grid 
    '''
    puzzle[pos[0],pos[1]] = value+1
    eliminate_value([pos[0], pos[1]], puzzle, possible_values)
    eliminate_rowscols(puzzle, possible_values)
    print(f"New value: {puzzle[pos[0],pos[1]]} at [{pos[0]}, {pos[1]}]")



    ####################################################################



def find_values_by_number(puzzle, possible_values):
    # x = None
    # y = None

    # Check each value if there are available spaces
    for value in range(9):
        checkrows = np.sum(possible_values[value,:,:], axis=1)
        checkcols = np.sum(possible_values[value,:,:], axis=0)

        # check if any columns/rows only have one possibility
        if any(checkcols == 1):
            x = np.argmax(checkcols == 1) # select row
            y = np.argmax(possible_values[value, :, x]) # select col
            # puzzle[y,x] = value+1 # assign value
            # print(f"New value assigned: {puzzle[y,x]} at [{y+1}, {x+1}]")
            assign_value(value, [y,x], puzzle, possible_values)
            return
        elif any(checkrows == 1):
            y = np.argmax(checkrows == 1)
            x = np.argmax(possible_values[value, y, :])
            # puzzle[y,x] = value+1 # assign value
            # print(f"New value assigned: {puzzle[y,x]} at [{y+1}, {x+1}]")
            assign_value(value, [y,x], puzzle, possible_values)
            return

    # if any value only occurs once in subgrid, assign
    for srow in range(3):
        for scol in range(3):
            subgrid = possible_values[:, srow*3:srow*3+3, scol*3:scol*3+3]

            if np.any(np.sum(np.sum(subgrid, axis=1), axis=1) == 1):
                value = int(np.argmax(np.sum(np.sum(subgrid, axis=1), axis=1)==1))
                sy,sx = np.where(subgrid[value,:,:])

                y = (int(sy[0]) + srow*3)
                x = (int(sx[0]) + scol*3)
                # puzzle[y,x] = value+1 # assign value
                # print(f"New value assigned: {puzzle[y,x]} at [{y+1}, {x+1}]")
                assign_value(value, [y,x], puzzle, possible_values)
                return
            
    # if only one value possible in cell, assign
    if np.any(np.sum(possible_values, axis=0) == 1):
        yvals, xvals = np.where(np.sum(possible_values, axis=0)==1)

        # iterate over all found values
        for y, x in zip(yvals, xvals):
            value = np.argmax(possible_values[:,y,x])
            # puzzle[y,x] = value+1 # assign value
            # print(f"New value assigned: {puzzle[y,x]} at [{y+1}, {x+1}]")
            assign_value(value, [y,x], puzzle, possible_values)
            return


def print_puzzle(txtfile, puzzle):
    # Create a printable puzzle text fil
    with open(txtfile, "a") as f:
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

def print_tofile(txtfile, txt):
    with open(txtfile, "a") as f:
        # write new line to puzzle
        f.write(f"{txt}")
    f.close()


def find_pointing_pairs(puzzle, possible_values): # find values that only exist in a row/col in a subgrid
    pass

            

            


# --------------------- Main --------------------- #
# while True:
try:
    init_eliminate_values(puzzle, possible_values)
    for i in range(50): # while some values exist, keep eliminating
        print(i)
        # find_single_values(puzzle, possible_values)
        find_values_by_number(puzzle, possible_values)
        # print(f"Update {i}: \n{puzzle}")

        # if i == 53 or not possible_values[8,3,0]:
        if i == 12: # 9 assigned to row/col [2,8] when not supposed to
            pass # DEBUG CHECKPOINT

        if not np.any(possible_values):
            if np.any(puzzle == 0):
                print("ERROR - puzzle is incomplete.")
            else:
                print("PUZZLE IS COMPLETE!")
            break


    print(f"Final solution: \n{puzzle}")

    print(f"Possible values: \n{possible_values}")


    # Print puzzle
    txtfile = "puzzle.txt"
    f = open(txtfile, "w")
    f.close

    print_tofile(txtfile, "\n--- Unsolved puzzle ---\n")
    print_puzzle(txtfile, puzzle_unsolved)
    print_tofile(txtfile, "\n\n--- Solved puzzle ---\n")
    print_puzzle(txtfile, puzzle)

except Exception as e:
    print(f"\n--- Error found ---\n{e}")
    print(f"\nFinal solution: \n{puzzle}")
    # print(f"Possible values: \n{possible_values}")
