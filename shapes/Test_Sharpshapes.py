import unittest
from shape import Shape

class TestSharpShapes(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')

    def test_shape_type(self):
        simple = Shape()

        assertIsInstance(simple, Shape);

    def test_shape_area(self):
        simple = Shape()
        simple.width = 2
        simple.height = 2

        assertEqual(simple.calculate_area(), 4);