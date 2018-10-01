"""This class defines a blokus piece as a collection of orientations."""

from .orientation import Orientation
from .corner import Corner
from . import point

import itertools

class Piece:

    def __init__(self, points):
        self.orientations = set()
        o_prime = Orientation(points)
        self.add_all_orientations(o_prime)

    def add_all_orientations(self, o_prime):
        self.add_both(o_prime)
        corners = o_prime.get_corners()
        for corner in corners:
            orientation = self.shift_orientation(o_prime, corner)
            rot = corner.get_rotation()
            orientation = Orientation(tuple([point.rot180(rot(p)) for p in orientation.points]))
            self.add_both(orientation)

    def add_both(self, orientation):
        self.orientations.add(orientation)
        self.orientations.add(orientation.flip())

    def shift_orientation(self, orientation, corner):
        c_prime = Corner((0, 0), (-1, -1))
        diff = point.subtract(c_prime.p1,  corner.p1)
        return Orientation([point.add(diff, p) for p in orientation.points])

    def get_orientation_prime(self):
        return min(self.orientations)

    def __len__(self):
        return len(self.get_orientation_prime())

    def __eq__(self, other):
        if isinstance(other, Piece):
            o_prime_1 = self.get_orientation_prime()
            o_prime_2 = other.get_orientation_prime()
            return o_prime_1 == o_prime_2
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "Piece:\n" + "\n".join([str(o) for o in self.orientations])
            
def gen_pieces():
    """Generates the pieces available to a player at the start of a game"""

    pieces = {
        'p1': Piece([(0, 0)]),
        'p2': Piece([(0, 0), (0, 1)]),
        'p3': Piece([(0, 0), (0, 1), (0, 2)]),
        'p4': Piece([(0, 0), (0, 1), (1, 1)]),
        'p5': Piece([(0, 0), (1, 0), (0, 1), (1, 1)]),
        'p6': Piece([(0, 0), (1, 0), (2, 0), (3, 0)]),
        'p7': Piece([(0, 0), (1, 0), (1, 1), (2, 1)]),
        'p8': Piece([(0, 0), (1, 0), (1, 1), (2, 0)]),
        'p9': Piece([(0, 0), (1, 0), (1, 1), (2, 1)]),
        'p10': Piece([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]),
        'p11': Piece([(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]),
        'p12': Piece([(0, 0), (1, 0), (2, 0), (2, 1), (3, 1)]),
        'p13': Piece([(0, 0), (1, 0), (2, 0), (1, 1), (2, 1)]),
        'p14': Piece([(0, 0), (1, 0), (2, 0), (0, 1), (2, 1)]),
        'p15': Piece([(0, 0), (1, 0), (2, 0), (3, 0), (2, 1)]),
        'p16': Piece([(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)]),
        'p17': Piece([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]),
        'p18': Piece([(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]),
        'p19': Piece([(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]),
        'p20': Piece([(0, 0), (1, 0), (1, 1), (2, 1), (1, 2)]),
        'p21': Piece([(0, 0), (1, 0), (1, 1), (1, -1), (2, 0)])
    }
    
    return pieces
