"""A game of Blokus."""

import logging
from .player import Player
from .piece import gen_pieces
from .board import Board
from .corner import Corner
from .point import Point
from .orientation import Orientation
from .move import Move

class Game:

    def __init__(self):
        self.board = Board()
        self.player_pointer = 0
        self.players = [Player(i) for i in range(4)]
        self.set_starting_moves()
        self.move_history = []
        logging.info("Player Pointer: %s", self.player_pointer)
    
    def set_starting_moves(self):
        corners = [Corner(Point(-1, -1), Point(0, 0)),
                   Corner(Point(-1, 20), Point(0, 19)),
                   Corner(Point(20, 20), Point(19, 19)),
                   Corner(Point(20, -1), Point(19, 0))]

        for i, c in enumerate(corners):
            self.add_corner_moves(c, i)

    def make_move(self, move):
        logging.info("Making move: %s", move)
        if not move.player_id == self.player_pointer:
            raise RuntimeError(f"Move: {move} not players turn")

        try:
            self.validate_move(move)
            self.update_state(move)
            self.move_history.append(move)
            self.set_next_player()
        except RuntimeError as err:
            logging.exception(err)

    def update_state(self, move):
        self.board.update(move)
        
        for player in self.players:
            player.update(move)
            
        for corner in move.orientation.get_corners():
            self.add_corner_moves(corner, move.player_id)
 
    def add_corner_moves(self, corner, player_id):
        player = self.players[player_id]
        rotation = corner.get_rotation()
        
        if not Board.on_board(corner.p2):
            logging.info("Corner %s is off board", corner)
            return
        
        logging.info("Adding corner %s moves", corner)
        for piece_id, piece in player.pieces.items():
            
            for orientation in piece.orientations:
                logging.debug("Examining orientation: %s", orientation)
                
                new_o = Orientation([corner.p2 + rotation(p) for p in orientation.points])
                logging.debug("New orientation: %s", new_o)
                m = Move(new_o, player_id, piece_id, corner)

                if self.is_move_valid(m):
                    logging.debug("Adding Move: %s", m)
                    player.add_move(m)

    def is_move_valid(self, move):
        try:
            self.validate_move(move)
            return True
        except RuntimeError as err:
            logging.debug(err)
            return False
    
    def validate_move(self, move):
        
        if not self.board.are_squares_free(move.orientation):
            raise RuntimeError(f"Move: {move} squares are not free")

        self.players[move.player_id].validate_move(move)
    
    
    def set_next_player(self):
        logging.info("Advancing player")
        self.player_pointer = self.get_next_player()

    def get_next_player(self):
        ptr = self.player_pointer
        logging.info("starting at %s", ptr)
        for i in range(4):
            ptr = self.advance(ptr)
            if self.players[ptr].has_moves():
                logging.info("returning %s", ptr)
                return ptr
        raise GameEnd("Game Over")
        
    
    def advance(self, player_id):
        return (player_id + 1) % 4

    def get_players_moves(self, player_id):
        return self.players[player_id].get_valid_moves()
    
    def display(self, player_id=None, bad_move=None):
        board = self.board
        
        if player_id is not None:
            board = self.fill_player_pov(board, player_id)
            
        if bad_move is not None:
            board = self.fill_bad_move(board, bad_move)

        board.display()

    def fill_player_pov(self, board, player_id):
        board = board.copy()
        
        adjacent_fill = 4
        corner_fill = 5
        
        for p in self.players[player_id].invalid_points:
            if board.point_empty(p):
                board.assign(p, adjacent_fill)
            
        for corner in self.players[player_id].get_corners():
            if board.point_empty(corner.p2):
                board.assign(corner.p2, corner_fill)
        return board

    def fill_bad_move(self, board, move):
        bad_fill = 6
        
        board = board.copy()

        for p in move.orientation.points:
            board.assign(p, bad_fill)
        return board
    
class GameEnd(Exception):
    pass