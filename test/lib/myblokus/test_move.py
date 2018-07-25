from block_ai.lib.myblokus.move import Move
from block_ai.lib.myblokus.corner import Corner
from block_ai.lib.myblokus.point import Point
from block_ai.lib.myblokus.orientation import Orientation

import unittest

class MoveTests(unittest.TestCase):

    def get_move(self, orientation=None, player_id=None, piece_id=None, corner=None):
        
        if orientation is None:
            orientation = self.get_orientation()

        if player_id is None:
            player = 0

        if piece_id is None:
            piece_id = 'p4'

        if corner is None:
            corner = self.get_corner()

        return Move(orientation, player_id, piece_id, corner)

    def get_orientation(self):
        
        points = (
            Point(0, 0),
            Point(0, 1),
            Point(1, 1)
            )

        return Orientation(points) 
    
    def get_corner(self):

        return Corner(Point(-1, -1), Point(0, 0))

    def test_hash_eq(self):
        # Given

        move1 = self.get_move()

        move2 = self.get_move()

        # when
        h1 = hash(move1)
        h2 = hash(move2)

        # Then
        self.assertEqual(h1, h2)

    def test_hash_not_equal_orientation(self):
        # Given
        # differ each of the 4 components of a move
        orientation2 = (
            Point(0, 0),
            Point(0, 1),
            Point(0, 2)
            )

        player_id5 = 1

        move1 = self.get_move()
        move2 = self.get_move(orientation=orientation2)
        move3 = self.get_move(player_id=player_id3)

        # When
        h1 = hash(move1)
        h2 = hash(move2)
        h3 = hash(move3)

        # Then
        self.assertNotEqual(h1, h2)
        self.assertNotEqual(h1, h3)

    def test_eq(self):
        
        orientation2 = Orientation((
            Point(0, 0),
            Point(0, 1),
            Point(0, 2)
            ))

        player_id5 = 1

        move1 = self.get_move()
        move2 = self.get_move(orientation=orientation2)
        move3 = self.get_move(player_id=player_id3)

        # Then
        self.assertNotEqual(move1, move2)
        self.assertNotEqual(move1, move3)
