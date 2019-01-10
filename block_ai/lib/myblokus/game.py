"""A game of Blokus."""

import logging
from copy import deepcopy

from .player import Player
from .board import Board
from .move import Move
from .game_view import GameView

class Game:

    def __init__(self):
        self.board = Board()
        self.move_history = []
        self.player_pointer = 0
        self.players = [Player(i, self.board) for i in range(4)]

    def make_move(self, move):
        if not move.player_id == self.player_pointer:
            raise RuntimeError(f"Move: {move} not players turn")

        try:
            if self.is_move_valid(move):
                self.update_state(move)
                self.move_history.append(move)
                self.set_next_player()
        except RuntimeError as err:
            logging.exception(err)

    def pop(self):
        logging.info("Poping Moves")
        
        if len(self.move_history) == 0:
            raise RuntimeError("Cannot pop_moves already at initial state")
        
        last_move = self.move_history.pop()

        logging.info(f"Last Move: {last_move}")
        logging.info("Unassigning Moves points from board")
        
        self.board.unassign(last_move)
        
        for i, player in enumerate(self.players):
            logging.info(f"poping player {i}")
            player.pop(last_move)

        self.player_pointer = last_move.player_id


    def update_state(self, move):
        
        self.board.assign(move)
        
        for player in self.players:
            player.update(move, self.board)

    def is_move_valid(self, move):
        return self.board.are_squares_free(move.piece) and self.players[move.player_id].is_move_valid(move)
         
        
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

        for i in range(4):
            
            self.player_pointer = (self.player_pointer + 1) % 4
            if self.players[self.player_pointer].has_moves():
                return

    def get_players_moves(self, player_id):
        return self.players[player_id].get_valid_moves()

    def copy(self):
        new_game = Game(set_start_moves=False)
        new_game.board = deepcopy(self.board)
        new_game.players = deepcopy(self.players)
        new_game.move_history = deepcopy(self.move_history)
        return new_game

    def __eq__(self, other):
        
        return (self.board == other.board and
                self.players == other.players and
                self.move_history == other.move_history and
                self.player_pointer == other.player_pointer)
    
    def has_moves(self):
        for p in self.players:
            if p.has_moves():
                return True
        return False

    def get_scores(self):
        return { i: p.get_score() for i, p in enumerate(self.players)}
            
 
    def display(self, player_id=None):
        gv = GameView()
        gv.display(self)

"""       
    def display(self, player_id=None):
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
"""
