from block_ai.lib.myblokus.player import Player
from block_ai.lib.myblokus.point import Point

import unittest

class PlayerTests(unittest.TestCase):

    def test_add_invalid_point(self):
        # Given
        point = Point(0, 0)
        player = Player(0)
        
        # When
        player.invalid_points.add(point)

        # Then

        self.assertTrue(point in player.invalid_points)
