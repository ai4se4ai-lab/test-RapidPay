# RapidPay Snake Game

A classic snake game implemented using Pygame.

## Overview

This is a simple and fun snake game where the player controls a snake to eat food, grow longer, and avoid colliding with the walls or its own body. The game features:

* A controllable snake that moves on a grid.
* Randomly generated food items.
* Scoring based on the amount of food eaten.
* Game over conditions for wall and self-collision.

## Getting Started

### Prerequisites

* **Python 3.x** installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
  
    ```bash
    C:\Users\<USERNAME>\AppData\Local\Programs\Python\Python312\python.exe -m venv myenv

    myenv\Scripts\activate
    ```

* **Pygame** library installed. You can install it using pip:

    ```bash
    pip install pygame
    ```

### Running the Game

1.  **Clone or download** the repository containing the game files (`main.py` and `game.py`).
2.  **Navigate** to the directory where the files are located in your terminal or command prompt.
3.  **Run the game** using the following command:

    ```bash
    python main.py
    ```

## How to Play

* Use the **arrow keys** (Up, Down, Left, Right) to control the direction of the snake.
* The snake will move continuously in the chosen direction.
* Guide the snake to eat the **red food** blocks.
* Each time the snake eats food, it will **grow longer**, and your **score will increase**.
* The game ends if the snake collides with the **walls** of the game window or with its **own body**.
* The final score will be displayed in the console when the game ends.

## Game Structure

The game consists of the following main files:

* **`main.py`**: This file is the entry point of the game. It initializes the Pygame environment and runs the main game loop through the `Game` class.
* **`game.py`**: This file contains the core logic of the game, including:
    * The `Snake` class, which handles the snake's movement, growth, direction changes, and collision detection.
    * The `Food` class, which manages the placement and drawing of the food.
    * The `Game` class, which sets up the game window, manages the game loop, handles events, and updates the game state.

## Contributing

Contributions to the RapidPay Snake Game are welcome! If you have ideas for improvements, new features, or bug fixes, feel free to:

1.  **Fork** the repository.
2.  **Create a new branch** for your changes.
3.  **Make your modifications** and commit them.
4.  **Push** your changes to your fork.
5.  **Submit a pull request** to the main repository.

## License

This project is open-source and available under the [MIT License](LICENSE) (Add your license file if you have one).

## Acknowledgements

* Pygame for providing the necessary tools for creating this game.
* The Pygame community for their helpful resources and support.