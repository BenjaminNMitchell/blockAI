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
