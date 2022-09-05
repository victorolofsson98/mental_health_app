import unittest

<<<<<<< HEAD:unit_tests/test_game.py
from code_files import Game
from code_files import Snake
import code_files.Game
import code_files.Snake
=======
import Game
import Snake
>>>>>>> df82b746d834b40e2d91f22ce0ae1966fe07e6d7:code_files/test_game.py


class TestDaily(unittest.TestCase):

    def test_change_direction_left(self):
        result = Game.change_direction('left', 'left')
        self.assertEqual(result, 'left')

        result = Game.change_direction('left', 'right')
        self.assertEqual(result, 'left')

        result = Game.change_direction('left', 'up')
        self.assertEqual(result, 'up')

        result = Game.change_direction('left', 'down')
        self.assertEqual(result, 'down')

    def test_change_direction_right(self):
        result = Game.change_direction('right', 'left')
        self.assertEqual(result, 'right')

        result = Game.change_direction('right', 'right')
        self.assertEqual(result, 'right')

        result = Game.change_direction('right', 'up')
        self.assertEqual(result, 'up')

        result = Game.change_direction('right', 'down')
        self.assertEqual(result, 'down')

    def test_change_direction_up(self):
        result = Game.change_direction('up', 'left')
        self.assertEqual(result, 'left')

        result = Game.change_direction('up', 'right')
        self.assertEqual(result, 'right')

        result = Game.change_direction('up', 'up')
        self.assertEqual(result, 'up')

        result = Game.change_direction('up', 'down')
        self.assertEqual(result, 'up')

    def test_change_direction_down(self):
        result = Game.change_direction('down', 'left')
        self.assertEqual(result, 'left')

        result = Game.change_direction('down', 'right')
        self.assertEqual(result, 'right')

        result = Game.change_direction('down', 'up')
        self.assertEqual(result, 'down')

        result = Game.change_direction('down', 'down')
        self.assertEqual(result, 'down')

    def test_calculate_new_coordinates_up(self):
        snake_id = Snake.Snake(BODY_PARTS=3)
        x, y = Game.calculate_new_coordinates(snake_id, 'up', SPACE_SIZE=40)
        y_comp = -40

        self.assertEqual(x, 0)
        self.assertEqual(y, y_comp)

    def test_calculate_new_coordinates_down(self):
        snake_id = Snake.Snake(BODY_PARTS=3)
        x, y = Game.calculate_new_coordinates(snake_id, 'down', SPACE_SIZE=40)
        y_comp = 40

        self.assertEqual(x, 0)
        self.assertEqual(y, y_comp)

    def test_calculate_new_coordinates_left(self):
        snake_id = Snake.Snake(BODY_PARTS=3)
        x, y = Game.calculate_new_coordinates(snake_id, 'left', SPACE_SIZE=40)
        x_comp = -40

        self.assertEqual(x, x_comp)
        self.assertEqual(y, 0)

    def test_calculate_new_coordinates_right(self):
        snake_id = Snake.Snake(BODY_PARTS=3)
        x, y = Game.calculate_new_coordinates(snake_id, 'right', SPACE_SIZE=40)
        x_comp = 40

        self.assertEqual(x, x_comp)
        self.assertEqual(y, 0)

    def test_check_collisions_side_right(self):
        snake_id = Snake.Snake(BODY_PARTS=3)
        snake_id.coordinates[0] = [500, 0]
        wall_bump = Game.check_collisions(snake_id, GAME_WIDTH=500, GAME_HEIGHT=500)

        self.assertTrue(wall_bump)

    def test_check_collisions_side_left(self):
        snake_id = Snake.Snake(BODY_PARTS=3)
        snake_id.coordinates[0] = [-1, 0]
        wall_bump = Game.check_collisions(snake_id, GAME_WIDTH=500, GAME_HEIGHT=500)

        self.assertTrue(wall_bump)

    def test_check_collisions_side_down(self):
        snake_id = Snake.Snake(BODY_PARTS=3)
        snake_id.coordinates[0] = [0, 500]
        wall_bump = Game.check_collisions(snake_id, GAME_WIDTH=500, GAME_HEIGHT=500)

        self.assertTrue(wall_bump)

    def test_check_collisions_side_top(self):
        snake_id = Snake.Snake(BODY_PARTS=3)
        snake_id.coordinates[0] = [0, -1]
        wall_bump = Game.check_collisions(snake_id, GAME_WIDTH=500, GAME_HEIGHT=500)

        self.assertTrue(wall_bump)

    def test_check_collisions_body(self):
        snake_id = Snake.Snake(BODY_PARTS=3)
        snake_id.coordinates[0] = [10, 10]
        snake_id.coordinates[2] = [10, 10]
        body_bump = Game.check_collisions(snake_id, GAME_WIDTH=500, GAME_HEIGHT=500)

        self.assertTrue(body_bump)

    def test_check_collisions_no_collisions(self):
        snake_id = Snake.Snake(BODY_PARTS=3)
        snake_id.coordinates[0] = [10, 10]
        collision = Game.check_collisions(snake_id, GAME_WIDTH=500, GAME_HEIGHT=500)

        self.assertFalse(collision)


if __name__ == '__main__':
    unittest.main()
