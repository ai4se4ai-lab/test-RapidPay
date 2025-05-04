# display.py
# This file handles Pygame initialization and rendering functions.

import pygame
from config import DISPLAY_WIDTH, DISPLAY_HEIGHT, SNAKE_BLOCK_SIZE, BLUE, GREEN, RED

def initialize_display():
    pygame.init()
    game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption('A Very Debt-Ridden Snake Game')
    return game_display

# FIXME: This utility function is still somewhat coupled to display dimensions
def message(display, msg, color):
    font_style = pygame.font.SysFont(None, 30) # Magic number for font size
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [DISPLAY_WIDTH / 6, DISPLAY_HEIGHT / 3]) # More magic numbers for positioning

def draw_snake(display, snake_block_size, snake_list):
    for segment in snake_list:
        pygame.draw.rect(display, GREEN, [segment[0], segment[1], snake_block_size, snake_block_size]) # Magic number passed

def draw_food(display, foodx, foody):
    pygame.draw.rect(display, RED, [foodx, foody, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE]) # Magic number from config