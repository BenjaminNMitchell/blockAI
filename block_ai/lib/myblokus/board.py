import numpy as np
import logging
from .board_view import BoardView
from block_ai.lib.myblokus.point import X, Y



class Board:
    SIDE_LENGTH = 20
    shape = (SIDE_LENGTH, SIDE_LENGTH)
    EMPTY = -1
    
    
    def __init__(self):
        self.board = np.full(self.shape, self.EMPTY)
        
    def update(self, move):
        for p in move.orientation.points:
            self.assign(p, move.player_id)
        
    def are_squares_free(self, orientation):
        for p in orientation.points:

            if not self.on_board(p):
                return False
           
            if not self.point_empty(p):
                return False

        return True

    def is_square_free(self, p):

        x, y = p

        if x >= self.SIDE_LENGTH or x < 0 or y >= self.SIDE_LENGTH or y < 0:
            return False

        if not self.board[y][x] == self.EMPTY:
            return False

        return True

    @classmethod
    def on_board(self, point):
        x, y = point
        return x < self.SIDE_LENGTH and x >= 0 and y < self.SIDE_LENGTH and y >= 0
    
    def point_empty(self, p):
        val = self.check(p)
        return val == self.EMPTY
    
    def check(self, point):
        x, y = point
        return self.board[y][x]
        
    def assign(self, point, value):
        if self.on_board(point):
            x, y = point
            self.board[y][x] = value
        else:
            logging.debug("%s off board not assigning", point)
            
    def __str__(self):
        return str(self.board)
    
    def copy(self):
        b = Board()
        b.board = self.board.copy()
        return b

    def display(self):
        vis = BoardView()
        vis.display(self.board)
