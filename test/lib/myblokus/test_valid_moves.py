
from block_ai.lib.myblokus.valid_moves import ValidMoves
from block_ai.lib.myblokus.move import Move
from block_ai.lib.myblokus.orientation import Orientation
from block_ai.lib.myblokus.corner import Corner
from block_ai.lib.myblokus import point
from . import test_lib as tl

import unittest


class ValidMovesTests(unittest.TestCase):

    def test_entry(self):
        # Given
        vm = ValidMoves()
        move = tl.get_move()

        # When
        vm.push({move})
        moves = list(vm.get_all())

        # Then
        self.assertEqual(len(moves), 1)
        self.assertEqual([move], moves)


    def test_remove(self):
        # Given
        vm = ValidMoves()
        move = tl.get_move()
        vm.push(new_moves={move})

        # When
        vm.remove(move)
        moves = list(vm.get_all())

        # Then
        self.assertEqual(len(moves), 0)


    def test_len(self):
        # Given
        vm = ValidMoves()
        moves = {tl.get_move(), tl.get_move((1,1,1))}

        # When
        vm.push(moves)

        # Then
        self.assertEqual(len(vm), 2)
