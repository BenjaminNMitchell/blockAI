import itertools

class Point:
    """Holds x and y cordinates"""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @property
    def x(self) -> int:
        """The x coordinate of this point."""

        return self.__x

    @x.setter
    def x(self, x: int):
        """Setter for the x coordinate of this point."""

        if type(x) is not int:
            raise TypeError("x must be an int")
        self.__x = x

    @property
    def y(self) -> int:
        """The y coordinate of this point."""

        return self.__y

    @y.setter
    def y(self, y: int):
        """Setter for the y coordinate of this point."""

        if type(y) is not int:
            raise TypeError("y must be an int")
        self.__y = y
    

    def get_adjacent(self):
        """Get all points at distance one."""

        return [
                Point(self.x - 1, self.y),
                Point(self.x, self.y - 1),
                Point(self.x, self.y + 1),
                Point(self.x + 1, self.y)
            ]

    def get_corners(self):
        """Get all diagonal points."""

        gen = itertools.product([-1, 1], [-1, 1])
        return [Point(self.x + a, self.y + b) for a, b in gen]

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other) -> bool:
        return not self == other

    def __lt__(self, other) -> bool:
        if self == other:
            return True
        elif self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x

    def __gt__(self, other) -> bool:
        return not self < other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def copy(self):
        return Point(self.x, self.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point{str(self)}"

def from_string(string):
    """Construct a Point object from a string representation."""
    return eval("Point" + string)
 
def ident(point):
    """Return a new Point object with the same coordinates."""
    return Point(point.x, point.y)

def flip(point):
    """Return a new Point object reflexcted by the x axis."""
    return Point(point.x, - point.y)

def rot90(point):
    """Return a new Point object rotated 90 degrees counter clockwise."""
    return Point(point.y, -point.x)

def rot180(point):
    """Return a new Point object rotated 180 degrees counter clockwise."""
    return Point( -point.x, -point.y)

def rot270(point):
    """Return a new Point object rotated 270 degrees counter clockwise."""
    return Point( -point.y, point.x)

