from block_ai.lib.myblokus import point
from block_ai.lib.myblokus.point import X, Y

import unittest

from hypothesis import given
import hypothesis.strategies as st

class PointTests(unittest.TestCase):

    def test_get_adjacent(self):
        # Given 
        p = (1, 1)

        # When
        adjacent = point.get_adjacent(p)

        # Then
        expected = [(0, 1),
                    (1, 0),
                    (1, 2),
                    (2, 1)]
        self.assertEqual(adjacent, expected)

    def test_get_corners(self):
        # Given
        p = (1, 1)

        # When
        corners = point.get_corners(p)

        # Then
        expected = [(0, 0),
                    (0, 2),
                    (2, 0),
                    (2, 2)]
        self.assertTrue(corners, expected)

    def test_str(self):
        # Given
        p = (1, 1)

        # When
        p_str = str(p)

        # Then
        self.assertEqual(p_str, "(1, 1)")

    def test_repr(self):

        # Given
        p = (1, 1)

        # When
        p_repr = repr(p)

        # Then
        self.assertEqual(p_repr, "(1, 1)")

    @given(x=st.integers(), y=st.integers())
    def test_equal(self, x, y):
        # Given
        p1 = (x, y)
        p2 = (x, y)

        # Then
        self.assertTrue(p1 == p2)


    @given(x=st.integers(), y=st.integers())
    def test_not_equal(self, x, y):
        # Given
        p1 = (x, y)
        p2 = (x + 1, y)

        # Then
        self.assertNotEqual(p1, p2)
        self.assertTrue(p1 != p2)
    
    @given(x=st.integers(), y=st.integers())
    def test_hash(self, x, y):
        # Given
        p1 = (x, y)
        p2 = (x, y)

        # Then
        self.assertEqual(hash(p1), hash(p2))

    @given(x=st.integers(), y=st.integers())
    def test_less_than(self, x, y):
        # Given
        p1 = (x - 1, y)
        p2 = (x, y - 1)
        p3 = (x, y)
        p4 = (x, y + 1)
        p5 = (x + 1, y + 1)

        # Then
        self.assertFalse(p1 < p1)
        self.assertTrue(p1 < p2)
        self.assertTrue(p2 < p3)
        self.assertTrue(p3 < p4)
        self.assertTrue(p4 < p5)

    
    
    @given(x=st.integers(), y=st.integers())
    def test_greater_than(self, x, y):
        # Given
        p1 = (x - 1, y)
        p2 = (x, y - 1)
        p3 = (x, y)
        p4 = (x, y + 1)
        p5 = (x + 1, y + 1)

        # Then
        self.assertFalse(p1 > p2)
        self.assertFalse(p2 > p3)
        self.assertFalse(p3 > p4)
        self.assertFalse(p4 > p5)

    @given(x=st.integers(), y=st.integers(), a=st.integers(), b=st.integers())
    def test_add(self, x, y, a, b):
        # Given
        p1 = (x, y)
        p2 = (a, b)

        # When
        p_sum = point.add(p1, p2)

        # Then
        expected = (x + a, y + b)
        self.assertEqual(p_sum, expected)

    @given(x=st.integers(), y=st.integers(), a=st.integers(), b=st.integers())
    def test_sub(self, x, y, a, b):
        # Given
        p1 = (x, y)
        p2 = (a, b)
        
        # When
        p_diff = point.subtract(p1, p2)

        # Then
        expected = (x - a, y - b)
        self.assertEqual(p_diff, expected)
   
    @given(x=st.integers(), y=st.integers())
    def test_from_string(self, x, y):
        # Given
        p1 = (x, y)

        # When
        p2 = point.from_string(str(p1))
        
        # Then
        self.assertEqual(p1, p2)

    @given(x=st.integers(), y=st.integers())
    def test_ident_transform(self, x, y):
        # Given
        p1 = (x, y)

        # When
        p2 = point.ident(p1)

        # Then
        self.assertEqual(p1, p2)


    @given(x=st.integers(), y=st.integers())
    def test_flip_transform(self, x, y):
        # Given
        p1 = (x, y)

        # When
        p2 = point.flip(p1)
        p3 = point.flip(p2)

        # Then
        self.assertEqual(p1, p3)
        self.assertEqual(p1[X], p2[X])
        self.assertEqual(p1[Y], -p2[Y])

    
    @given(x=st.integers(), y=st.integers())
    def test_rot90_transform(self, x, y):
        # Given
        p1 = (x, y)

        # When
        p2 = point.rot90(p1)
        
        p = p1
        for i in range(4):
            p = point.rot90(p)

        # Then
        self.assertEqual(p1[X], -p2[Y])
        self.assertEqual(p1[Y], p2[X])
        self.assertEqual(p1, p)


    @given(x=st.integers(), y=st.integers())
    def test_rot180_transform(self, x, y):
        # Given
        p1 = (x, y)

        # When
        p2 = point.rot180(p1)
        
        p = p1
        for i in range(2):
            p = point.rot180(p)

        # Then
        self.assertEqual(p1[X], -p2[X])
        self.assertEqual(p1[Y], -p2[Y])
        self.assertEqual(p1, p)

    @given(x=st.integers(), y=st.integers())
    def test_rot270_transform(self, x, y):
        # Given
        p1 = (x, y)

        # When
        p2 = point.rot270(p1)
        
        p = p1
        for i in range(4):
            p = point.rot90(p)

        # Then
        self.assertEqual(p1[X], p2[Y])
        self.assertEqual(p1[Y], -p2[X])
        self.assertEqual(p1, p)

