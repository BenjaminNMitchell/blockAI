from block_ai.lib.myblokus.agent import Agent, HumanInput
from block_ai.lib.myblokus.game import Game

import unittest
from unittest.mock import patch


class HumanInput(unittest.TestCase):

    def test_get_move(self):
        # Given
        game = Game()
        hi = HumanInput(3)




'''



        # When
        move = hi.get_move(game)
        
        # Then
        o = Orientation((Point(0, 0,)))
        c = Corner(Point(-1, -1), Point(0, 0))
        expected = Move(o, 3, 'p1', c)

        self.assertMove(move, expected)'''
