# main.py

from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from snake_game import SnakeGame
from gesture_input import GestureInput
import pygame

def main():
    pygame.init()
    game = SnakeGame()
    gesture_input = GestureInput(WINDOW_WIDTH, WINDOW_HEIGHT)
    game.run(gesture_input)

if __name__ == "__main__":
    main()
