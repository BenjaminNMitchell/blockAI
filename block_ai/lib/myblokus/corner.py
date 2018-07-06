"""This class defines a corner object as a collection of 2 Point objects."""

import logging
from .point import Point
from . import point


class Corner:
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.diff = self.p2 - self.p1
        self.validate_diff()

    def validate_diff(self):
        valid_diffs = [
            Point(-1, -1),
            Point(-1, 1),
            Point(1, -1),
            Point(1, 1),
        ]

        if self.diff not in valid_diffs:
            raise ValueError(f"Invalid Diff: {self.diff}")
           
    def get_rotation(self):
        if self.diff == Point(1, 1):
            return point.ident
        elif self.diff == Point(-1, 1):
            return point.rot90
        elif self.diff == Point(1, -1):
            return point.rot270
        else:
            return point.rot180

