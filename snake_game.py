import pygame
import random
from settings import *

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Gesture Controlled Snake")
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        start_x = WINDOW_WIDTH // 2
        start_y = WINDOW_HEIGHT // 2
        self.snake = [
            (start_x, start_y),
            (start_x - CELL_SIZE, start_y),
            (start_x - 2*CELL_SIZE, start_y)
        ]
        self.direction = DIR_RIGHT
        self.score = 0
        self.place_food()
        self.game_over = False

    def place_food(self):
        grid_w = WINDOW_WIDTH  // CELL_SIZE
        grid_h = WINDOW_HEIGHT // CELL_SIZE
        food_x = random.randint(0, grid_w - 1) * CELL_SIZE
        food_y = random.randint(0, grid_h - 1) * CELL_SIZE
        while (food_x, food_y) in self.snake:
            food_x = random.randint(0, grid_w - 1) * CELL_SIZE
            food_y = random.randint(0, grid_h - 1) * CELL_SIZE
        self.food = (food_x, food_y)

    def update(self):
        if self.game_over:
            return

        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx * CELL_SIZE, head_y + dy * CELL_SIZE)

        # collision with wall
        if (new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH or
            new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT):
            self.game_over = True
            return

        # collision with self
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()

    def draw(self):
        self.screen.fill(BG_COLOR)
        # draw food
        pygame.draw.rect(self.screen, FOOD_COLOR,
                         pygame.Rect(self.food[0], self.food[1],
                                     CELL_SIZE, CELL_SIZE))
        # draw snake
        for seg in self.snake:
            pygame.draw.rect(self.screen, SNAKE_COLOR,
                             pygame.Rect(seg[0], seg[1], CELL_SIZE, CELL_SIZE))
        # draw score
        font = pygame.font.SysFont(None, 30)
        score_surf = font.render(f"Score: {self.score}", True, (255,255,255))
        self.screen.blit(score_surf, (5,5))

        pygame.display.flip()

    def set_direction(self, new_dir):
        opposite = (-self.direction[0], -self.direction[1])
        if new_dir != opposite:
            self.direction = new_dir

    def run(self, gesture_input):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if self.game_over:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r or event.key == pygame.K_SPACE:
                            self.reset()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.reset()
                # else: you could process keyboard movement fallback here

            if not self.game_over:
                dir_from_gesture = gesture_input.get_direction()
                if dir_from_gesture:
                    self.set_direction(dir_from_gesture)
                self.update()

            self.draw()

            if self.game_over:
                font_big = pygame.font.SysFont(None, 60)
                font_small = pygame.font.SysFont(None, 40)

                msg1 = font_big.render("GAME OVER!", True, (255, 0, 0))
                msg2 = font_small.render("Press SPACE or Click to Restart", True, (255, 255, 255))

                rect1 = msg1.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 30))
                rect2 = msg2.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 30))

                self.screen.blit(msg1, rect1)
                self.screen.blit(msg2, rect2)
                pygame.display.flip()

                self.clock.tick(5)
            else:
                self.clock.tick(SNAKE_SPEED)
