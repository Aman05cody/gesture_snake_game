# gesture_input.py

import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, MOUSE_MOVE_THRESHOLD, DIR_UP, DIR_DOWN, DIR_LEFT, DIR_RIGHT

class GestureInput:
    def __init__(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, threshold=MOUSE_MOVE_THRESHOLD):
        self.width  = width
        self.height = height
        self.threshold = threshold
        self.last_pos = None
        self.last_direction = None

    def update_mouse_pos(self):
        return pygame.mouse.get_pos()

    def get_direction(self):
        pos = self.update_mouse_pos()

        if self.last_pos is None:
            self.last_pos = pos
            return self.last_direction

        dx = pos[0] - self.last_pos[0]
        dy = pos[1] - self.last_pos[1]

        direction = None
        # decide based on larger movement
        if abs(dx) > abs(dy):
            if dx > self.threshold:
                direction = DIR_RIGHT
            elif dx < -self.threshold:
                direction = DIR_LEFT
        else:
            if dy > self.threshold:
                direction = DIR_DOWN
            elif dy < -self.threshold:
                direction = DIR_UP

        # update
        if direction:
            self.last_direction = direction
            self.last_pos = pos

        return self.last_direction
