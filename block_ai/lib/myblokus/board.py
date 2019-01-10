class Board:
    
    def __init__(self):
        self.board = 0
                
    def are_squares_free(self, piece):
        return not self.board & piece
    
    def assign(self, move):
        self.board = self.board | move.piece

    def unassign(self, move):
        self.board = self.board & ~ move.piece

    def __eq__(self, other):
        return self.board == other.board

    def copy(self):
        b = Board()
        b.board = self.board.copy()
        return b
