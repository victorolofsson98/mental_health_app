import unittest
<<<<<<< HEAD:unit_tests/test_snake.py
from code_files import Snake
import code_files.Snake
=======
import Snake
>>>>>>> df82b746d834b40e2d91f22ce0ae1966fe07e6d7:code_files/test_snake.py


class MyTestCase(unittest.TestCase):
    def test__init__(self):
        """"test snake class attributes"""
        snake_id = Snake.Snake(BODY_PARTS=3)
        list_x_y = [[0, 0], [0, 0], [0, 0]]
        squares_comp = []
        self.assertEqual(snake_id.body_size, 3)
        self.assertEqual(snake_id.coordinates, list_x_y)
        self.assertEqual(snake_id.squares, squares_comp)

    def test_get_coordinates(self):
        """"test get coordinates function"""
        x_exp, y_exp = Snake.get_coordinates(GAME_WIDTH=500, GAME_HEIGHT=500, SPACE_SIZE=40)

        self.assertGreaterEqual(x_exp, 0)
        self.assertLessEqual(x_exp, 460)
        self.assertGreaterEqual(y_exp, 0)
        self.assertLessEqual(y_exp, 460)


if __name__ == '__main__':
    unittest.main()
