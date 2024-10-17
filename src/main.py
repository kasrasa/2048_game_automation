import sys
import os
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../utilities'))
if module_path not in sys.path:
    sys.path.append(module_path)


import pyautogui
import numpy as np
import cv2
import time
from utilities.utils import *
from utilities.moves import *
import pyautogui
import time
import numpy as np

# 5 seconds to switch to the game screen
time.sleep(5.0)

# Capture a screenshot of the entire screen
screenshot = pyautogui.screenshot()

# Convert screenshot to a NumPy array for OpenCV
image = np.array(screenshot)

# Convert RGB to BGR for OpenCV
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Main loop
while True:
    grid = get_game_grid()
    best_move = None
    max_score = float('-inf')
    
    # Try all moves and pick the best one using Expectimax
    for move, direction in [('left', move_left), ('right', move_right), ('up', move_up), ('down', move_down)]:
        new_grid = direction(grid)
        if not np.array_equal(grid, new_grid):
            score = expectimax(new_grid, 3)  # Depth can be adjusted
            if score > max_score:
                max_score = score
                best_move = move
    
    # Make the best move
    if best_move:
        press_key(best_move)
    
    # Sleep for a short time before the next move
    time.sleep(0.5)
