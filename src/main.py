
from array import *
from tkinter import *

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
                        rowTemp = r + rIndex
                        colTemp = c + cIndex

                        if (r + rIndex) < 0:
                            rowTemp = rowCount-1
                        elif (r + rIndex) >= rowCount:
                            rowTemp = 0

                        if (c + cIndex) < 0:
                            colTemp = colCount-1
                        elif (c + cIndex) >= colCount:
                            colTemp = 0

                        totalAlive += universe[rowTemp][colTemp]

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
    converter = lambda cell: " # " if cell == 1 else " _ "
    rowNum: int = 0
    for row in universe:
        renderedRow = " ".join(map(converter, row))
        Label(window, text=renderedRow).grid(row=rowNum, column=0)
        rowNum=rowNum+1

def nextGeneration(universe):
    nextGen = evolve(universe)
    printUniverse(nextGen)
    window.after(100, lambda: nextGeneration(nextGen))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()

    u = makeUniverse(25,75)
    u[1][2] = 1
    u[2][3] = 1
    u[3][1] = 1
    u[3][2] = 1
    u[3][3] = 1
    # u[1][2] = 1

    nextGeneration(u)
    window.mainloop()
