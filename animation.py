import pygame
import sys
import numpy as np

width, height = 800, 600


def next_generation(array):
    size_x = len(array) - 2
    size_y = len(array[0]) - 2
    array_copy = array.copy()
    for x in range(1, size_x + 1):
        for y in range(1, size_y + 1):
            living_cell = bool(array_copy[x][y])
            living_neighbours = 0
            for x1 in range(-1, 2):
                for y1 in range(-1, 2):
                    if (x1, y1) == (0, 0): continue
                    living_neighbours += array_copy[x + x1][y + y1]

            if living_cell:
                if living_neighbours not in range(2, 4):
                    array[x][y] = 0
            elif living_neighbours == 3:
                array[x][y] = 1
            else:
                array[x, y] = array_copy[x, y]


def create_array(cols, rows):
    temp_array = np.random.randint(2, size=(cols, rows))
    padded_array = np.pad(temp_array, pad_width=1, mode='constant', constant_values=0)
    return padded_array


def run(screen, array):
    cols = len(array) - 2
    rows = len(array[0]) - 2
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                # Update the window size
                width1, height1 = event.size
                screen = pygame.display.set_mode((width1, height1), pygame.RESIZABLE)

        rect_width = width // cols
        rect_height = height // rows

        next_generation(array)

        # Draw the rectangles
        for row in range(rows):
            for col in range(cols):
                color = WHITE if array[col][row] == 0 else BLACK
                pygame.draw.rect(screen, color, (col * rect_width, row * rect_height, rect_width, rect_height))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(10)  # Adjust the number to make the animation faster or slower

    # Quit Pygame
    pygame.quit()
    sys.exit()


# Initialize Pygame
pygame.init()

# Set up the initial display

scr = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Resizable Animated Chessboard")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Set up the clock
clock = pygame.time.Clock()
run(scr, create_array(80, 60))
