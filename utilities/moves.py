import random
import numpy as np

# Helper function to move tiles in a direction
def move_left(grid):
    new_grid = np.zeros((4, 4))
    for row in range(4):
        tiles = [num for num in grid[row] if num != 0]
        new_tiles = []
        i = 0
        while i < len(tiles):
            if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
                new_tiles.append(tiles[i] * 2)
                i += 2
            else:
                new_tiles.append(tiles[i])
                i += 1
        new_grid[row][:len(new_tiles)] = new_tiles
    return new_grid

def move_right(grid):
    return np.fliplr(move_left(np.fliplr(grid)))

def move_up(grid):
    return np.transpose(move_left(np.transpose(grid)))

def move_down(grid):
    return np.transpose(move_right(np.transpose(grid)))
