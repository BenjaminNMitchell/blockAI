from block_ai.lib.myblokus.player import Player
from block_ai.lib.myblokus.point import Point

from .test_lib import get_move

import unittest

class PlayerTests(unittest.TestCase):

    def test_update_same_player(self):
        # Given
        player = Player(0)
        move = get_move(player_id=0)

        # When
        player.update(move)
    
        # Then

    
    def test_get_score(self):
        # Given
        p = Player(0)

        # When
        score = p.get_score()

        # Then
        self.assertEqual(score, 89)
        
