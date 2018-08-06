"""This class defines a single orientation of a piece."""

from .point import Point
from .corner import Corner
import logging

class Orientation():
    """The orientation calss stores a collection of relative points."""

    def __init__(self, points):
        #  must be sorted for equality comparison

        self.points = tuple(sorted(points))

    def get_border_points(self):
        """Return all points adjacent to the orientation."""

        return self.__get_related_points("get_adjacent")

    def get_corners(self):
        """Return all points which only share a corner with this orientation."""

        border_points = set(self.get_border_points())
        
        played_point = {Point(-1, -1)} # point we played from
        invalid_corners = border_points | played_point 
        
        related_corners = set()
        for point in self.points:
            relatives = point.get_corners()
            valid_relatives = set(filter(lambda p: p not in self.points, relatives))
            valid_relatives = valid_relatives - invalid_corners
            valid_corners = set([Corner(point, relative) for relative in valid_relatives])
            related_corners = related_corners | valid_corners
   
        return related_corners

    def __get_related_points(self, func_name):
        """Generate points related to this orientation."""

        related_points = set()
        for point in self.points:
            relatives = eval(f"point.{func_name}()")
            valid_relatives = set(filter(lambda p: p not in self.points, relatives))
            related_points = related_points | valid_relatives
        return related_points

    def get_invalid_points(self):
        
        adjacent_points = self.get_border_points()        
        return [p.copy() for p in self.points + tuple(adjacent_points)]

    def is_valid(self) -> bool:
        """Return true if this is a valid orientation and false otherwise."""

        invalid_points = [
            Point(-1, -1),  # Point we played from
            Point(0, -1),   # Adjacent point
            Point(-1, 0),   # Adjacent point
        ]

        for p in self.points:
            if p in invalid_points:
                return False
        return True

    def flip(self):
        new_points = [Point(p.y, p.x) for p in self.points]
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

        if len(self) != len(other):
            return False
        for a, b in zip(self.points, other.points):
            if a != b:
                return False
        return True

    def __str__(self) -> str:
        """Return a string representation of this oriention."""

        # return ", ".join([str(p) for p in self.points])
        return str(self.points)

    def __repr__(self) -> str:
        """Return a string representation of this oriention."""

        # return ", ".join([str(p) for p in self.points])
        return f"Orientation({str(self)})"

