
from block_ai.lib.myblokus.valid_moves import ValidMoves
from block_ai.lib.myblokus.move import Move
from block_ai.lib.myblokus.orientation import Orientation
from block_ai.lib.myblokus.corner import Corner
from block_ai.lib.myblokus import point

import unittest


class ValidMovesTests(unittest.TestCase):

    def test_entry(self):
        # Given
        vm = ValidMoves()
        move = self.get_move()

        # When
        vm.add(move)
        moves = list(vm.get_all())

        # Then
        self.assertEqual(len(moves), 1)
        self.assertEqual(move, moves[0])
        

    def get_move(self):
        o = Orientation(((0, 0),))
        c = Corner((-1, -1), (0, 0))
        piece_id = 'p1'
        player_id = 0
        return Move(o, piece_id, player_id, c)


    def test_remove(self):
        # Given
        vm = ValidMoves()
        move = self.get_move()
        vm.add(move)

        # When
        vm.remove(move)
        moves = list(vm.get_all())

        # Then
        self.assertEqual(len(moves), 0)


    def test_len(self):
        # Given
        vm = ValidMoves()
        move = self.get_move()

        # When
        vm.add(move)

        # Then
        self.assertEqual(len(vm), 1)
