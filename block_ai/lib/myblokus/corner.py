""" This class defines a corner object as a collection of 2 Point objects. """

from block_ai.lib.myblokus import point

import logging

class Corner:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.diff = self.p2 - self.p1

    def get_rotation(self):
        if self.diff == Point(1, 1):
            return point.ident
        elif self.diff == Point(-1, 1):
            return point.rot270
        elif self.diff == Point(1, -1):
            return point.rot90
        elif self.diff == Point(-1, -1):
            return point.rot180
        else:
            raise ValueError(f"Invalid Diff: {corner.diff}")
