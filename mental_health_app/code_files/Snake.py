# inspired by: https://www.youtube.com/watch?v=bfRwxS5d0SI&list=RDCMUC4SVo0Ue36XCfOyb5Lh1viQ&start_radio=1

import random

# this is almost the same as the tutorial, but we removed the gui functionality, so that we can test the class.
class Snake:
    def __init__(self, BODY_PARTS):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # list of coordinates.
        for i in range(0, BODY_PARTS):
            """initial coordinates for each body-part is 0,0. so that the snake appear at the top left when the 
            game starts."""
            self.coordinates.append([0, 0])


class Food:
    def __init__(self, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE, canvas, FOOD_COLOR):
        x, y = get_coordinates(GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE)
        self.coordinates = [x, y]

        # viewing the food.
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


# in the tutorial, this was in the class Food, put we put it as a separate function so that we can test it.
def get_coordinates(GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE):

    # creating food at random places.
    x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
    y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

    return x, y