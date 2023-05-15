from snake import SnakeEnv
import pygame as pg

snakeEnv = SnakeEnv(600, 600)
difficulty = 10
fps = pg.time.Clock()
check_errors = pg.init()
pg.display.set_caption("Snake Game")
black = pg.Color(0, 0, 0)
green = pg.Color(0, 255, 0)
white = pg.Color(255, 255, 255)
red = pg.Color(255, 0, 0)

while True:
    for event in pg.event.get():
        snakeEnv.action = snakeEnv.human_step(event)

    #check Direction
    snakeEnv.direction = snakeEnv.changeDirection(snakeEnv.action, snakeEnv.direction)
    snakeEnv.snake_position = snakeEnv.move(snakeEnv.direction, snakeEnv.snake_position)

    #Check if we at food
    snakeEnv.snake_body.insert(0, list(snakeEnv.snake_position))
    if snakeEnv.eat():
        snakeEnv.score +=1
        snakeEnv.food_spawn = False
    else:
        snakeEnv.snake_body.pop()

    #Check if spawn new food
    if not snakeEnv.food_spawn:
        snakeEnv.food_position = snakeEnv.spawn_food()
    snakeEnv.food_spawn = True

    #Drawing the snake
    snakeEnv.game_window.fill(black)
    for position in snakeEnv.snake_body:
        pg.draw.rect(snakeEnv.game_window, green, pg.Rect(position[0], position[1], 10, 10))


