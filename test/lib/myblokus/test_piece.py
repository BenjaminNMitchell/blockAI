from block_ai.lib.myblokus import piece
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
                  Point(2, 0),
                  Point(3, 0),
                  Point(3, 1)]

        # When
        actual = Piece(points).orientations

        # Then
        self.maxDiff = None

        expected = {
            # C1
            Orientation((Point(0, 0), Point(1, 0), Point(1, 1), Point(1, 2), Point(1, 3))),
            Orientation((Point(0, 0), Point(0, 1), Point(1, 1), Point(2, 1), Point(3, 1))),
            # C2
            Orientation((Point(0, 0), Point(1, 0), Point(0, 1), Point(0, 2), Point(0, 3))),
            Orientation((Point(0, 0), Point(0, 1), Point(1, 0), Point(2, 0), Point(3, 0))),
            # C3
            Orientation((Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0), Point(3, -1))),
            Orientation((Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3), Point(-1, 3))),
            # C4
            Orientation((Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0), Point(3, 1))),
            Orientation((Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3), Point(1, 3))),
            # C5
            Orientation((Point(0, 0), Point(1, 0), Point(1, -1), Point(1, -2), Point(1, -3))),
            Orientation((Point(0, 0), Point(0, 1), Point(-1, 1), Point(-2, 1), Point(-3, 1)))
        }

        self.assertEqual(sorted(actual), sorted(expected))

    def test_get_orientation_prime(self):
        # Given
        points = [Point(0, 0),
                  Point(1 ,0),
                  Point(1, 1)]

        piece = Piece(points)

        # When
        actual = piece.get_orientation_prime()

        # Then
        expected = Orientation((
                                Point(-1, 1),
                                Point(0, 0),
                                Point(0, 1)
        ))
        self.assertEqual(actual, expected)

    def test_equals(self):
        # Given
        points = [Point(0, 0),
                  Point(1 ,0),
                  Point(1, 1)]

        p1 = Piece(points)
        p2 = Piece(points)

        # Then
        self.assertEqual(p1, p2)

    def test_equals_different_points(self):
        # Given
        points1 = [Point(0, 0),
                  Point(1 ,0),
                  Point(1, 1)]

        points2 = [Point(0, 0),
                  Point(1 ,0),
                  Point(2, 0)]

        p1 = Piece(points1)
        p2 = Piece(points2)

        # Then
        self.assertFalse(p1 == p2)

    def test_equals_wrong_object(self):
        # Given
        piece = Piece([Point(0, 0)])

        self.assertNotEqual(piece, 1)

    def test_str(self):
        # Given
        piece = Piece([Point(0, 0)])

        # When
        actual = str(piece)
        expected = "Piece:\nOrientation:\n(0, 0)"

        # Then
        self.assertEqual(actual, expected)

