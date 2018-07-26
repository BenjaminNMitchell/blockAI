from block_ai.lib.myblokus.move import Move
from block_ai.lib.myblokus.corner import Corner
from block_ai.lib.myblokus.point import Point
from block_ai.lib.myblokus.orientation import Orientation


def get_move(orientation=None, player_id=None, piece_id=None, corner=None):

    if orientation is None:
        orientation = get_orientation()

    if player_id is None:
        player = 0

    if piece_id is None:
        piece_id = 'p4'

    if corner is None:
        corner = get_corner()

    return Move(orientation, player_id, piece_id, corner)


def get_orientation():

    points = (
        Point(0, 0),
        Point(0, 1),
        Point(1, 1)
        )

    return Orientation(points)

def get_corner():

    return Corner(Point(-1, -1), Point(0, 0))
