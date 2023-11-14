import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")

# Grid
grid = np.random.randint(2, size=(ROWS, COLS))

def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                pygame.draw.rect(screen, WHITE, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def update_grid():
    global grid
    new_grid = grid.copy()
    for row in range(ROWS):
        for col in range(COLS):
            state = grid[row][col]
            neighbours = np.sum(grid[row-1:row+2, col-1:col+2]) - state
            if state == 0 and neighbours == 3:
                new_grid[row][col] = 1
            elif state == 1 and (neighbours < 2 or neighbours > 3):
                new_grid[row][col] = 0
    grid = new_grid

# Game loop
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_grid()
    update_grid()
    pygame.display.update()
    pygame.time.delay(100)

pygame.quit()
