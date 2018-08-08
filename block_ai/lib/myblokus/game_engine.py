import logging
import itertools

from .game import Game, GameEnd
from .agent import RandomAgent, GreedyAgent, HumanInput, PointAgent


class GameEngine:
    
    def __init__(self, display=False):
        self.display = display
        self.game = Game()
        self.players = [RandomAgent(0), RandomAgent(1), RandomAgent(2), PointAgent(3)]

    def play_game(self):
        while True:
            try:
                if self.game.player_pointer % 4 == 0:
                    print(self.game.player_pointer)
                self.play_turn()
            except GameEnd:
                break

    def play_turn(self):
        try:
            m = self.get_move()
            self.game.make_move(m)
        except RuntimeError as err:
            logging.info(err)
            self.game.set_next_player()

        if self.display:
            self.game.display(self.game.player_pointer - 1)
            
    def get_move(self):
        ptr = self.game.player_pointer
        logging.info("Player pointer: %s", ptr)
        agent = self.players[ptr]
        logging.info("Agent id: %s", agent.player_id)
        return agent.get_move(self.game)
