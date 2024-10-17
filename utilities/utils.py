from utilities.moves import *
import pyautogui

# Expectimax function
def expectimax(grid, depth):
    if depth == 0 or is_game_over(grid):
        return evaluate_grid(grid)

    # Player's turn (maximize score)
    if depth % 2 == 0:
        max_score = float('-inf')
        for move in [move_left, move_right, move_up, move_down]:
            new_grid = move(grid)
            if not np.array_equal(grid, new_grid):  # Check if the move changed the grid
                score = expectimax(new_grid, depth - 1)
                max_score = max(max_score, score)
        return max_score

    # Computer's turn (random tile placement, expect average score)
    else:
        empty_tiles = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
        if not empty_tiles:
            return evaluate_grid(grid)

        avg_score = 0
        for i, j in empty_tiles:
            new_grid = np.copy(grid)
            new_grid[i][j] = 2
            avg_score += 0.9 * expectimax(new_grid, depth - 1)
            new_grid[i][j] = 4
            avg_score += 0.1 * expectimax(new_grid, depth - 1)
        return avg_score / len(empty_tiles)

# Evaluation function (this can be made more sophisticated)
def evaluate_grid(grid):
    return np.sum(grid)  # Simple heuristic: sum of the grid's values

# Check if the game is over
def is_game_over(grid):
    if 0 in grid:
        return False
    for move in [move_left, move_right, move_up, move_down]:
        if not np.array_equal(grid, move(grid)):
            return False
    return True



# Function to simulate key presses
def press_key(move):
    pyautogui.press(move)

# Function to get the game grid (in reality, you'd use image processing here)
def get_game_grid(image):
    return np.array([[2, 4, 8, 16],
                     [32, 64, 128, 256],
                     [512, 1024, 2048, 0],
                     [0, 0, 0, 0]])
