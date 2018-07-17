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
            return point.rot270
        elif self.diff == Point(1, -1):
            return point.rot90
        else:
            return point.rot180

    def __repr__(self):
        
        return f"Corner(p1={repr(self.p1)}, p2={repr(self.p2)})"

    def __str__(self):
        return f"Corner\nP1: {self.p1}\nP2: {self.p2}"

    def __eq__(self, other):
        if not isinstance(other, Corner):
            raise TypeError(f"Cannot use operator = on Point and {type(other)}")
        return self.p1 == other.p1 and self.p2 == other.p2

    def __lt__(self, other):
        if not isinstance(other, Corner):
            raise TypeError(f"Cannot use operator = on Point and {type(other)}")
        
        if self.p1 == other.p1:
            return self.p2 < other.p2
        else:
            return self.p1 < other.p1

    def __hash__(self):
        return hash((self.p1, self.p2))
