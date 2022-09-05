"""
Inspired by: https://www.youtube.com/watch?v=bfRwxS5d0SI&list=RDCMUC4SVo0Ue36XCfOyb5Lh1viQ&start_radio=1
The changes that were made to the original tutorial were put as comments in this module and in the modules
Game and Snake.
"""

from tkinter import *
from code_files import Game, Snake

# constants
GAME_WIDTH = 500
GAME_HEIGHT = 500
SPEED = 150                          # speed of the game.
SPACE_SIZE = 40                     # the size of objects in the game.
BODY_PARTS = 3                      # the number of body-parts of the snake.
SNAKE_COLOR = "#C32323"
FOOD_COLOR = "#3519E5"
BACKGROUND_COLOR = "#000000"        # game background.


# variables
score = 0
direction = 'down'


# in the original tutorial there was no main method, but we added it so that we can run the game as a subprogram.
def main():
    # creating window.
    window = Tk()
    window.title('Snake game')

    # score label.
    label = Label(window, text='Score:{}'.format(score), font=('arial', 40))
    label.pack()

    # creating a canvas.
    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

    # centering the window.
    window.update()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # defining keys.
    window.bind("<Left>", lambda event: change_direction_helper('left'))
    window.bind("<Right>", lambda event: change_direction_helper('right'))
    window.bind("<Up>", lambda event: change_direction_helper('up'))
    window.bind("<Down>", lambda event: change_direction_helper('down'))



    snake = Snake.Snake(BODY_PARTS)
    reset_directionAndCoordinates(snake)

    # creating body-parts. this was put in the class Snake in the tutorial, but we put it here so that the class can
    # be testable.
    for x, y in snake.coordinates:
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
        snake.squares.append(square)

    food = Snake.Food(GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE, canvas, FOOD_COLOR)

    next_turn(snake, food, canvas, window, label)

    window.resizable(False, False)  # make window un-resizable.
    window.mainloop()


def reset_directionAndCoordinates(snake):
    # resetting the head-coordinates after the game is restarted.
    snake.coordinates[0] = 0, 0
    # resetting the direction after the game is restarted.
    global direction
    start_direction = 'down'
    direction = start_direction


# this was not in the tutorial, but we added it so that we can put change_direction in another module.
def change_direction_helper(new_direction):
    global direction
    returned_direction = Game.change_direction(direction, new_direction)

    direction = returned_direction


# in the tutorial there was some extra code in this function, but we put the code in other functions,
# so that we can test it, and so that the function is not too large.
def next_turn(snake, food, canvas, window, label):

    x, y = Game.calculate_new_coordinates(snake, direction, SPACE_SIZE)

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    # check when head if snack overlap with food.
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))

        canvas.delete("food")
        food = Snake.Food(GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE, canvas, FOOD_COLOR)
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if Game.check_collisions(snake, GAME_WIDTH, GAME_HEIGHT):
        Game.game_over(canvas)

    else:
        window.after(SPEED, next_turn, snake, food, canvas, window, label)


if __name__ == '__main__':
    main()
