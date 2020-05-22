"""Node for boardtree """

class BTNode:
    """ Node for realisation boartree """

    def __init__(self, board=None):
        """ Creates node for realisation """
        self.board = board
        self.right = None
        self.left = None
