""" Module for implementation Board class"""


class Board:
    """ Class of boards """

    def __init__(self, board_desk=None, positions=None):
        """ Creates board """
        if board_desk:
            self.board = board_desk
        else:
            self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        if positions:
            self.positions = positions
        else:
            self.positions = {
                '7': (0, 0), '8': (0, 1), '9': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '1': (2, 0), '2': (2, 1), '3': (2, 2)}

    def check_status(self):
        """ Checks current status on the board
        Return True if the game can continue """
        if self.board[0][0]==self.board[0][1]==self.board[0][2] and self.board[0][0]!="":
            return False
        if self.board[1][0]==self.board[1][1]==self.board[1][2] and self.board[1][0]!="":
            return False
        if self.board[2][0]==self.board[2][1]==self.board[2][2] and self.board[2][0]!="":
            return False
        if self.board[0][0]==self.board[1][0]==self.board[2][0] and self.board[0][0]!="":
            return False
        if self.board[0][1]==self.board[1][1]==self.board[2][1] and self.board[0][1]!="":
            return False
        if self.board[0][2]==self.board[1][2]==self.board[2][2] and self.board[0][2]!="":
            return False
        if self.board[0][0]==self.board[1][1]==self.board[2][2] and self.board[0][2]!="":
            return False
        if self.board[0][2]==self.board[1][1]==self.board[2][0] and self.board[0][2]!="":
            return False
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    return True


    def free_cells(self):
        """ Returns that, that is free"""
        list_of_free = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    list_of_free.append(str(3 * (2 - i) + 1 + j))

        return list_of_free

    def game(self, number, sem):
        """
        Write symbol at current position
        """
        if number in self.positions:
            row, col = self.positions[str(number)][0], \
                       self.positions[str(number)][1]

            if self.board[row][col] == '':
                self.board[row][col] = sem

    def __str__(self):
        """ Represent as string """
        result = ''
        for i in self.board:
            for k in i:
                if k == '':
                    result += '-'
                elif k == '0':
                    result += '0'
                elif k == 'X':
                    result += "X"
            result += '\n'
        return result[:-1]


if __name__ == "__main__":
    BOARD = Board([["", "", ""], ["", "", ""], ["", "", ""]])
    if BOARD.check_status():
        print(BOARD)
