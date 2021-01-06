# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from array import *

ALIVE = 1
DEAD = 0
OFFSETS = [-1, 0, 1]

def makeUniverse(rows, columns):
    return [[0] * columns for i in range(rows)]

def evolve(universe: list[list[int]]):


    # 1100     0000
    # 0X00  => 0000
    # 0000     0000
    # 0011     0000

    rowCount = len(universe)
    colCount = len(universe[0])

    newUniverse: list[list[int]] = makeUniverse(rowCount, colCount)

    for r in range(rowCount):
        for c in range(colCount):

            totalAlive: int = 0
            for rIndex in OFFSETS:
                for cIndex in OFFSETS:
                    if not (rIndex == 0 and cIndex == 0):
                        if (r + rIndex) >= 0 and (c + cIndex) >= 0:
                            if (r + rIndex) < rowCount and (c + cIndex) < colCount:
                                totalAlive += universe[r+rIndex][c+cIndex]

            newUniverse[r][c] = evolveCell(universe[r][c], totalAlive)

    return newUniverse

def evolveCell(cellState: int, total_alive: int):
    if cellState == ALIVE and total_alive < 2:
        return DEAD
    elif cellState == ALIVE and total_alive > 3:
        return DEAD
    elif cellState == DEAD and total_alive == 3:
        return ALIVE
    else:
        return cellState

def printUniverse(universe: list[list[int]]):
    converter = lambda cell: "*" if cell == 1 else "_"
    for row in universe:
        print(" ".join(map(converter, row)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    u = makeUniverse(10,10)
    u[1][2] = 1
    u[2][3] = 1
    u[3][1] = 1
    u[3][2] = 1
    u[3][3] = 1
    # u[1][2] = 1

    printUniverse(u)
    print("\n")

    for _ in range(100):
        u = evolve(u)
        printUniverse(u)
        print("\n")
