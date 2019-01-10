class ValidMoves:
    
    def __init__(self):
        self.valid_moves = [set()]
        
    def push(self, *, invalid_moves=set(), new_moves=None):

        if new_moves:
            self.valid_moves.append((self.valid_moves[-1] | new_moves) - invalid_moves)
        else:
            self.valid_moves.append(self.valid_moves[-1] - invalid_moves)
    
    def pop(self):
        self.valid_moves.pop()

    def remove(self, move):
        self.valid_moves[-1].remove(move)
        
    def get_all(self):
        return list(self.valid_moves[-1])

    def __len__(self):
        return len(self.valid_moves[-1])

    def __eq__(self, other):
        return self.valid_moves == other.valid_moves
     
