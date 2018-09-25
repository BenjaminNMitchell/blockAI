from block_ai.lib.myblokus.game import Game, GameEnd
from .turn_moves import turn_moves
import unittest


class GameTests(unittest.TestCase):

    def test_game(self):
        # Given
        game = Game()

        # When
        with self.assertRaises(GameEnd):

            for turn_num in turn_moves:

                move, expected_moves  = turn_moves[turn_num]

                actual_moves = list(game.get_players_moves(move.player_id))

                self.assertEqual(sorted(actual_moves), sorted(expected_moves))

                game.make_move(move)
            

