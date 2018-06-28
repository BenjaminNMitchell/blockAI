"""This class defines a blokus piece as a collection of orientations."""

from block_ai.lib.myblokus.orientation import Orientation
from block_ai.lib.myblokus.point import Point
from block_ai.lib.myblokus import point

import itertools

class Piece:

    def __init__(self, points):
        self.orientations = set()
        o_prime = Orientation(points)
        self.add_all_orientations(o_prime)
        self.orientations = sorted(self.orientations)

    def add_all_orientations(self, o_prime):
        corners = o_prime.get_corner_points()
        for corner in corners:
            orientation = self.shift_orientation(o_prime, corner)
            self.add_rotations(orientation)

    def shift_orientation(self, orientation, corner_point):
        """This doesn't work this link may hold the answer https://math.stackexchange.com/questions/180418/calculate-rotation-matrix-to-align-vector-a-to-vector-b-in-3d."""
        c_prime = Point(-1, -1)
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
        for o in self.orientations:
            # will just return the first one
            return o

    def __eq__(self, other):
        if len(self.orientations) != len(other.orientations):
            return False
        for o in self.orientations:
            if o not in other.orientations:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "\n".join([str(o) for o in self.orientations])
