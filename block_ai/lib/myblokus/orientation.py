"""This class defines a single orientation of a piece."""

from . import point
from .corner import Corner

class Orientation():
    """The orientation calss stores a collection of relative points."""

    def __init__(self, points):
        #  must be sorted for equality comparison

        self.points = frozenset(points)

    def get_border_points(self):
        """Return all points adjacent to the orientation."""

        border_points = set()

        for p in self.points:
        
            border_points.update(point.get_adjacent(p))

        return border_points - self.points
            
    def get_corners(self):
        """Return all points which only share a corner with this orientation."""

        
        corner_points = set()

        for p in self.points:
            corners = [Corner(p, c) for c in point.get_corners(p)] 
            corner_points.update(corners)
        
        invalid_points = self.get_border_points()
        invalid_points.update(self.points)
        invalid_points.add((-1, -1))
        
        return {c for c in corner_points if c.p2 not in invalid_points}

    def get_invalid_points(self):       
        adjacent_points = self.get_border_points()        
        return [(p[0], p[1]) for p in self.points + tuple(adjacent_points)]

    def is_valid(self) -> bool:
        """Return true if this is a valid orientation and false otherwise."""

        invalid_points = [
            (-1, -1),  # Point we played from
            (0, -1),   # Adjacent point
            (-1, 0),   # Adjacent point
        ]

        for p in invalid_points:
            if p in self.points:
                return False
        return True

    def flip(self):
        new_points = [(p[1], p[0]) for p in self.points]
        return Orientation(new_points)
 
    def __hash__(self) -> int:
        """Return a hash value for this orientation."""

        return hash(self.points)

    def __len__(self):
        """Return the number of points in this orientation."""

        return len(self.points)   

    def __lt__(self, other) -> bool:
        """Return true if this orientation has a smaller point false otherwise."""

        if len(self) != len(other):
            return len(self) < len(other)

        for a, b in zip(self.points, other.points):
            if a == b:
                continue
            return a < b

    def __eq__(self, other) -> bool:
        """Returns true if this orientation contains all the same points as the other."""
        return len(self.points) == len(other.points) and self.points.issubset(other.points)

    def __str__(self) -> str:
        """Return a string representation of this oriention."""

        return "Orientation:\n" +  "\n".join([str(p) for p in self.points])
        

    def __repr__(self) -> str:
        """Return a string representation of this oriention."""


        inner = ", ".join([repr(p) for p in self.points])
        return f"Orientation(({inner}))"

