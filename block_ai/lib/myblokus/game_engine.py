import logging
import itertools

from .game import Game, GameEnd
from .agent import RandomAgent, GreedyAgent, HumanInput, PointAgent


class GameEngine:
    
    def __init__(self, display=False, players=None):
        self.display = display
        self.game = Game()
        if players is None:
            self.players = [RandomAgent(i) for  i in range(4)]
        else:
            if len(players) != 4:
                raise ValueError("Must specify 4 player strings")

            self.players = [self.load_player(i, string) for i, string in enumerate(players)]

    def load_player(self, player_num, string):
        if string == 'random':
            return RandomAgent(player_num)
        elif string == 'greedy':
            return GreedyAgent(player_num)
        elif string == 'point':
            return PointAgent(player_num)
        elif string == 'human':
            return HumanInput(player_num)
        else:
            raise ValueError(f"Invalid agent string {string}")

    def play_game(self):
        while True:
            try:
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
