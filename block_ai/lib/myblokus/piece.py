"""This class defines a blokus piece as a collection of orientations."""

from .orientation import Orientation
from .point import Point
from . import point

import itertools
import logging

class Piece:

    def __init__(self, points):
        self.orientations = set()
        o_prime = Orientation(points)
        self.add_all_orientations(o_prime)
        self.orientations = sorted(self.orientations)

    def add_all_orientations(self, o_prime):
        self.orientations.add(o_prime)
        corners = o_prime.get_piece_corners()
        for corner in corners:
            orientation = self.shift_orientation(o_prime, corner)
            self.add_rotations(orientation)

    def shift_orientation(self, orientation, corner_point):
        c_prime = Point(0, 0)
        diff = c_prime - corner_point
        return Orientation([diff + p for p in orientation.points])

    def add_rotations(self, orientation):
        for transform in self.gen_transforms():
            orientation = Orientation(tuple([transform(point) for point in orientation.points]))
            if orientation.is_valid():
                self.orientations.add(orientation)

    def gen_transforms(self):
        flips = [point.ident, point.flip]
        rots = [point.ident, point.rot90, point.rot180, point.rot270]
        for f, r in itertools.product(flips, rots):
            yield lambda x: f(r(x))

    def get_orientation_prime(self):
        return min(self.orientations)

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

    def __repr__(self):
        return f"Piece({str(self.orientations)})"

def gen_pieces():
    """Generates the pieces available to a player at the start of a game"""
    # Numbered according to graphic included in
    p1 = Piece([Point(0, 0)])

    p2 = Piece([Point(0, 0), Point(1, 0)])

    p3 = Piece([Point(0, 0), Point(1, 0), Point(2, 0)])
    p4 = Piece([Point(0, 0), Point(1, 0), Point(1, 1)])

    p5 = Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)])
    p6 = Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1)])
    p7 = Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(1, 1)])
    p8 = Piece([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)])
    p9 = Piece([Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1)]

    p10 = Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)], Point(4, 0))
    p11 = Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)], Point(3, 1))
    p15 = Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)], Point(2, 1))
    p12 = Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1)], Point(3, 1))
    p17 = Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1)], Point(2, 2))
    p16 = Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(1, 1)], Point(1, 2))
    p13 = Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(1, 1)], Point(2, 1))
    p18 = Piece([Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1)], Point(2, 2))
    p20 = Piece([Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1)], Point(1, 2))
    p21 = Piece([Point(0, 1), Point(1, 1), Point(1, 2), Point(1, 0)], Point(2, 1))
    p14 = Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(0, 1)], Point(2, 1))
    p19 = Piece([Point(0, 0), Point(0, 1), Point(1, 1), Point(2, 1)], Point(2, 2))

    return [p1,
            p2,
            p3, p4,
            p5, p6, p7, p8, p9,
            p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21
           ]
