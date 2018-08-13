"""This Class defines a move in the Game Blokus."""

class Move:
    
    def __init__(self, orientation, player_id, piece_id, corner):

        self.orientation = orientation
        self.player_id = player_id
        self.piece_id = piece_id
        self.corner = corner
    
        if corner.p2 not in orientation.points:
            raise RuntimeError(f"Invalid move {str(self)}. Corner disconnected from pieces")

    def get_footprint(self):
        return self.orientation.points
    
    def __repr__(self):
        o_repr = repr(self.orientation)
        c_repr = repr(self.corner)
        return f"""Move(orientation={o_repr},
                        player_id={self.player_id},
                        piece_id='{self.piece_id}',
                        corner={c_repr})"""

    def __key(self):
        return (self.orientation, self.player_id)

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())

    def __str__(self):
        return f"Player ID: {self.player_id}\nPiece ID:{self.piece_id}\n{self.orientation}"
