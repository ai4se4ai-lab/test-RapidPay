import pygame
import random

# Initialize Pygame (it's good practice to have this at the top)
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Snake:
    def __init__(self, grid_size, width, height):
        self.grid_size = grid_size
        self.width = width
        self.height = height
        self.body = [(width // 2, height // 2)]  # Initial snake position (list of coordinates)
        self.direction = (1, 0)  # Initial direction: right
        self.color = GREEN
        self.grow_snake = False

    def move(self):
        if self.grow_snake:
            self.body.append(self.body[-1])  # Add a new segment at the tail's previous position
            self.grow_snake = False

        new_head_x = self.body[0][0] + self.direction[0] * self.grid_size
        new_head_y = self.body[0][1] + self.direction[1] * self.grid_size
        new_head = (new_head_x, new_head_y)
        self.body.insert(0, new_head)
        self.body.pop()  # Remove the last segment to maintain length (unless growing)

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, self.color, (segment[0], segment[1], self.grid_size, self.grid_size))

    def get_head_position(self):
        return self.body[0]

    def check_collision(self):
        head_x, head_y = self.get_head_position()
        # Collision with walls
        if not (0 <= head_x < self.width and 0 <= head_y < self.height):
            return True
        # Collision with self
        if len(self.body) > 1 and self.get_head_position() in self.body[1:]:
            return True
        return False

class Food:
    def __init__(self, grid_size, width, height):
        self.grid_size = grid_size
        self.width = width
        self.height = height
        self.position = self.place_randomly()
        self.color = RED

    def place_randomly(self):
        x = random.randrange(0, self.width // self.grid_size) * self.grid_size
        y = random.randrange(0, self.height // self.grid_size) * self.grid_size
        return (x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], self.grid_size, self.grid_size))

class Game:
    def __init__(self, width=600, height=480, grid_size=20):
        pygame.init()
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.grid_size, self.width, self.height)
        self.food = Food(self.grid_size, self.width, self.height)
        self.score = 0

    def place_food(self):
        while True:
            self.food.position = self.food.place_randomly()
            if self.food.position not in self.snake.body:
                break

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != (0, 1):
                        self.snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                        self.snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                        self.snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                        self.snake.change_direction((1, 0))

            self.snake.move()

            # Check for collision with food
            if self.snake.get_head_position() == self.food.position:
                self.score += 1
                self.snake.grow_snake = True  # Set the flag to grow the snake in the next move
                self.place_food()

            if self.snake.check_collision():
                running = False
                print(f"Game Over! Score: {self.score}")

            self.display.fill(BLACK)
            self.food.draw(self.display)
            self.snake.draw(self.display)
            pygame.display.flip()

            self.clock.tick(10)  # Control the game speed

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()