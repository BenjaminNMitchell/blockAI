from block_ai.lib.myblokus.player import Player
from block_ai.lib.myblokus.point import Point

import unittest
import hypothesis


class PlayerTests(unittest.TestCase):

    def test_add_move(self):
        # Given
        player = Player(1)

        # When
        player.add_move([Point(0, 0)])

        # Then
        self.assertEqual(len(player.valid_moves), 1)
