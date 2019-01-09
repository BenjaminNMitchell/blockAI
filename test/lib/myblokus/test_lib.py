from block_ai.lib.myblokus.move import Move
from block_ai.lib.myblokus.corner import Corner
from block_ai.lib.myblokus import point  
from block_ai.lib.myblokus.position import Position


def get_move(piece=None,  player_id=None, piece_id=None):
    
    if piece is None:
        piece = (14680067, 15393180614668, 18691697672208)

    if player_id is None:
        player = 0

    if piece_id is None:
        piece_id = 'p4'

    return Move(*piece, player_id, piece_id)
