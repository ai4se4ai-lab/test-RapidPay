# main.py
# This is the entry point for the Snake game.

from game import Game

if __name__ == "__main__":
    # TODO: Consider adding a more robust game manager or orchestrator here if the game grows.
    snake_game = Game()
    snake_game.run()