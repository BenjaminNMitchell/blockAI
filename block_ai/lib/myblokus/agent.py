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

        piece = self.get_piece(player)

        corner = self.get_piece(player, piece)

        move = self.get_move(player, piece, corner)


        return move
    


    def get_piece(self, player):
        
        pieces = player.pieces

        string = "Please Pick a piece from one of the following:\n"
        string += "\n".join(pieces)
        string += ": "

        while True:
            piece = input(string)
            if piece in pieces:
                return piece
            else:
                print("Invalid piece please try again")

    def get_corner(self, player, piece):
        
        moves = player.valid_moves.get_piece_moves(piece)
        corners = list(filter(lambda m: m.corner, moves))

        string = "Please pick a corner from the following by its index"
        strings = [f"{str(c.p2)}, {i}" for i, c in enumerate(corners)]
        string += "\n".join(strings)

        return pick_by_index(corners, string)


    def get_move(self, player, piece, corner):
        moves = player.valid_moves.get_corner_piece_moves(corner, piece)
        for i, move in enumerate(moves):
            b = game.board.copy()
            print(f"Move {i}")
            b.update(move)
            b.display()

        string = f"pick a move in range [0, {len(moves)}]"
        return pick_by_index(moves, string)

    def pick_by_index(self, values, string):

        while True:

            try:
                index = self.get_index(string)
                return values[index]

            except IndexError:
                print("Invalid Selection please try again.")

    def get_index(self, string):
        resp = input(string)
        try:
            return int(resp)

        except ValueError:
            print("Not a valid int try again")
