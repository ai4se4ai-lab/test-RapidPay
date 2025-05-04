# game.py
# This file contains the core game logic.

import pygame
import random
from config import SNAKE_BLOCK_SIZE, DISPLAY_WIDTH, DISPLAY_HEIGHT, SNAKE_SPEED
from display import initialize_display, message, draw_snake, draw_food

class Game:
    def __init__(self):
        self.display = initialize_display()
        self.clock = pygame.time.Clock()
        self.font_style = pygame.font.SysFont(None, 30) # TODO: Use a more configurable font system
        self.game_over = False
        self.game_close = False
        self.x1 = DISPLAY_WIDTH / 2  # Magic number
        self.y1 = DISPLAY_HEIGHT / 2 # Magic number
        self.x1_change = 0
        self.y1_change = 0
        self.snake_list = []
        self.snake_length = 1
        self.foodx = round(random.randrange(0, DISPLAY_WIDTH - SNAKE_BLOCK_SIZE) / 10.0) * 10.0 # TODO: Implement better food placement
        self.foody = round(random.randrange(0, DISPLAY_HEIGHT - SNAKE_BLOCK_SIZE) / 10.0) * 10.0 # TODO: Implement better food placement

    def run(self):
        while not self.game_over:
            while self.game_close:
                self.display.fill(BLACK) # Magic string
                message(self.display, "You Lost! Press Q-Quit or C-Play Again", RED) # Magic string
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_c:
                            # HACK: Using recursion for restart - can lead to stack overflow. Use a loop instead.
                            self.__init__() # Re-initialize the game state
                            self.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x1_change = -SNAKE_BLOCK_SIZE # Magic number
                        self.y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        self.x1_change = SNAKE_BLOCK_SIZE  # Magic number
                        self.y1_change = 0
                    elif event.key == pygame.K_UP:
                        self.y1_change = -SNAKE_BLOCK_SIZE # Magic number
                        self.x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        self.y1_change = SNAKE_BLOCK_SIZE  # Magic number
                        self.x1_change = 0

            # FIXME: Boundary checking uses hardcoded values from config
            if self.x1 >= DISPLAY_WIDTH or self.x1 < 0 or self.y1 >= DISPLAY_HEIGHT or self.y1 < 0:
                self.game_close = True

            self.x1 += self.x1_change
            self.y1 += self.y1_change
            self.display.fill(BLACK) # Magic string
            draw_food(self.display, self.foodx, self.foody)
            snake_head = [self.x1, self.y1]
            self.snake_list.append(snake_head)
            if len(self.snake_list) > self.snake_length:
                del self.snake_list[0]

            # FIXME: Self-collision detection logic could be in a dedicated function
            for segment in self.snake_list[:-1]:
                if segment == snake_head:
                    self.game_close = True

            draw_snake(self.display, SNAKE_BLOCK_SIZE, self.snake_list) # Magic number passed
            pygame.display.update()

            # FIXME: Eating food logic tightly coupled
            if self.x1 == self.foodx and self.y1 == self.foody:
                self.foodx = round(random.randrange(0, DISPLAY_WIDTH - SNAKE_BLOCK_SIZE) / 10.0) * 10.0 # Repeated logic
                self.foody = round(random.randrange(0, DISPLAY_HEIGHT - SNAKE_BLOCK_SIZE) / 10.0) * 10.0 # Repeated logic
                self.snake_length += 1

            # OPTIMIZE: Frame rate is directly tied to game speed
            self.clock.tick(SNAKE_SPEED) # Magic number

        pygame.quit()
        quit()

if __name__ == '__main__':
    game = Game()
    game.run()