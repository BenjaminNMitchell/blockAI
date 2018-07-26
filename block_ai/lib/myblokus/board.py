import numpy as np
import logging
#from .board_view import BoardView

class Board:
    SIDE_LENGTH = 20
    shape = (SIDE_LENGTH, SIDE_LENGTH)
    EMPTY = -1
    
    def __init__(self):
        self.board = np.full(self.shape, self.EMPTY)
        
    def update(self, move):
        for p in move.get_footprint():
            self.assign(p, move.player_id)
        
    def are_squares_free(self, orientation):
        for p in orientation.points:
            logging.info(f"Point: {p}")
            if not self.is_square_free(p):
                return False
        return True

    def is_square_free(self, p):
        if not self.on_board(p):
            return False
        if not self.point_empty(p):
            return False
        return True

    @classmethod
    def on_board(self, point):
        valid_points = range(0, self.SIDE_LENGTH)
        return point.x in valid_points and point.y in valid_points
    
    def point_empty(self, p):
        val = self.check(p)
        logging.debug(val)
        return val == self.EMPTY
    
    def check(self, point):
        return self.board[point.y][point.x]
        
    def assign(self, point, value):
        if self.on_board(point):
            logging.debug("assigning %s: %s", point, value)
            self.board[point.y][point.x] = value
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
