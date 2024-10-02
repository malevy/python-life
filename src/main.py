import pygame
from universe import Universe

ROWS: int = 30
COLUMNS: int = 50
CELL_HEIGHT_PIXELS: int = 10
CELL_WIDTH_PIXELS: int = 10


def renderCellCallback(row: int, column: int, state: bool):
    """
    Callback to use with Universe.visit to render the universe onto a screen.

    :param row: the row index of the cell
    :param column: the column index of the cell
    :param state: the state of the cell (True is alive, False is dead)
    """
    x = column * CELL_WIDTH_PIXELS
    y = row * CELL_HEIGHT_PIXELS
    color = "black" if state else "white"
    pygame.draw.rect(screen, color, (x, y, CELL_WIDTH_PIXELS, CELL_HEIGHT_PIXELS))


pygame.init()

# setup screen
screen = pygame.display.set_mode(
    (COLUMNS * CELL_WIDTH_PIXELS, ROWS * CELL_HEIGHT_PIXELS)
)

u: Universe = Universe(ROWS, COLUMNS)

running = True
while running:
    screen.fill("white")

    # update the screen with a black square for each live cell
    u.visit(renderCellCallback, True)

    # update the screen with the new rendering
    pygame.display.flip()

    # is the user trying to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.wait(250)

    u.evolve()

pygame.quit()
