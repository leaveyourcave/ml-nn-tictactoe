
class Game:
    def __init__(self):
        self.squares = [0, 0, 0,
                        0, 0, 0,
                        0, 0, 0]

    def is_move_possible(self, index):
        return self.squares[index] == 0

    def move(self, index, val):
        self.squares[index] = val

    def get_game_state(self):
        s = self.squares
        if self._check(s[0], s[1], s[2], 1) or self._check(s[3], s[4], s[5], 1) \
                or self._check(s[6], s[7], s[8], 1) or self._check(s[0], s[3], s[6], 1) \
                or self._check(s[1], s[4], s[7], 1) or self._check(s[2], s[5], s[8], 1) \
                or self._check(s[0], s[4], s[8], 1) or self._check(s[2], s[4], s[6], 1):
            return "X"
        elif self._check(s[0], s[1], s[2], -1) or self._check(s[3], s[4], s[5], -1) \
                or self._check(s[6], s[7], s[8], -1) or self._check(s[0], s[3], s[6], -1) \
                or self._check(s[1], s[4], s[7], -1) or self._check(s[2], s[5], s[8], -1) \
                or self._check(s[0], s[4], s[8], -1) or self._check(s[2], s[4], s[6], -1):
            return "O"
        elif sum(map(abs, self.squares)) == 9:
            return "DRAW"
        else:
            return ""

    def display_board(self):
        for i in range(0, len(self.squares), 3):
            for n in self.squares[i:i + 3]:
                print "%2d" % n,
            print ""
        print ""

    @staticmethod
    def _check(a, b, c, val):
        return abs(a + b + c) == 3 and a == val
