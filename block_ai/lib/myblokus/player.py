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
        
        if self.player_id == move.player_id:

            logging.info("Deleting piece id: %s", move.piece_id)
            del self.pieces[move.piece_id]
            
            logging.info("Adding border points")
            self.add_border_points(move)
            
        logging.info("Clearing moves")
        self.clear_moves(move)
        
    def add_border_points(self, move):
        invalid_points = move.orientation.get_border_points()
        invalid_points = list(filter(Board.on_board, invalid_points))
        self.invalid_points.update(invalid_points)

    def clear_moves(self, move):
        
        valid_moves = list(self.valid_moves.get_all())

        for m in valid_moves:

            if not self.is_move_valid(m):
                self.valid_moves.remove(m)
                
            elif self.overlap(m, move):
                self.valid_moves.remove(m)
 

    def overlap(self, m1, m2):
        overlap = m1.orientation.points & m2.orientation.points
        return len(overlap) != 0
    

    """
    def is_move_valid(self, move):
        try:
            self.validate_move(move)
            return True
        except RuntimeError as err:
            logging.debug(err)
            return False

    """
    
    def is_move_valid(self, move):

        if not self.has_piece(move.piece_id):
            return False

        overlap = self.invalid_points & move.orientation.points
        return len(overlap) == 0

    def get_score(self):
        return sum([len(p) for p in self.pieces.values()])

    def validate_move(self, move):
        if not self.has_piece(move.piece_id):
            raise RuntimeError(f"Move {move} invalid. Already played {move.piece_id}")

        new_points = move.orientation.points
        for p in move.get_footprint():
            if p in self.invalid_points:
                raise RuntimeError(f"Move {move} invalid. Includes invalid point {p}")

    def has_piece(self, piece_id):
        return piece_id in self.pieces

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

