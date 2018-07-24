"""This class defines an agent for the Blokus Game"""

import random


class Agent:

    def __init__(self, player_id):
        self.player_id = player_id
    
    def get_move(self, game):
        raise RuntimeError("get_move is not implimented")
    
    
class RandomAgent(Agent):
    
    def get_move(self, game):
        valid_moves = list(game.get_players_moves(self.player_id))
        return self.pick_random_move(valid_moves)
        
    def pick_random_move(self, moves):     
        if len(moves) == 0:
            raise RuntimeError(f"Player {self.player_id} is out of moves")

        rand_int = random.randrange(len(moves))
        return moves[rand_int]

class GreedyAgent(RandomAgent):

    def get_move(self, game):
        valid_moves = list(game.get_players_moves(self.player_id))
        max_len = max([len(m.orientation) for m in valid_moves])
        largest_moves = list(filter(lambda m: len(m.orientation) == max_len, valid_moves))
        return self.pick_random_move(largest_moves)
