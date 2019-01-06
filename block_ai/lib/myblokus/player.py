"""
This class defines a Player as a collection of.

Pieces, valid moves, and invalid squares.
"""

import logging
from .valid_moves import ValidMoves
from copy import deepcopy
from .position import positions
from .move import Move

class Player:

    def __init__(self, player_id):
        self.player_id = player_id
        self.full = 0
        self.adj = 0
        self.corners = 0
        self.pieces = [True] * 21
        self.valid_moves = ValidMoves()

    def update(self, move, board):

        if self.player_id == move.player_id:
            self.pieces[move.piece_id] = False
            self.full |= move.piece
            self.adj  |= move.adj

            new_corners = move.corners & ~ self.corners
            self.add_moves(new_corners, board)

        self.clear_moves(move)

    def add_moves(self, new_corners, board):

        c = 1

        new_moves = set()

        for index in range(400):

            if new_corners & c:
                for i in range(21):

                    if self.pieces[i]:

                        for p in positions[i]:

                            shifted = p.shift(index)

                            if shifted != -1 and board.are_squares_free(shifted) and not shifted & self.adj:
                                (adj, corners) = p.get_other_ints(index, shifted)
                                new_moves.add(Move(shifted, adj, corners, self.player_id, i))
 
            c <<= 1
 
        self.valid_moves.push(new_moves)
 
        self.corners |= new_corners 

    def clear_moves(self, move):
 
        valid_moves = list(self.valid_moves.get_all())

        if self.player_id == move.player_id:
            bad_points = move.piece | move.adj
 
        else:
            bad_points = move.piece
 
        for m in valid_moves:
            if not self.pieces[m.piece_id] or m.piece & bad_points:
                self.valid_moves.remove(m)

    def pop(self, move):

        if self.player_id == move.player_id:

            self.pieces[move.piece_id] = True
            self.full = self.full & ~ move.piece
            self.corners.pop()
            self.adj.pop()
            self.valid_moves.pop()

        else:
            # do recalculate from new corner
            # Maybe track in valid moves ones that got errased in the current turn
            pass

    def is_move_valid(self, move):
        p = move.piece 
        return self.pieces[move.piece_id] and (not (p & self.adj)) and (p & self.corners)
 
    def has_moves(self):
        return len(self.valid_moves) > 0

    def get_score(self):
        sizes = [1, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        return sum([size for piece, size in zip(self.pieces, sizes) if piece])

    def get_valid_moves(self):
        return self.valid_moves.get_all()

