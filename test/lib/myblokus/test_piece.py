from block_ai.lib.myblokus.piece import Piece
from block_ai.lib.myblokus.orientation import Orientation
from block_ai.lib.myblokus.point import Point
from block_ai.lib.myblokus import point

import unittest
import hypothesis

class PieceTests(unittest.TestCase):

    def test_all_orientations_get_added(self):
        # Given
        points = [Point(0, 0),
                  Point(1 ,0),
                  Point(1, 1)]

        # When
        actual = Piece(points).orientations

        # Then
        self.maxDiff = None
        expected = [
                    Orientation([Point(0, 0), Point(1, 0), Point(1, 1)]),
                    Orientation([Point(0, 0), Point(0, 1), Point(-1, 1)]),
                    Orientation([Point(0, 0), Point(0, 1), Point(1, 1)]),
                    Orientation([Point(0, 0), Point(1, 0), Point(1, -1)]),
                    Orientation([Point(0, 0), Point(1, 0), Point(0, 1)])
              ]

        self.assertEqual(actual, expected)

   def test_shift_orientation(self):
        # Given
        points = [Point(0, 0),
                  Point(1 ,0),
                  Point(1, 1)]

        piece = Piece(points)

        # When
        corner_point = Point(2, -1)
        

