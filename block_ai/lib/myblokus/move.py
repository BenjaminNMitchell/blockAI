"""This Class defines a move in the Game Blokus."""

class Move:
    
    def __init__(self, piece, adj, corners, player_id, piece_id):
        self.piece = piece
        self.adj = adj
        self.corners = corners
        self.player_id = player_id
        self.piece_id = piece_id
        
    def __hash__(self):
        return hash(self.piece)

    def __eq__(self, other):
        return self.piece == other.piece

    def get_size(self):
       return [1, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5][self.piece_id]
        
       
