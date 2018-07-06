from block_ai.lib.myblokus.piece import *
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
            Orientation((Point(-1, 1), Point(0, 0), Point(0, 1))),
            Orientation((Point(0, 0), Point(0, 1), Point(1, 0))),
            Orientation((Point(0, 0), Point(0, 1), Point(1, 1))),
            Orientation((Point(0, 0), Point(1, -1), Point(1, 0))),
            Orientation((Point(0, 0), Point(1, 0), Point(1, 1)))
        ]
        self.assertEqual(actual, expected)

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
        expected = "(Point(0, 0),)"

        # Then
        self.assertEqual(actual, expected)

    def test_repr(self):
        # Given
        piece = Piece([Point(0, 0)])

        # When
        actual = repr(piece)
        expected = "Piece([Orientation((Point(0, 0),))])"

        # Then
        self.assertEqual(actual, expected)
