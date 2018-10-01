from block_ai.lib.myblokus.player import Player

import unittest

class PlayerTests(unittest.TestCase):

    def test_add_invalid_point(self):
        # Given
        point = (0, 0)
        player = Player(0)
        
        # When
        player.invalid_points.add(point)

        # Then
        self.assertTrue(point in player.invalid_points)

    def test_update_same_player(self):
        # Given
        player = Player(0)
        # When
        # Then

    
    def test_get_score(self):
        # Given
        p = Player(0)

        # When
        score = p.get_score()

        # Then
        self.assertEqual(score, 89)
        
