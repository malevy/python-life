from main import *


def test_liveCellWith0Neighbours_dies():
    # arrange
    u = makeUniverse(3, 3)
    u[1][1] = 1

    # act
    nu = evolve(u)

    # assert
    assert nu[1][1] == 0


def test_liveCellWith1Neighbours_dies():
    # arrange
    u = makeUniverse(3, 3)
    u[1][1] = 1
    u[1][0] = 1

    # 000
    # 110
    # 000


    # act
    nu = evolve(u)

    # assert
    assert nu[1][1] == 0


def test_liveCellWith2Neighbours_lives():
    # arrange
    u = makeUniverse(3, 3)
    u[1][1] = 1
    u[1][0] = 1
    u[2][1] = 1

    # act
    nu = evolve(u)

    # assert
    assert nu[1][1] == 1

def test_liveCellWith3Neighbours_lives():
    # arrange
    u = makeUniverse(3, 3)
    u[1][1] = 1
    u[1][0] = 1
    u[2][1] = 1
    u[1][2] = 1

    # act
    nu = evolve(u)

    # assert
    assert nu[1][1] == 1

def test_liveCellWith4Neighbours_dies():
    # arrange
    u = makeUniverse(3, 3)
    u[1][1] = 1
    u[1][0] = 1
    u[2][1] = 1
    u[1][2] = 1
    u[0][1] = 1

    # act
    nu = evolve(u)

    # assert
    assert nu[1][1] == 0

def test_deadCellWith3Neighbours_lives():
    # arrange
    u = makeUniverse(3, 3)
    u[1][1] = DEAD
    u[1][0] = ALIVE
    u[2][1] = ALIVE
    u[1][2] = ALIVE

    # act
    nu = evolve(u)

    # assert
    assert nu[1][1] == 1

def test_small_aliveCellWith0Neighbours_dies():
    # arrange
    u = makeUniverse(2, 2)
    u[0][0] = DEAD

    # act
    nu = evolve(u)

    # assert
    assert nu[0][0] == 0

def test_large_aliveCellWith0Neighbours_dies():
    # arrange
    u = makeUniverse(4, 4)
    u[0][0] = ALIVE # subject
    u[0][1] = ALIVE
    u[3][2] = ALIVE # subject
    u[3][3] = ALIVE

    # 1100     0000
    # 0000  => 0000
    # 0000     0000
    # 0011     0000

    # act
    nu = evolve(u)

    # assert
    assert nu[3][2] == 0

def test_canPrintTheUniverse():
    u = makeUniverse(3, 3)
    u[1][1] = 1
    u[1][0] = 1
    u[2][1] = 1
    u[1][2] = 1

    printUniverse(u)
