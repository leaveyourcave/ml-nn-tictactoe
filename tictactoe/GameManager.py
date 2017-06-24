from numpy import random


class GameManager:
    def __init__(self, game, player_o, player_x):
        self.game = game
        self.player_o = player_o
        self.player_x = player_x

        self.turn = 1
        if random.randint(0, 2) == 0:
            self.turn = -1

    def play(self):
        # Logging
        print "Starts: %d" % self.turn
        ###############

        while self.game.get_game_state() == "":
            next_move = self._ask_player_for_next_move()

            # Logging
            self.game.display_board()
            print "Player [%2d] makes move: %d" % (self.turn, next_move)
            ###############

            if self.game.is_move_possible(next_move):
                self.game.move(next_move, self.turn)
            else:
                return self.end_game("WRONG_MOVE")

            self.switch_turn()

        return self.end_game(self.game.get_game_state())

    def end_game(self, state):
        # Logging
        print "End with status: [%s]" % state
        ###############

        player_x_points = 0
        player_o_points = 0

        if state == "WRONG_MOVE":
            if self.turn == 1:
                player_x_points = -2
                player_o_points = 1
            else:
                player_x_points = 1
                player_o_points = -2

        if state == "X":
                player_x_points = 1
                player_o_points = -1

        if state == "O":
                player_x_points = -1
                player_o_points = 1

        return player_x_points, player_o_points

    def switch_turn(self):
        if self.turn == 1:
            self.turn = -1
        else:
            self.turn = 1

    def _ask_player_for_next_move(self):
        if self.turn == 1:
            return self.player_x.make_next_move(self.game.squares)
        else:
            return self.player_o.make_next_move(self.game.squares)


