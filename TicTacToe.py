# Tic Tac Toe
# 3x3-Matrix is divided by rows
# give current state of game

# noinspection PyRedundantParentheses

class Board():
    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def sign_to_print(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        else:
            return "O"

    def print_board(self):
        print(self.sign_to_print(self.state[0]) + " | " + self.sign_to_print(self.state[1]) + " | " + self.sign_to_print(self.state[2])
              + "\n" + self.sign_to_print(self.state[3]) + " | " + self.sign_to_print(self.state[4]) + " | " + self.sign_to_print(self.state[5])
              + "\n" + self.sign_to_print(self.state[6]) + " | " + self.sign_to_print(self.state[7]) + " | " + self.sign_to_print(self.state[8]))

    def is_valid_turn(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False

    def make_turn(self, cell, active_player):
        if self.is_valid_turn(cell):
            self.state[cell] = active_player.symbol
            return True
        else:
            return False

    def check_win(self, player):
        s = player.symbol
# Horizontal
        if  self.state[0] == s and self.state[1] == s and self.state[2] == s:
            return True
        elif self.state[3] == s and self.state[4] == s and self.state[5] == s:
            return True
        elif self.state[6] == s and self.state[7] == s and self.state[8] == s:
            return True
# Diagonal
        elif self.state[0] == s and self.state[4] == s and self.state[8] == s:
            return True
        elif self.state[2] == s and self.state[4] == s and self.state[6] == s:
            return True
# Vertical
        elif self.state[0] == s and self.state[3] == s and self.state[6] == s:
            return True
        elif self.state[1] == s and self.state[4] == s and self.state[7] == s:
            return True
        elif self.state[2] == s and self.state[5] == s and self.state[8] == s:
            return True

    def is_full(self):
        for i in self.state:
            if i == 0:
                return False
        return True


# noinspection PyRedundantParentheses
class Player:
    def __init__(self, symbol):
        self.symbol = symbol


if __name__ == '__main__':
    player_a = Player(1)
    player_b = Player(-1)
    board = Board()
    active_player = player_a

    while not board.is_full():
        board.print_board()
        try:
            cell = int(input('Where would you like to place your sign? [1-9]'))
        except ValueError:
            continue
        cell = cell - 1
        if cell < 0 or cell > 8:
            print('Please enter a valid cell value.')
            continue
        if board.make_turn(cell, active_player):
            if board.check_win(active_player):
                board.print_board()
                print('You win!')
                break
            if active_player == player_a:
                active_player = player_b
            else:
                active_player = player_a
        else:
            print('invalid move')
            continue
