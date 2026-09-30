import pygame
import numpy as np
import time

# -----------------------------
# Settings
# -----------------------------

WIDTH = 800
HEIGHT = 800

GRID_SIZE = 1000

# Time between generations
DELAY = 0.15

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1000 × 1000 Cellular Automaton")

# 1000 x 1000 grid
grid = np.random.choice(
    [0, 1],
    size=(GRID_SIZE, GRID_SIZE),
    p=[0.9, 0.1]
)

running = True

while running:

    # Handle closing window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -----------------------------
    # Draw grid
    # -----------------------------

    # Resize 1000x1000 -> 800x800
    display_grid = pygame.surfarray.make_surface(
        np.repeat(np.repeat(grid, 1, axis=0), 1, axis=1)
    )

    display_grid = pygame.transform.scale(
        display_grid,
        (WIDTH, HEIGHT)
    )

    screen.blit(display_grid, (0, 0))

    pygame.display.flip()

    # -----------------------------
    # Next generation
    # -----------------------------

    neighbors = (
        np.roll(grid, 1, axis=0) +
        np.roll(grid, -1, axis=0) +
        np.roll(grid, 1, axis=1) +
        np.roll(grid, -1, axis=1) +
        np.roll(np.roll(grid, 1, axis=0), 1, axis=1) +
        np.roll(np.roll(grid, 1, axis=0), -1, axis=1) +
        np.roll(np.roll(grid, -1, axis=0), 1, axis=1) +
        np.roll(np.roll(grid, -1, axis=0), -1, axis=1)
    )

    # Conway's Game of Life rules
    grid = (
        ((grid == 1) & ((neighbors == 2) | (neighbors == 3))) |
        ((grid == 0) & (neighbors == 3))
    ).astype(np.uint8)

    time.sleep(DELAY)

pygame.quit()
