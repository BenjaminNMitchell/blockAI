"""This class defines an agent for the Blokus Game"""

import random
import datetime as dt
import logging

class OutOfMoves(Exception):
    pass

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
            raise OutOfMoves(f"Player {self.player_id} is out of moves")

        rand_int = random.randrange(len(moves))
        return moves[rand_int]

class GreedyAgent(RandomAgent):

    def get_move(self, game):
        valid_moves = list(game.get_players_moves(self.player_id))
        max_len = max([m.get_size() for m in valid_moves])
        largest_moves = list(filter(lambda m: m.get_size() == max_len, valid_moves))
        return self.pick_random_move(largest_moves)

class PointAgent(Agent):

    def __init__(self, player_id):
        self.turn_counter = 0
        super().__init__(player_id)

    def get_move(self, game):

        moves = list(game.get_players_moves(self.player_id))

        logging.info("Analizing %s potential moves on move: %s", len(moves), self.turn_counter)

        if len(moves) == 0:
            raise OutOfMoves(f"Player {self.player_id} is out of moves")

        max_move = None
        max_count = 0
        
        t0 = dt.datetime.now()
        for move in moves:

            game.make_move(move)
            move_num = len(list(game.get_players_moves(self.player_id)))

            if move_num >= max_count:
                max_count = move_num
                max_move = move

            game.pop()

        self.turn_counter += 1

        t1 = dt.datetime.now()

        logging.info("Completed in %s seconds", (t1 - t0).total_seconds())

        if max_move is None:
            raise ValueError(f"Not returning a Max Move Moves Length: {len(moves)}")

        return max_move

class GreedyPointAgent(Agent):

    def __init__(self, player_id):
        self.turn_counter = 0
        super().__init__(player_id)

    def get_move(self, game):
 
        moves = list(game.get_players_moves(self.player_id))

        biggest_piece_size = self.get_biggest_piece_size(moves)

        logging.info("Analizing %s potential moves on move: %s", len(moves), self.turn_counter)

        if len(moves) == 0:
            raise OutOfMoves(f"Player {self.player_id} is out of moves")

        max_move = None
        max_count = 0
        
        moves = filter(lambda m: m.get_size() == biggest_piece_size, moves)

        t0 = dt.datetime.now()
        for move in moves:

            game.make_move(move)
            move_num = len(list(game.get_players_moves(self.player_id)))

            if move_num >= max_count:
                max_count = move_num
                max_move = move

            game.pop()

        self.turn_counter += 1

        t1 = dt.datetime.now()

        logging.info("Completed in %s seconds", (t1 - t0).total_seconds())

        if max_move is None:
            raise ValueError(f"Not returning a Max Move Moves Length: {len(moves)}")

        return max_move

    def get_biggest_piece_size(self, moves):

        max_piece_size = 0

        for move in moves:
 
            piece_size = move.get_size()

            if piece_size > max_piece_size:
                max_piece_size = piece_size

            if max_piece_size == 5:
                return 5

        return max_piece_size

class HumanInput(Agent):

    def get_move(self, game):
        player = game.players[self.player_id]

        piece = self.pick_piece(player)

        corner = self.pick_corner(player, piece)

        move = self.pick_move(game, piece, corner)

        return move

    def pick_piece(self, player):

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

    def pick_corner(self, player, piece):
        
        moves = player.valid_moves.get_piece_moves(piece)
        corners = list({move.corner for move in moves})
        string = "Please pick a corner from the following by its index"
        strings = [f"{str(c.p2)}, {i}" for i, c in enumerate(corners)]
        string += "\n".join(strings)

        return self.pick_by_index(corners, string)


    def pick_move(self, game, piece, corner):
        moves = game.players[self.player_id].valid_moves.get_corner_piece_moves(corner, piece)
        moves = list(moves)
        for i, move in enumerate(moves):
            b = game.board.copy()
            print(f"Move {i}")
            b.update(move)
            b.display()

        string = f"pick a move in range [0, {len(moves)}]"
        return self.pick_by_index(moves, string)

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

