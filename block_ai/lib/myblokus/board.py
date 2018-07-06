"""This class defines a blokus board."""

from .piece import Piece
from .point import Point
from .player import Player
from .orientation import Orientation
from .corner import Corner

import numpy as np
import matplotlib.pyplot as plt


class Board:
    SIDE_LENGTH = 20
    EMPTY = 0

    def __init__(self):
        shape = (self.SIDE_LENGTH, self.SIDE_LENGTH)
        self.board = np.zeros(shape)
        self.player_pointer = 0
        self.players = [Player(i) for i in range(4)]
        self.set_starting_moves()

    def set_starting_moves(self):
        corners = [Corner(Point(-1, -1), Point(0, 0)),
                   Corner(Point(-1, 20), Point(0, 19)),
                   Corner(Point(20, 20), Point(19, 19)),
                   Corner(Point(20, -1), Point(19, 0))]

        for i, c in enumerate(corners):
            self.add_valid_moves(c, i + 1)

    def add_valid_moves(self, corner, player_id):

        player = self.get_player(player_id)
        rotation = corner.get_rotation()
        for piece in player.pieces:
            for orientation in piece.orientations:
                points = [corner.p2 + rotation(p) for p in orientation.points]

                if not self.is_orientation_valid(points):
                    continue

                if not player.is_orientation_valid(points):
                    continue

                player.add_move(Orientation(points))


    def make_move(self, move):
        if is_orientation_valid(move):
            self.update_state(move)
        else:
            self.log_error(move)

    def is_orientation_valid(self, points):
        for p in points:
            if not self.on_board(p):
                return False
            if not self.point_empty(p):
                return False
        return True


    def on_board(self, point):
        valid_points = range(0, self.SIDE_LENGTH)
        return point.x in valid_points and point.y in valid_points

    def update_state(self, move):
        player = move.player
        player.pieces.remove(move.piece)
        for p in move.get_footprint():
            self.assign(p, player)

    def point_empty(self, p):
        return self.check(p) == self.EMPTY

    def get_player(self, player):
        return self.players[player - 1]

    def check(self, point):
        return self.board[point.x][point.y]

    def assign(self, point, value):
        self.board[point.x][point.y] = value

    def __str__(self):
        return str(self.board)

    def display(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_aspect('equal')
        plt.imshow(self.board, origin='lower')
        plt.show()

    def visualize_move(self, orientation):
        NEW_MOVE = 5
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_aspect('equal')
        next_board = self.board.copy()
        for p in orientation.points:
            next_board[p.x][p.y] = NEW_MOVE

        plt.imshow(next_board, origin='lower')
        plt.show()



board = Board()
