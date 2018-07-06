""" This class defines a Player as a collection of
Pieces, valid moves, and invalid squares. """

from block_ai.lib.myblokus.piece import *
from block_ai.lib.myblokus.point import Point

import logging

class Player:

    def __init__(self, player_num):
        self.player_num = player_num
        self.pieces = gen_pieces()
        self.valid_moves = []
        self.no_go_squares = []

    def clear_moves(self, footprint):
        valid_moves = []

        for m in self.valid_moves:
            if not overlap(m, footprint):
                valid_moves.append(m)
                self.valid_moves = valid_moves

    def is_orientation_valid(self, points):
        for p in points:
            if p in self.no_go_squares:
                return False
        return True

    def add_move(self, move):
        self.valid_moves.append(move)

    def overlap(move, footprint):
    # TODO make this faster by sorting and incrementing
        for p in move.get_footprint():
            if p in footprint:
                return True
        return False
