# import random

# matrix = []
# total = 0

# row_num = eval(input("Enter Number Of Row: "))
# col_num = eval(input("Enter Number Of Column: "))

# for row in range(0,row_num):
#     matrix.append([])
#     for column in range(0,col_num):
#         matrix[row].append(random.randrange(0,100))

# for row in range(len(matrix[0])):
#     for column in range(len(matrix)):
#         total += matrix[row][column]

# print(matrix)
# print("The Total = ",total)

# Check whether a solution is valid 
def isValid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] < 1 or grid[i][j] > 9 \
               or not isValidAt(i, j, grid):
                return False
    return True # The fixed cells are valid

# Check whether grid[i][j] is valid in the grid 
def isValidAt(i, j, grid):
    # Check whether grid[i][j] is valid at the i's row
    for column in range(9):
        if column != j and grid[i][column] == grid[i][j]:
            return False

    # Check whether grid[i][j] is valid at the j's column
    for row in range(9):
        if row != i and grid[row][j] == grid[i][j]:
            return False

    # Check whether grid[i][j] is valid in the 3 by 3 box
    for row in range((i // 3) * 3, (i // 3) * 3 + 3):
          for col in range((j // 3) * 3, (j // 3) * 3 + 3):
             if row != i and col != j and \
                    grid[row][col] == grid[i][j]:
                 return False

    return True # The current value at grid[i][j] is valid
from CheckSudokuSolution import isValid

def main():
    # Read a Sudoku solution
    grid = readASolution()

    if isValid(grid):
        print("Valid solution")
    else:
        print("Invalid solution")
  
# Read a Sudoku solution from the console 
def readASolution():
    print("Enter a Sudoku puzzle solution:")
    grid = []
    for i in range(9):
        line = input().strip().split()
        grid.append([int(x) for x in line])
    
    return grid

main() # Call the main functio