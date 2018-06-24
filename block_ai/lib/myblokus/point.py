class Point:
    """Holds x and y cordinates"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_adjacent(self):
        return [Point(self.x, self.y + 1),
                Point(self.x, self.y - 1),
                Point(self.x + 1, self.y),
                Point(self.x - 1, self.y)]
        
    def get_corners(self):
        gen = itertools.product([1, -1], [1, -1])
        return [Point(self.x + a, self.y + b) for a, b in gen]
            
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __gt__(self, other):
        if self == other:
            return True
        elif self.x + self.y > other.x + other.y:
            return True
        else:
            if self.x == other.x:
                return self.y > other.y
            else:
                return self.x > self.y
            
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
            
    def __lt__(self, other):
        return self.__gt__(other)

