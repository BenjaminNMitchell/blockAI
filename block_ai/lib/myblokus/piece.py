"""This class defines a blokus piece as a collection of orientations."""

from block_ai.lib.myblokus.orientation import Orientation
from block_ai.lib.myblokus.point import Point
from block_ai.lib.myblokus import point

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
        """This doesn't work this link may hold the answer https://math.stackexchange.com/questions/180418/calculate-rotation-matrix-to-align-vector-a-to-vector-b-in-3d."""
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

p1 = Piece([Point(0, 0)])
p2 = Piece([Point(0, 0), Point(0, 1)])
p3_1 = Piece([Point(0, 0), Point(0, 1), Point(0, 2)])
p3_2 = Piece([Point(0, 0), Point(0, 1), Point(1, 1)])
p4_1 = Piece([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)])
p4_2 = Piece([Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)])
p4_3 = Piece([Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1)])
p4_4 = Piece([Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 0)]
# TODO implement remaining Pieces and add to gen_pieces

all_pieces = [p1,
            p2,
            p3_1, p3_2,
            p4_1, p4_2, p4_3, p4_4]


def gen_pieces():
    """ Generates the pieces available to a player at the start of a game """
    return all_pieces
