from block_ai.lib.myblokus.game import Game
from .benchmark_game import moves, turn_moves
import unittest


class GameTests(unittest.TestCase):

    def test_game(self):
        # Given
        game = Game()
        
        # When
        actual_moves = [set(game.get_players_moves(i)) for i in range(4)]
        self.assertEqual( turn_moves[0], actual_moves)

        for move, expected_moves in zip(moves, turn_moves[1:]):

            game.make_move(move)

            actual_moves = [set(game.get_players_moves(i)) for i in range(4)]

            self.assertEqual(actual_moves, expected_moves)


        
        self.assertFalse(game.has_moves())


    def test_pop(self):
        
        g1 = Game()
        g2 = Game()
        
        self.assertEqual(g1, g2)

        g1.make_move(moves[0])

        self.assertNotEqual(g1, g2)

        g1.pop()

        self.assertEqual(g1, g2)
