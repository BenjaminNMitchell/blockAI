class Move:
    
    def __init__(self, orientation, player_id, piece_id, corner):
        self.orientation = orientation
        self.player_id = player_id
        self.piece_id = piece_id
        self.corner = corner

    def get_footprint(self):
        return [p for p in self.orientation.points]
    
    def __repr__(self):
        o_repr = repr(self.orientation)
        c_repr = repr(self.corner)
        return f"""Move(orientation={o_repr},
                        player_id={self.player_id},
                        piece_id='{self.piece_id}',
                        corner={c_repr})"""
    
    def __eq__(self, other):
        for attr in ["orientation", "player_id", "piece_id", "corner"]:
            if not eval(f"self.{attr} == other.{attr}"):
                return False
        return True

    def __hash__(self):
        return hash((self.orientation, self.player_id, self.piece_id, self.corner))

    def __str__(self):
        return f"Player ID: {self.player_id}\nPiece ID:{self.piece_id}\n{self.orientation}"
