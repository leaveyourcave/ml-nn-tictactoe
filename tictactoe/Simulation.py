from tictactoe.AiPlayer import AiPlayer
from tictactoe.AiTeacher import AiTeacher
from tictactoe.GameManager import GameManager
from tictactoe.RandomPlayer import RandomPlayer
from tictactoe.Game import Game

# player_o = RandomPlayer()
# player_x = AiPlayer()
# game = Game()
#
# game_manager = GameManager(game, player_o, player_x)
#
# print(game_manager.play())
# game.display_board()

teacher = AiTeacher()
teacher.create_population_and_rate_it()
