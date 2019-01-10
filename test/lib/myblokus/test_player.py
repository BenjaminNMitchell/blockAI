from block_ai.lib.myblokus.player import Player
from . import test_lib as tl

import unittest
from unittest.mock import Mock

class PlayerTests(unittest.TestCase):

    def test_eq(self):
        # Given
        b = Mock()
        b.board = 0
        p1 = Player(0, b)
        
        p2 = Player(1, b) 

        self.assertEqual(p1, p1)
        self.assertNotEqual(p1, p2)

    def test_update(self):
        # Given
        b = Mock()
        b.board = 0
        p1 = Player(0, b)
        p2 = Player(0, b)

        move = tl.get_move()
        
        self.assertEqual(p1, p2)

        p1.update(move, b)
        self.assertNotEqual(p1, p2)

        p1.pop(move)
        self.assertEqual(p1, p2)
    
    def test_get_score(self):
        # Given
        b = Mock()
        b.board = 0
        p = Player(0, b)

        # When
        score = p.get_score()

        # Then
        self.assertEqual(score, 89)

