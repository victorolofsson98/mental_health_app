# inspired by: https://www.youtube.com/watch?v=bfRwxS5d0SI&list=RDCMUC4SVo0Ue36XCfOyb5Lh1viQ&start_radio=1
from tkinter import *


# in the tutorial this was a part of the function next_turn, but we put it here so that we can test it separately.
def calculate_new_coordinates(snake, direction, SPACE_SIZE):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE

    return x, y



def check_collisions(snake, GAME_WIDTH, GAME_HEIGHT):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False



def change_direction(direction, new_direction):

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

    return direction



def game_over(canvas):
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('arial', 70),
                       text="GAME OVER", fill='red', tag="gameover")
