from block_ai.lib.myblokus.orientation import Orientation
from block_ai.lib.myblokus import point  
from block_ai.lib.myblokus.corner import Corner

import unittest
from hypothesis import given
import hypothesis.strategies as st


class OrientationPoints(unittest.TestCase):
    
    def setUp(self):
        self.p1 = (0, 0)
        self.p2 = (1, 0)
        self.p3 = (1, 1)
        self.points = [self.p1, self.p2, self.p3]

    def test_setup(self):
        o = Orientation(self.points)

    def test_get_border_points(self):
        # Given
        o = Orientation(self.points)

        # When
        actual = o.get_border_points()

        # Then
        expected = {(-1, 0), 
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 2),
                    (2, 0),
                    (2, 1)}
        self.assertEqual(actual, expected)

    def test_get_corners(self):
        # Given
        o = Orientation(self.points)

        # When
        actual = o.get_corners()

        # Then
        expected = {
            Corner((0, 0), (-1, 1)),
            Corner((1, 1), (0, 2)),
            Corner((1, 0), (2, -1)),
            Corner((1, 1), (2, 2)),
            Corner((0, 0), (-1, -1))
        }
        self.assertEqual(actual, expected)

    def test_is_valid(self):
        # Given
        o = Orientation(self.points)

        # When
        actual = o.is_valid()

        # Then
        self.assertTrue(actual)

    def test_is_valid_false(self):
        # Given
        o = Orientation([(-1, -1)])

        # When
        actual = o.is_valid()

        # Then
        self.assertFalse(actual)

    @given(st.integers(), st.integers())
    def test_hash(self, x, y):
        # Given
        p1 = (x, y)
        p2 = (x + 1, y + 1)
    
        o1 = Orientation([p1, p2])
        o2 = Orientation([p1, p2])

        # Then
        self.assertEqual(hash(o1), hash(o2))

    def test_length(self):
        # Given
        o = Orientation(self.points)

        # When
        length = len(o)

        # Then
        self.assertEqual(length, 3)

    def test_less_than_unequal_length(self):    
        # Given
        o1 = Orientation([self.p1, self.p2])
        o2 = Orientation(self.points)

        # Then
        self.assertTrue(o1 < o2)


    def test_less_than_equal_length(self):
        # Given
        p1 = (0, 0)
        p2 = (0, 1)
        p3 = (1, 0)
    
        o1 = Orientation([p1, p2])
        o2 = Orientation([p1, p3])

        # Then
        self.assertTrue(o1 < o2)

    def test_equals_true(self):
        # Given
        o1 = Orientation([(0, 0), (0, 1)])
        o2 = Orientation([(0, 0), (0, 1)])

        # Then
        self.assertTrue(o1 == o2)
    
    def test_equals_false(self):
        # Given
        o1 = Orientation([(0, 0), (0, 1)])
        o2 = Orientation([(0, 0), (1, 0)])

        # Then
        self.assertFalse(o1 == o2)

    def test_equals_false_different_length(self):
        # Given
        o1 = Orientation([(0, 0), (0, 1)])
        o2 = Orientation([(0, 0)])

        # Then
        self.assertFalse(o1 == o2)

    def test_str(self):
        # Given
        o = Orientation(self.points)

        # When
        actual = str(o)

        # Then
        expected = "Orientation:\n(1, 0)\n(0, 0)\n(1, 1)" 
        self.assertEqual(actual, expected)

    def test_repr(self):
        ## Multiple Points Case
        # Given
        o = Orientation(self.points)

        # When
        new_o = eval(repr(o))

        # Then
        self.assertEqual(o, new_o)

        ## Single Points Case
        # Given
        o = Orientation(((19, 19),))

        # When
        new_o = eval(repr(o))

        # Then
        self.assertEqual(o, new_o)
