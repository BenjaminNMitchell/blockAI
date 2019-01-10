
from block_ai.lib.myblokus.valid_moves import ValidMoves
from block_ai.lib.myblokus.move import Move
from block_ai.lib.myblokus.orientation import Orientation
from block_ai.lib.myblokus.corner import Corner
from block_ai.lib.myblokus import point
from . import test_lib as tl

import unittest


class ValidMovesTests(unittest.TestCase):

    def test_push(self):
        # Given
        vm = ValidMoves()
        move = tl.get_move()

        # When
        vm.push(new_moves={move})
        moves = list(vm.get_all())

        # Then
        self.assertEqual([move], moves)


    def test_remove(self):
        # Given
        vm = ValidMoves()
        move = tl.get_move()
        vm.push(new_moves={move})

        # When
        vm.push(invalid_moves={move})
        moves = list(vm.get_all())

        # Then
        self.assertEqual(len(moves), 0)


    def test_len(self):
        # Given
        vm = ValidMoves()
        moves = {tl.get_move(), tl.get_move((1,1,1))}

        # When
        vm.push(new_moves=moves)

        # Then
        self.assertEqual(len(vm), 2)

    def test_pop(self):
        # Given
        vm = ValidMoves()
        move = tl.get_move()

        # When
        vm.push(new_moves={move})
        moves1 = list(vm.get_all())
        vm.pop()
        moves2 = list(vm.get_all())

        # Then

        self.assertEqual([move], moves1)
        self.assertEqual([], moves2)

    def test_eq(self):
        
        # Given
        vm1 = ValidMoves()
        vm2 = ValidMoves()
        
        self.assertEqual(vm1, vm2)
    
        move = tl.get_move()
        vm1.push(new_moves={move})
        
        self.assertNotEqual(vm1, vm2)

        vm1.pop()
      
        self.assertEqual(vm1, vm2)
