from block_ai.lib.myblokus.board import Board

import unittest
import hypothesis


class PlayerBoard(unittest.TestCase):

    def test_board(self):
        # Given
        b = Board()
