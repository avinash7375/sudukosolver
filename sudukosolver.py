import math
M = 9  # Didn't change it as you made it that way so I just improved your code to handle it dynamically


def printBoard(a: list[list[int]]) -> None:
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()


def checkIfValid(grid: list[list[int]], row: int, col: int, num: int) -> bool:
    for x in range(M):
        if grid[row][x] == num:
            return False

    for x in range(M):
        if grid[x][col] == num:
            return False

    sqr = int(math.sqrt(M))
    startRow = row - row % sqr
    startCol = col - col % sqr
    for i in range(sqr):
        for j in range(sqr):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def solve(grid: list[list[int]]) -> bool:
    for i in range(M):
        for j in range(M):
            if grid[i][j] == 0:
                for k in range(1, M + 1):
                    if (checkIfValid(grid, i, j, k)):
                        grid[i][j] = k
                        if (solve(grid)):
                            return True
                        grid[i][j] = 0
                return False
    return True


'''0 means the cells where no value is assigned'''
grid = [
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
    printBoard(grid)
else:
    print("Solution does not exist:(")
