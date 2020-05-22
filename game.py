"""Module of running game"""
from cross.board import Board
from cross.btree import BTree


class Game:
    """ Class of game running """

    def __init__(self):
        """ Creates game """
        self.board = Board()
        self.player = 'X'
        self.other = '0'

    def draw(self):
        """ Ask about where should it write """
        number = input('Where: \n')
        print(self.board.free_cells())
        while number not in self.board.free_cells():
            print('Possible cells:')
            print('7 8 9\n4 5 6\n1 2 3')
            number = input('Enter again: ')
        self.board.game(number, self.player)

    def computer_draw(self):
        """ Computer draw"""
        tree = BTree(self.board)
        self.board.game(tree.run(self.player, self.other)[1], self.other)


if __name__ == '__main__':
    print("Нічия не передбачена")
    GAME = Game()

    while GAME.board.check_status():
        print('------')
        print(GAME.board)
        GAME.draw()
        if not GAME.board.check_status():
            break
        GAME.computer_draw()

    print('\n-----')
    print(GAME.board)
    print("Game over")
