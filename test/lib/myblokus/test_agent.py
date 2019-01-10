from block_ai.lib.myblokus.agent import RandomAgent, GreedyAgent, PointAgent, GreedyPointAgent
from block_ai.lib.myblokus.game import Game
from block_ai.lib.myblokus.move import Move

import unittest
from unittest.mock import patch


class AgentTests(unittest.TestCase):

    def test_random_agent(self):
        # Givent
        g = Game()
        a = RandomAgent(0)
        
        m = a.get_move(g)

        self.assertTrue(type(m) is Move)

    def test_greedy_agent(self):
        # Givent
        g = Game()
        a = GreedyAgent(0)
        
        m = a.get_move(g)

        self.assertTrue(type(m) is Move)

    def test_point_agent(self):
        # Givent
        g = Game()
        a = PointAgent(0)
        
        m = a.get_move(g)

        self.assertTrue(type(m) is Move)
        
    def test_greedy_point_agent(self):
        # Givent
        g = Game()
        a = GreedyPointAgent(0)
        
        m = a.get_move(g)

        self.assertTrue(type(m) is Move)

