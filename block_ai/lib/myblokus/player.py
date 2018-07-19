"""
This class defines a Player as a collection of.

Pieces, valid moves, and invalid squares.
"""

import logging
from .piece import gen_pieces
from .valid_moves import ValidMoves
from .board import Board


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
        
        invalid_points = move.get_footprint()
        
        if self.player_id == move.player_id:
            invalid_points += move.orientation.get_border_points()
            
        valid_moves = list(self.valid_moves.get_all())

        for m in valid_moves:
            #if m == test_move:
            #    logger.setLevel(logging.DEBUG)
                
            if not self.is_move_valid(m):
                self.valid_moves.remove(m)
                continue
                
            if self.overlap(m, move):
                self.valid_moves.remove(m)
                
            #logger.setLevel(logging.INFO)

    def overlap(self, m1, m2):
        for p in m1.orientation.points:
            if p in m2.orientation.points:
                return True
        return False
            
    def is_move_valid(self, move):
        try:
            self.validate_move(move)
            return True
        except RuntimeError as err:
            logging.debug(err)
            return False

    def validate_move(self, move):
        if not self.has_piece(move.piece_id):
            raise RuntimeError(f"Move {move} invalid. Already played {move.piece_id}")

        new_points = {move.orientation.points}
        overlap = self.invalid_points.intersection(new_points)
        if len(overlap) > 0:
            raise RuntimeError(f"Move {move} invalid. Includes invalid point {p}")

    def has_piece(self, piece_id):
        return piece_id in self.pieces

    def get_corners(self):
        return self.valid_moves.get_corners()

    def add_move(self, move):
        self.valid_moves.add(move)

    def has_moves(self):
        return len(self.valid_moves) > 0

    def get_valid_moves(self):
        return self.valid_moves.get_all()
