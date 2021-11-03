import math
M = 9  # Didn't change it as you made it that way so I just improved your code to handle it dynamically


def printBoard(a: list[list[int]]) -> None: #This is be used to print the Board
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()


def checkIfValid(grid: list[list[int]], row: int, col: int, num: int) -> bool:  #this will check if the place to put nummber is valid or not 
    for x in range(M):      #checking rows for putting valid input
        if grid[row][x] == num:
            return False

    for x in range(M):      #checking columns for putting valid input
        if grid[x][col] == num:
            return False

    sqr = int(math.sqrt(M))     #this will check if the number is in 3 x 3 matrix
    startRow = row - row % sqr
    startCol = col - col % sqr
    for i in range(sqr):
        for j in range(sqr):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def solve(grid: list[list[int]]) -> bool:       #the main solution
    for i in range(M):      #rows
        for j in range(M):      #cols
            if grid[i][j] == 0:     #if the grid has the empty space 
                for k in range(1, M + 1):                   #k is the input to be put in valid space(grid)
                    if (checkIfValid(grid, i, j, k)):       #check if the grid is valid to take valid input
                        grid[i][j] = k                      #print the input
                        if (solve(grid)):                   #if the grid is solved(right value) 
                            return True                     #return True
                        grid[i][j] = 0                      #or else make grid = o
                return False
    return True


'''0 means the cells where no value is assigned'''
grid = [                                            #input for grid
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]
]


if (solve(grid)):
    printBoard(grid)            #this will print the solved grid
else:
    print("Solution does not exist:(")      #else the grid is invalid to be solved
