from block_ai.lib.myblokus.corner import Corner
from block_ai.lib.myblokus import point

import unittest
import hypothesis

class CornerTests(unittest.TestCase):

    def test_invalid_diff(self):
        # Given
        p1 = (0, 0)
        p2 = (1, 2)

        # Then
        with self.assertRaises(ValueError):

            # When
            c = Corner(p1, p2)

    def test_get_rotation(self):
        # Given
        points = [
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]

        for point in points:
            c = Corner((0, 0), point)

            # When
            rot = c.get_rotation()
            vector = rot(c.diff)

            # Then
            self.assertEqual(vector, (1, 1))

    def test_eq_true(self):
        # Given
        c1 = Corner((0, 0), (1, 1))
        c2 = Corner((0, 0), (-1, -1))

        # Then
        self.assertTrue(c1 == c1)
        self.assertFalse(c1 == c2)
    
    def test_hash(self):

        # Given
        c1 = Corner((0, 0), (1, 1))
        c2 = Corner((0, 0), (1, 1))
        c3 = Corner((0, 0), (-1, -1))

        # When
        h1 = hash(c1)
        h2 = hash(c2)
        h3 = hash(c3)

        # Then
        self.assertTrue(h1 == h2)
        self.assertFalse(h1 == h3)
