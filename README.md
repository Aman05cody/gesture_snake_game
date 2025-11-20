# 🐍 Gesture Controlled Snake Game 🎮

A classic Snake game controlled by mouse gestures, built with Python 🐍 and Pygame.

## ✨ Features
- 👆 **Gesture Control:** Control the snake's direction by moving your mouse.
- 🍎 **Classic Gameplay:** Eat food to grow longer and increase your score.
- 💥 **Collision Detection:** The game ends if you hit a wall or yourself.
- 🔄 **Simple Restart:** Easily restart the game with a keypress (`SPACE` or `R`) or a mouse click.
- 🔧 **Configurable:** Adjust game settings like speed, colors, and window size in `settings.py`.

## 🚀 Quick Start

1.  **Install Dependencies** 📦
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Game** ▶️
    ```bash
    python snake_game.py
    ```

## 🕹️ Controls

- **Move Snake** 🐍: Move your mouse in the desired direction (Up, Down, Left, or Right).
- **Restart Game** 🔁: After a "Game Over", press `SPACE`, `R`, or click the mouse to play again.

## ⚙️ Configuration

You can customize the game by editing the `settings.py` file:

- 🖼️ `WINDOW_WIDTH`, `WINDOW_HEIGHT`: Game window size.
- 📏 `CELL_SIZE`: Size of the snake and food.
- ⚡ `SNAKE_SPEED`: Game speed (frames per second).
- 🎨 `SNAKE_COLOR`, `FOOD_COLOR`, `BG_COLOR`: Game colors.
- 🖱️ `MOUSE_MOVE_THRESHOLD`: Sensitivity for gesture detection.

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License.