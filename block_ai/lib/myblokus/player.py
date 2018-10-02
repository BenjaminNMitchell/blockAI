"""
This class defines a Player as a collection of.

Pieces, valid moves, and invalid squares.
"""

import logging
from .piece import gen_pieces
from .valid_moves import ValidMoves
from .board import Board
from copy import deepcopy

class Player:

    def __init__(self, player_id):
        self.player_id = player_id
        self.pieces = gen_pieces()
        self.valid_moves = ValidMoves()
        self.invalid_points = set()
        
    def update(self, move):
        logging.info("Updating player %s", self.player_id)

        self.valid_moves.next_move()
        
        if self.player_id == move.player_id:

            del self.pieces[move.piece_id]
            
            self.add_border_points(move)
            
        self.clear_moves(move)

    def pop_moves(self, move):
        # TODO add code to add last played piece back if we played it
        # revert valid moves
        # make similar stackset thing for invalid_points

        raise ValueError("You left off here")
        
        
    def add_border_points(self, move):
        invalid_points = move.orientation.get_border_points()
        invalid_points = list(filter(Board.on_board, invalid_points))
        self.invalid_points.update(invalid_points)

    def clear_moves(self, move):
        
        valid_moves = list(self.valid_moves.get_all())

        for m in valid_moves:
                
            if not self.is_move_valid(m):
                self.valid_moves.remove(m)
                continue
                
            if self.overlap(m, move):
                self.valid_moves.remove(m)
                

    def overlap(self, m1, m2):
        return not m1.orientation.points.isdisjoint(m2.orientation.points)

    def is_move_valid(self, move):
        if not move.piece_id in self.pieces:
           return False

        return move.orientation.points.isdisjoint(self.invalid_points)

    def get_score(self):
        return sum([len(p) for p in self.pieces.values()])

    def validate_move(self, move):
        if not move.piece_id in self.pieces:
            raise RuntimeError(f"Move {move} invalid. Already played {move.piece_id}")
        
        #TODO optimize this
        new_points = move.orientation.points
        for p in new_points:
            if p in self.invalid_points:
                raise RuntimeError(f"Move {move} invalid. Includes invalid point {p}")

    def get_corners(self):
        return self.valid_moves.get_corners()

    def add_move(self, move):
        self.valid_moves.add(move)

    def copy(self):
        copy = Player(self.player_id)
        copy.valid_moves = self.valid_moves.copy()
        copy.pieces = deepcopy(self.pieces)
        copy.invalid_points = deepcopy(self.invalid_points)
        return copy

    def has_moves(self):
        return len(self.valid_moves) > 0

    def get_valid_moves(self):
        return self.valid_moves.get_all()

