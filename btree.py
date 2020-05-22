""" Implemtation tree for game """
import random
from copy import deepcopy

from cross.btnode import BTNode


class BTree:
    """ Class of trees for board """

    def __init__(self, board=None):
        """ Creates tree """
        self.node = BTNode(board)

    def run(self, user, other):
        """ Gaming """

        def recursion(node, rec):
            """ Makes drawing """
            if node is None:
                return -100000, None
            last = not node.board.check_status()
            if last == user:
                return 1, None
            if last == other:
                return -1, None

            player = other
            if rec % 2 == 0:
                player = user

            game = node.board.free_cells()
            right = ()
            left = ()

            if len(game) > 0:
                left = random.choice(game)
                game.remove(left)
                board = deepcopy(node.board)
                board.game(left, player)
                node.left = BTNode(board)

            if len(game) > 0:
                right = random.choice(game)
                game.remove(right)
                board = deepcopy(node.board)
                board.game(right, player)
                node.right = BTNode(board)

            l_pos = recursion(node.left, rec + 1)[0]
            r_pos = recursion(node.right, rec + 1)[0]

            if r_pos > l_pos:
                return r_pos + l_pos, right
            return r_pos + l_pos, left

        return recursion(self.node, rec=0)
