from block_ai.lib.myblokus.move import Move
from block_ai.lib.myblokus.corner import Corner
from block_ai.lib.myblokus.orientation import Orientation

from . import test_lib as tl

import unittest

class MoveTests(unittest.TestCase):

    def test_hash_eq(self):
        # Given

        move1 = tl.get_move()

        move2 = tl.get_move()

        # when
        h1 = hash(move1)
        h2 = hash(move2)

        # Then
        self.assertEqual(h1, h2)

    def test_hash_not_equal_orientation(self):
        # Given
        # differ for the two components of a move

        player_id3 = 1

        move1 = tl.get_move()
        
        move2 = tl.get_move(piece=(1, 1, 1))

        # When
        h1 = hash(move1)
        h2 = hash(move2)

        # Then
        self.assertNotEqual(h1, h2)


    def test_eq(self):
        
        player_id3 = 1

        move1 = tl.get_move()
        move2 = tl.get_move(piece=(1, 1, 1))

        # Then
        self.assertNotEqual(move1, move2)

    def test_get_size(self):
        # Given 
        move1 = tl.get_move(piece_id=0)
        move2 = tl.get_move(piece_id=1)
        move3 = tl.get_move(piece_id=2)
        move4 = tl.get_move(piece_id=5)
        move5 = tl.get_move(piece_id=10)

        self.assertEqual(1, move1.get_size())
        self.assertEqual(2, move2.get_size())
        self.assertEqual(3, move3.get_size())
        self.assertEqual(4, move4.get_size())
        self.assertEqual(5, move5.get_size())
            
