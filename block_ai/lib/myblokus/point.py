"""Functions to manipulate tupple which represent 2d points"""

X = 0
Y = 1

def get_adjacent(p):
    x, y = p
    return [
            (x - 1, y),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y)
        ]

def get_corners(p):
    x, y = p
    return [
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x + 1, y + 1)
    ]




def from_string(string):
    """Construct a Point object from a string representation."""
    return eval(string)

def ident(point):
    """Return a new Point object with the same coordinates."""
    x, y = point
    return x, y

def flip(point):
    """Return a new Point object reflexcted by the x axis."""
    
    x, y = point
    return (x, -y)

def rot90(point):
    """Return a new Point object rotated 90 degrees counter clockwise."""
    
    x, y = point
    return (y, -x)

def rot180(point):
    """Return a new Point object rotated 180 degrees counter clockwise."""
    
    x, y = point
    return ( -x, -y)

def rot270(point):
    """Return a new Point object rotated 270 degrees counter clockwise."""
    x, y = point
    return ( -y, x)

def add(p1, p2):
    """Add two points."""
    return (p1[X] + p2[X], p1[Y] + p2[Y])

def subtract(p1, p2):
    """Add two points."""
    return (p1[0] - p2[X], p1[Y] - p2[Y])

