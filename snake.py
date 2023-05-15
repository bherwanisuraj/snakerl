import pygame as pg
import sys, time, random

black = pg.Color(0, 0, 0)
green = pg.Color(0, 255, 0)
white = pg.Color(255, 255, 255)
red = pg.Color(255, 0, 0)


class SnakeEnv():

    def __init__(self, window_x, window_y):
        self.window_x = window_x
        self.window_y = window_y
        self.game_window = pg.display.set_mode((window_x, window_y))

        # Reset the Game
        self.reset()

    def reset(self):
        self.game_window.fill(black)
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.food_position = self.spawn_food()
        self.food_spawn = True

        self.direction = "right"
        self.action = self.direction
        self.score = 0
        self.step = 0
        print('Game Reset')

    def changeDirection(self, action, direction):
        if action == 'up' and direction != 'down':
            direction = 'up'

        if action == 'down' and direction != 'up':
            direction = 'down'

        if action == 'right' and direction != 'left':
            direction = 'right'

        if action == 'left' and direction != 'right':
            direction = 'left'

        return direction

    def move(self, direction, snake_position):
        if direction == 'up':
            snake_position[1] -= 10

        if direction == 'down':
            snake_position[1] += 10

        if direction == 'left':
            snake_position[0] -= 10

        if direction == 'right':
            snake_position[0] += 10

        return snake_position

    def spawn_food(self):
        return [random.randrange(1, (self.window_x // 10)) * 10,
                random.randrange(1, (self.window_y // 10)) * 10]

    def eat(self):
        return self.snake_position[0] == self.food_position[0] and self.snake_position[1] == self.food_position[1]

    def human_step(self, event):
        action = None
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                action = 'up'
                print('UP')
            if event.key == pg.K_DOWN:
                action = 'down'
            if event.key == pg.K_LEFT:
                action = 'left'
            if event.key == pg.K_RIGHT:
                action = 'right'
            if event.key == pg.K_ESCAPE:
                pg.event.post(pg.event.Event(pg.QUIT))

        return action

    def scoreKeeper(self, color, font, size):
        score_font = pg.font.SysFont(font, size)
        scoreArea = score_font.render('Score: ' + str(self.score), True, color)
        scoreRect = scoreArea.get_rect()
        scoreRect.midtop = (self.window_x / 10, 15)
        self.game_window.blit(scoreArea, scoreRect)

    def gameOver(self):
        if self.snake_position[0] < 0 or self.snake_position[0] > self.window_x - 10:
            self.endGame()
        if self.snake_position[1] < 0 or self.snake_position[1] > self.window_y - 10:
            self.endGame()

        for block in self.snake_body[1:]:
            if self.snake_position[0] == block[0] and self.snake_position[1] == block[1]:
                self.endGame()

    def endGame(self):
        message = pg.font.SysFont('arial', 45)
        messageArea = message.render('Game Over', True, red)
        messageRect = messageArea.get_rect()
        messageRect.midtop = (self.window_x / 2, self.window_y / 4)

        self.game_window.fill(black)
        self.game_window.blit(messageArea, messageRect)
        self.scoreKeeper(red, 'times', 20)
        pg.display.flip()
        time.sleep(3)
        pg.quit()
        sys.exit()
