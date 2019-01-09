from block_ai.lib.myblokus.player import Player

import unittest

class PlayerTests(unittest.TestCase):
    
    def test_get_score(self):
        # Given
        p = Player(0)

        # When
        score = p.get_score()

        # Then
        self.assertEqual(score, 89)
        
