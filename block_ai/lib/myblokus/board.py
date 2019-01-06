class Board:
    
    def __init__(self):
        self.board = 0
                
    def are_squares_free(self, piece):
        return not self.board & piece
    
    def update(self, move):
        self.board = self.board | move.piece
            
    def copy(self):
        b = Board()
        b.board = self.board.copy()
        return b
