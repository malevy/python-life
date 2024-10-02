import random


class Universe:

    _currentGeneration: list[list[bool]] = []

    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        for rIndex in range(rows):
            self._currentGeneration.append([])
            for cIndex in range(columns):
                self._currentGeneration[rIndex].append(random.random() > 0.7)

    def _countLiveNeighbors(self, row: int, column: int):
        OFFSETS: list[int] = [-1, 0, 1]
        total = 0
        for rIndex in OFFSETS:
            for cIndex in OFFSETS:
                if rIndex == 0 and cIndex == 0:
                    continue

                if (
                    (row + rIndex) >= 0
                    and (column + cIndex) >= 0
                    and (row + rIndex) < self.rows
                    and (column + cIndex) < self.columns
                ):
                    total += int(self._currentGeneration[row + rIndex][column + cIndex])
        return total

    def _evolveCell(self, currentState: bool, liveNeighbors: int):
        ALIVE = True
        DEAD = False
        if currentState == ALIVE and liveNeighbors < 2:
            return DEAD
        elif currentState == ALIVE and liveNeighbors > 3:
            return DEAD
        elif currentState == DEAD and liveNeighbors == 3:
            return ALIVE
        else:
            return currentState

    def evolve(self):
        nextGeneration: list[list[bool]] = []

        for rIndex in range(self.rows):
            nextGeneration.append([])
            for cIndex in range(self.columns):
                liveNeighbors = self._countLiveNeighbors(rIndex, cIndex)
                currentState = self._currentGeneration[rIndex][cIndex]
                nextGeneration[rIndex].append(
                    self._evolveCell(currentState, liveNeighbors)
                )

        self._currentGeneration = nextGeneration

    def visit(self, callback, liveOnly=False):
        """
        Visit each cell in the universe and call the provided
        callback with the row index, column index, and state of the cell.

        :param callback: function to call with the row index, column index, and state of each cell
        :param liveOnly: if True, only call the callback with live cells
        """
        DEAD = False
        for rIndex in range(self.rows):
            for cIndex in range(self.columns):
                state = self._currentGeneration[rIndex][cIndex]
                if liveOnly and state == DEAD:
                    continue

                callback(rIndex, cIndex, state)
