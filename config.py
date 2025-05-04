# config.py
# This file holds game configuration constants.

# FIXME: These are magic numbers - should be more descriptive or part of a settings object
SNAKE_BLOCK_SIZE = 20
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 480
SNAKE_SPEED = 15

# FIXME: Use proper color constants module or enum for better readability and maintainability
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)  # Unused color - dead code? REMOVE if not needed