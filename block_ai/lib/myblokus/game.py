"""A game of Blokus."""

import logging
from . import point
from .player import Player
from .piece import gen_pieces
from .board import Board
from .corner import Corner
from .orientation import Orientation
from .move import Move

from copy import deepcopy

class Game:

    def __init__(self, set_start_moves=True):
        self.board = Board()
        self.player_pointer = 0
        self.players = [Player(i) for i in range(4)]

        self.init_corners = [Corner((-1, -1), (0, 0)),
                             Corner((-1, 20), (0, 19)),
                             Corner((20, 20), (19, 19)),
                             Corner((20, -1), (19, 0))]

        self.starting_points = [c.p1 for c in self.init_corners]

        self.move_history = []
        
        if set_start_moves:
            self.set_starting_moves()

        logging.info("Player Pointer: %s", self.player_pointer)
    
    
    def set_starting_moves(self):
        for i, c in enumerate(self.init_corners):
            self.add_corner_moves(c, i)

    def make_move(self, move):
        if not move.player_id == self.player_pointer:
            raise RuntimeError(f"Move: {move} not players turn")

        try:
            self.validate_move(move)
            self.update_state(move)
            self.move_history.append(move)
            self.set_next_player()
        except RuntimeError as err:
            logging.exception(err)

    def pop_moves(self):
        for p in self.move_history[-1].orientation.points:
            self.board.assign(p, Board.EMPTY)
        
        for player in self.players:
            player.pop_moves(self.move_history[-1])

        self.set_prev_player()
        self.move_history.pop()

            
    def update_state(self, move):
        self.board.update(move)
        
        for player in self.players:
            player.update(move)
            
        for corner in move.orientation.get_corners():
            self.add_corner_moves(corner, move.player_id)
 
    def add_corner_moves(self, corner, player_id):
        player = self.players[player_id]
        rotation = corner.get_rotation_game()
        
        if not Board.on_board(corner.p2):
            return
        
        for piece_id, piece in player.pieces.items():
            
            for orientation in piece.orientations:
                
                new_o = Orientation([point.add(corner.p2, rotation(p)) for p in orientation.points])
                try:
                    m = Move(new_o, player_id, piece_id, corner)

                    if self.is_move_valid(m):
                        player.add_move(m)
                except RuntimeError as err:
                    err_msg = f"Move: {m} invalid: original_orientation: {orientation}"
                    logging.exception(err_msg)

    def is_move_valid(self, move):

        if not self.board.are_squares_free(move.orientation):
            return False
        play_point = move.corner.p1

        if play_point not in self.starting_points:
            val = self.board.check(play_point)
            if val != move.player_id:
                return False

        if not self.players[move.player_id].is_move_valid(move):
            return False

        return True
        
    def validate_move(self, move):
        
        if not self.board.are_squares_free(move.orientation):
            raise RuntimeError(f"Move: {move} squares are not free")
        
        play_point = move.corner.p1
        logging.info("play point: %s", play_point)

        if play_point not in self.starting_points:
            logging.info("Not in starting_points")
            val = self.board.check(play_point)
            logging.info("Value at play_point: %s", val)
            logging.info("Move player_id: %s", move.player_id)
            if val != move.player_id:
                raise RuntimeError(f"Move: {move} player: {move.player_id} does not occupy corner starting point {play_point}")
                
        self.players[move.player_id].validate_move(move)

    def set_next_player(self):
        logging.info("Advancing player")
        self.player_pointer = self.get_next_player()

    def get_next_player(self):
        ptr = self.player_pointer

        for i in range(4):
            ptr = self.advance(ptr)
            if self.players[ptr].has_moves():
                return ptr

        raise GameEnd("Game Over")

    def set_prev_player(self):
        logging.info("Retreating Player")
        logging.info(f"Current Player Pointer: {self.player_pointer}")
        self.player_pointer = self.get_prev_player()
        logging.info(f"New Player Pointer: {self.player_pointer}")

    def get_prev_player(self):
        
        turn_nums = [len(self.move_history) - i for i in range(4)]
       
        ptr = self.player_pointer

        logging.info(f"Turn nums: {turn_nums}")
        for i in range(4):

            logging.info(f"I: {i}")
            if turn_nums[i]  == 0:
                raise ValueError("No prior turns")
            
            
            ptr = self.retreate(ptr)

            logging.info(f"New Pointer {ptr}")

            if self.players[ptr].has_moves():
                logging.info(f"Player: {ptr} has moves")
                return ptr
            else:
                logging.info(f"Player: {ptr} does not have moves!")

    def advance(self, player_id):
        return (player_id + 1) % 4

    def retreate(self, player_id):
        return (player_id - 1) % 4

    def get_players_moves(self, player_id):
        return self.players[player_id].get_valid_moves()

    def display(self, player_id=None, bad_move=None):
        board = self.board
        
        if player_id is not None:
            board = self.fill_player_pov(board, player_id)
            
        if bad_move is not None:
            board = self.fill_bad_move(board, bad_move)

        board.display()

    def copy(self):
        new_game = Game(set_start_moves=False)
        new_game.board = deepcopy(self.board)
        new_game.players = deepcopy(self.players)
        new_game.move_history = deepcopy(self.move_history)
        return new_game

    def get_scores(self):
        return { i: p.get_score() for i, p in enumerate(self.players)}
            
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
