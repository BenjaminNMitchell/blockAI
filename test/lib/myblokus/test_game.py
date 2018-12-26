from block_ai.lib.myblokus.game import Game
from .turn_moves import turn_moves
import unittest


class GameTests(unittest.TestCase):

    def test_game(self):
        # Given
        game = Game()

        # When
        for turn_num in turn_moves:

            move, expected_moves  = turn_moves[turn_num]

            actual_moves = set(game.get_players_moves(move.player_id))

            self.assertEqual(actual_moves, set(expected_moves))

            game.make_move(move)
        
        self.assertFalse(game.has_moves())
