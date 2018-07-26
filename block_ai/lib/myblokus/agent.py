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


class HumanInput(Agent):

    def get_move(self, game):
        player = game.players[self.player_id]
        pieces = player.pieces

        while True:

            string = "Please Pick a piece from one of the following:\n"
            string += "\n".join(pieces)
            string += ": "
            piece = input(string)
            if piece in pieces:
                break
            else:
                print("Invalid piece please try again")

        moves = player.valid_moves.get_piece_moves(piece)
        corners = list(filter(lambda m: m.corner, moves))

        string = "Please pick a corner from the following by its index"
        strings = [f"{str(c.p2)}, {i}" for i, c in enumerate(corners)]
        string += "\n".join(strings)

        corner = get_response(corners, string)

        moves = player.valid_moves.get_corner_piece_moves()

        for i, move in enumerate(moves):
            b = game.board.copy()
            print(f"Move {i}")
            b.update(move)
            b.display()

        string = f"pick a move in range [0, {len(moves)}]"
        move = get_response(moves, string)
        return move

    def get_response(self, values, string):

        while True:

            resp = input(string)
            try:
                index = int(resp)
                return values[index]

            except Exception:
                print("Invalid Selection please try again.")


    
