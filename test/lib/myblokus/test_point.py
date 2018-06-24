from block_ai.lib.myblokus.point import Point

import unittest

from hypothesis import given
import hypothesis.strategies as st

class PointTests(unittest.TestCase):

    def test_init(self):
        p = Point(1, 1)

    def test_init_fails(self):
        with self.assertRaises(TypeError):
            p = Point(None, None)

    def test_get_adjacent(self):
        # Given 
        p = Point(1, 1)

        # When
        adjacent = p.get_adjacent()

        # Then
        expected = [Point(0, 1),
                    Point(1, 0),
                    Point(1, 2),
                    Point(2, 1)]
        self.assertEqual(adjacent, expected)

    def test_get_corners(self):
        # Given
        p = Point(1, 1)

        # When
        corners = p.get_corners()

        # Then
        expected = [Point(0, 0),
                    Point(0, 2),
                    Point(2, 0),
                    Point(2, 2)]
        self.assertTrue(corners, expected)

    def test_str(self):
        # Given
        p = Point(1, 1)

        # When
        p_str = str(p)

        # Then
        self.assertEqual(p_str, "(1, 1)")

    @given(x=st.integers(), y=st.integers())
    def test_equal(self, x, y):
        p1 = Point(x, y)
        p2 = Point(x, y)

        self.assertTrue(p1 == p2)


    @given(x=st.integers(), y=st.integers())
    def test_not_equal(self, x, y):
        p1 = Point(x, y)
        p2 = Point(x + 1, y)
        
        self.assertNotEqual(p1, p2)
        self.assertTrue(p1 != p2)
    
    @given(x=st.integers(), y=st.integers())
    def test_hash(self, x, y):
        p1 = Point(x, y)
        p2 = Point(x, y)
    
        self.assertEqual(hash(p1), hash(p2))

    @given(x=st.integers(), y=st.integers())
    def test_less_than(self, x, y):
        # Given
        p1 = Point(x - 1, y)
        p2 = Point(x, y - 1)
        p3 = Point(x, y)
        p4 = Point(x, y + 1)
        p5 = Point(x + 1, y + 1)

        # Then
        self.assertTrue(p1 < p2)
        self.assertTrue(p2 < p3)
        self.assertTrue(p3 < p4)
        self.assertTrue(p4 < p5)

    
    @given(x=st.integers(), y=st.integers())
    def test_greater_than(self, x, y):
        # Given
        p1 = Point(x - 1, y)
        p2 = Point(x, y - 1)
        p3 = Point(x, y)
        p4 = Point(x, y + 1)
        p5 = Point(x + 1, y + 1)

        # Then
        self.assertFalse(p1 > p2)
        self.assertFalse(p2 > p3)
        self.assertFalse(p3 > p4)
        self.assertFalse(p4 > p5)

    @given(x=st.integers(), y=st.integers(), a=st.integers(), b=st.integers())
    def test_add(self, x, y, a, b):
        # Given
        p1 = Point(x, y)
        p2 = Point(a, b)

        # When
        p_sum = p1 + p2

        # Then
        self.assertEqual(p_sum.x, x + a)
        self.assertEqual(p_sum.y, y + b)


    @given(x=st.integers(), y=st.integers(), a=st.integers(), b=st.integers())
    def test_sub(self, x, y, a, b):
        # Given
        p1 = Point(x, y)
        p2 = Point(a, b)
        
        # When
        p_sum = p1 - p2

        # Then
        self.assertEqual(p_sum.x, x - a)
        self.assertEqual(p_sum.y, y - b)

