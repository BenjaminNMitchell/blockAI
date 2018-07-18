class Agent:

    def __init__(self, player_id):
        self.player_id = player_id
    
    def get_move(self, game):
        raise RuntimeError("get_move is not implimented")
    
    
class RandomAgent(Agent):
    
    def __init__(self, player_id):
        self.player_id = player_id
        
    def get_move(self, game):
        valid_moves = list(game.get_players_moves(self.player_id))
        return self.pick_random_move(valid_moves)
        
    def pick_random_move(self, moves):     
        if len(moves) == 0:
            raise RuntimeError(f"Player {self.player_id} is out of moves")

        rand_int = random.randrange(len(moves))
        return moves[rand_int]
