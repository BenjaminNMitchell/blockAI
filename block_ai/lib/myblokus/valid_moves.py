"""Valid Moves store."""

import itertools
from copy import deepcopy
import logging


class ValidMoves:
    
    def __init__(self):
        self.turn_moves = [{}]
        self.valid_moves = self.turn_moves[-1]
        
    def next_move(self):
        
        self.turn_moves.append(self.get_vm_copy())
        self.valid_moves = self.turn_moves[-1]
    
    def get_vm_copy(self):
        new_dict = {}
        for name1, d_outer in self.valid_moves.items():
            new_dict[name1] = {}

            d_set1 = new_dict[name1]
 
            for name2, l in d_outer.items():
                
                d_set1[name2] = l.copy()

        return new_dict
    
    def prev_move(self):
        
        _ = self.turn_moves.pop()
        self.valid_moves = self.turn_moves[-1]

    #TODO Use (Corner, Piece) --> Move
    def add(self, move):
        try:
            corner_moves = self.valid_moves[move.corner]
            try:
                corner_moves[move.piece_id].append(move)
            except KeyError:
                corner_moves[move.piece_id] = [move]
        except KeyError:
            self.valid_moves[move.corner] = {}
            corner_moves = self.valid_moves[move.corner]
            corner_moves[move.piece_id] = [move]
    
    def remove(self, move):
        logging.info(f"Length 0 1: {len(self.turn_moves[0])}")
        self.valid_moves[move.corner][move.piece_id].remove(move)
        
        logging.info(f"Length 0 2: {len(self.turn_moves[0])}")
        if self.valid_moves[move.corner][move.piece_id] == []:
            del self.valid_moves[move.corner][move.piece_id]
 
        logging.info(f"Length 0 3: {len(self.turn_moves[0])}")
        if self.valid_moves[move.corner] == {}:
            del self.valid_moves[move.corner]

    def get_all(self):
        gens = [self.get_corner_moves(c) for c in self.get_corners()]
        for m in itertools.chain(*gens):
            yield m

    def get_corner_moves(self, corner):
        for piece_id in self.valid_moves[corner]:
            for m in self.valid_moves[corner][piece_id]:
                yield m

    def get_corners(self):
        return self.valid_moves.keys()
    
    def get_corner_piece_moves(self, corner, piece_id):
        return filter(lambda m: m.piece_id == piece_id, self.get_corner_moves(corner))
            
    def get_piece_moves(self, piece_id):
        return filter(lambda m: m.piece_id == piece_id, self.get_all())

    def __len__(self):
        length = 0
        for val in self.valid_moves.values():
            for l in val.values():
                length += len(l)
        return length

    def copy(self):
        copy = ValidMoves()
        copy.valid_moves = deepcopy(self.valid_moves)
        return copy





#TODO figure out why this dosen't work 
'''
class ValidMoves:
    
    def __init__(self):
        self.valid_moves = set()

    #TODO Use (Corner, Piece) --> Move
    def add(self, move):
        self.valid_moves.add(move)
    
    def remove(self, move):
        self.valid_moves.remove(move)
        
    def get_all(self):
        return list(self.valid_moves)

    def get_corner_moves(self, corner):
        for move in self.valid_moves:
            if move.corner == corner:
                yield move

    def get_corners(self):
        return {m.corner for m in self.valid_moves}
    
    def get_corner_piece_moves(self, corner, piece_id):
        
        for move in self.valid_moves:
            if move.corner == corner and move.piece_id == piece_id:
                yield move
            
    def get_piece_moves(self, piece_id):
        for move in self.valid_moves:
            if move.piece_id == piece_id:
                yield move

    def __len__(self):
        
        return len(self.valid_moves)

    def copy(self):
        copy = ValidMoves()
        copy.valid_moves = deepcopy(self.valid_moves)
        return copy

'''
