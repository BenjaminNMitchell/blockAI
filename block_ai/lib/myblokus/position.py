from .piece import gen_pieces
from . import point 
from .orientation import Orientation

BITSIZE = 400
ORIGIN = 210
UPPER_BOUND = (1 << 400) - 1
LEFT_SIDE_MASK = eval("0b" + ("1" + "0" * 19) * 20)
RIGHT_SIDE_MASK = eval("0b" + ("0" * 19 + "1") * 20)

pieces = gen_pieces()


class Position:

    def __init__(self, piece, adj, corners, quadrent, lower_bound):
        self.piece = piece
        self.adj = adj
        self.corners = corners
        self.piece = piece
        self.quadrent = quadrent
        self.lower_bound = lower_bound

    def shift(self, index):
        

        shift = index - ORIGIN 
        
        if shift > 0:
            
            new = self.piece << shift
            
            if new > UPPER_BOUND:
                return -1
            
        else:
            
            new = self.piece >> - shift

            if new < self.lower_bound:
                return -1

        if (LEFT_SIDE_MASK & new) and (RIGHT_SIDE_MASK & new):
            return -1

        return new
    
    def get_other_ints(self, index, piece):
        
        shift = index - ORIGIN
        
        if shift > 0:
            
            new_adj = (self.adj << shift) & UPPER_BOUND 
            new_corners = (self.corners << shift) & UPPER_BOUND 
        
        else:
            
            new_adj = self.adj >> - shift
            new_corners = self.corners >> - shift

        
        
        if (LEFT_SIDE_MASK & piece):
            
            new_adj = new_adj & ~ RIGHT_SIDE_MASK
            new_corners = new_corners & ~ RIGHT_SIDE_MASK
            
        if (RIGHT_SIDE_MASK & piece):
            
            new_adj = new_adj & ~ LEFT_SIDE_MASK
            new_corners = new_corners & ~ LEFT_SIDE_MASK
        
        return (new_adj, new_corners)

    def __hash__(self):
        return hash(self.piece)

    def __eq__(self, other):
        return self.piece == other.piece


def get_size(integer):
    
    i = integer
    count = 0
    while i > 0:
        mask = 1 << (i.bit_length() - 1)
        if i & mask:
            count += 1
            i -= mask 

    return count

def points_to_int(points):
    indices = sorted([20 * j + i for (i, j) in points], reverse=True)
    indices = [i + ORIGIN for i in indices]
    
    integer = 0
    
    for i in indices:
        integer |= 1 << i
    return integer

def get_min_val(i):
    
    size = get_size(i)

    while get_size(i >> 1) == size:
        i >>= 1

    return i

def fix_overflow(i):
    return i & UPPER_BOUND

positions = [ set() for i in range(21)]

for pid, p  in pieces.items():
    
    pid = int(pid[1:]) - 1
    for o in p.orientations:

        for q, rot in zip([1, 4, 3, 2], [point.ident,  point.rot90, point.rot180, point.rot270]):

            new_o = Orientation([rot(p) for p in o.points])

            piece = points_to_int(new_o.points)
            adj = points_to_int(new_o.get_border_points())
            corners = points_to_int([c.p2 for c in new_o.get_corners()])
            lower_bound = get_min_val(piece)
            positions[pid].add(Position(piece, adj, corners, q, lower_bound))

positions = [list(s) for s in positions]
