"""This class defines a blokus piece as a collection of orientations."""

from .orientation import Orientation
from .corner import Corner
from .point import Point
from . import point

import itertools
import logging


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
            orientation = Orientation(tuple([rot(point) for point in orientation.points]))
            self.add_both(orientation)

    def add_both(self, orientation):
        self.orientations.add(orientation)
        self.orientations.add(orientation.flip())

    def shift_orientation(self, orientation, corner):
        c_prime = Corner(Point(0, 0), Point(-1, -1))
        diff = c_prime.p1 - corner.p1
        return Orientation([diff + p for p in orientation.points])

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
        return "\n".join([str(o) for o in self.orientations])
            
def gen_pieces():
    """Generates the pieces available to a player at the start of a game"""

    pieces = {
        'p1': Piece([Point(0, 0)]),
        'p2': Piece([Point(0, 0), Point(0, 1)]),
        'p3': Piece([Point(0, 0), Point(0, 1), Point(0, 2)]),
        'p4': Piece([Point(0, 0), Point(0, 1), Point(1, 1)]),
        'p5': Piece([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]),
        'p6': Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)]),
        'p7': Piece([Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1)]),
        'p8': Piece([Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 0)]),
        'p9': Piece([Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1)]),
        'p10': Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0), Point(4, 0)]),
        'p11': Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0), Point(3, 1)]),
        'p12': Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1), Point(3, 1)]),
        'p13': Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(1, 1), Point(2, 1)]),
        'p14': Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(0, 1), Point(2, 1)]),
        'p15': Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0), Point(2, 1)]),
        'p16': Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(1, 1), Point(1, 2)]),
        'p17': Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1), Point(2, 2)]),
        'p18': Piece([Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1), Point(2, 2)]),
        'p19': Piece([Point(0, 0), Point(0, 1), Point(1, 1), Point(2, 1), Point(2, 2)]),
        'p20': Piece([Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1), Point(1, 2)]),
        'p21': Piece([Point(0, 0), Point(1, 0), Point(1, 1), Point(1, -1), Point(2, 0)])
    }
    
    return pieces
