from block_ai.lib.myblokus.game import Game
from . import expected_move import expected_moves
import unittest


class GameTests(unittest.TestCase):

    def test_game(self):
        # Given
        game = Game()

        # When

        for val in expected_moves:
            move, options = expected_moves[val]
            

