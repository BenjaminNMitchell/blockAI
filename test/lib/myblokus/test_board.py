from block_ai.lib.myblokus.board import Board

import unittest
import hypothesis


class PlayerBoard(unittest.TestCase):

    def test_board(self):
        # Given
        b = Board()

        # Then
        self.assertEqual(len(b.players[0].valid_moves), 53)
