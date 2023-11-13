import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random


# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction

# iter_number = 10000
# iter = 0
# size_x = 10
# size_y = 10
# array = np.random.randint(2, size=(size_x, size_y))
# # array = [[0, 0, 0], [1, 1, 0],[0, 0, 0]]


# # while iter < iter_number:
# while True:
#     iter += 1
#     print(f"Iteration {iter}\n============")
#     print(array)

#     for x in range(1, size_x - 1):
#         for y in range(1, size_y - 1):
#             living_cell = bool(array[x][y])
#             living_neighbours = 0
#             for x1 in range(-1, 2):
#                 for y1 in range(-1, 2):
#                     if (x1, y1) == (0, 0): continue
#                     living_neighbours += array[x + x1][y + y1]


#             if living_cell:
#                 if living_neighbours not in range(2, 4):
#                     array[x][y] = 0
#             else:
#                 if living_neighbours == 3:
#                     array[x][y] = 1

#     input()


def draw_array(array, size_x, size_y):
    print(array)

    # Set up the figure and axis for drawing
    fig, ax = plt.subplots()
    ax.set_xlim([0, size_y + 2])
    ax.set_ylim([0, size_x + 2])
    ax.set_xticks(np.arange(0, size_y + 2, 1))
    ax.set_yticks(np.arange(0, size_x + 2, 1))
    ax.grid(which='both')

    # Create a matrix of rectangle objects
    rect_matrix = np.empty((size_x + 2, size_y + 2), dtype=object)
    for i in range(size_x + 2):
        for j in range(size_y + 2):
            rect_color = 'black' if array[i, j] == 1 else 'white'
            rect_matrix[i, j] = plt.Rectangle([j, i], 1, 1, edgecolor='black', facecolor=rect_color)
            # rect_matrix[i, j] = plt.Rectangle([j, i], 1, 1, edgecolor='black', facecolor='white')
            ax.add_patch(rect_matrix[i, j])

    plt.gca().invert_yaxis()  # Invert Y axis so that (0,0) is at the top left

    def next_generation():
        array_copy = array.copy()
        for x in range(1, size_x + 1):
            for y in range(1, size_y + 1):
                living_cell = bool(array_copy[x][y])
                living_neighbours = 0
                for x1 in range(-1, 2):
                    for y1 in range(-1, 2):
                        if (x1, y1) == (0, 0): continue
                        living_neighbours += array_copy[x + x1][y + y1]
                changed = False
                if living_cell:
                    if living_neighbours not in range(2, 4):
                        array[x][y] = 0
                        changed = True
                else:
                    if living_neighbours == 3:
                        array[x][y] = 1
                        changed = True
                if changed == False: array[x, y] = array_copy[x, y]

                # if living_cell:
                #     if living_neighbours not in range(2, 4):
                #         array[x][y] = 0
                # elif living_neighbours == 3:
                #         array[x][y] = 1
                # else: array[x, y] = array_copy[x, y]

    def update(frame):
        next_generation()
        for x in range(1, size_x):
            for y in range(1, size_y):
                color = 'black' if array[x, y] == 1 else 'white'
                rect_matrix[x, y].set_facecolor(color)
        return rect_matrix.flatten()

    ani = FuncAnimation(fig, update, frames=10, interval=1000, blit=True)
    plt.show()


def create_array(size_x, size_y):
    temp_array = np.random.randint(2, size=(size_x, size_y))
    padded_array = np.pad(temp_array, pad_width=1, mode='constant', constant_values=0)
    return padded_array


def swap_arrays(array1, array2):
    temp_array = array1
    array1 = array2
    array2 = temp_array


size_x = 5
size_y = 5

array = create_array(size_x, size_y)
draw_array(array, size_x, size_y)