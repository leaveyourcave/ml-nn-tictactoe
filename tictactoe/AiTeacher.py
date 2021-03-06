import numpy as np

from tictactoe.AiPlayer import AiPlayer
from tictactoe.Game import Game
from tictactoe.GameManager import GameManager
from tictactoe.RandomPlayer import RandomPlayer
import random


class AiTeacher:
    def __init__(self):
        pass

    """
        TODO fitness should work differently - player should play as much matches as he can.
            Play until loose or wrong move.
            Every won match multiplies his fitness - makes him better.

    """

    def fitness(self, player_x):
        iteration = 0
        total_rating = 0
        stop = False
        player_o = RandomPlayer()  # FIXME Its important to have the same seed for each fitness evaluation... but why it makes, that population gets worse?

        while not stop:
            iteration = iteration + 1
            game_manager = GameManager(Game(), player_o, player_x)
            rating = game_manager.play()
            player_x_rating = rating[0]  # value {1, 0, -1, -2}

            if player_x_rating < 0:
                stop = True

            player_x_rating = 3 + (player_x_rating - 1)  # scale {1, 0, -1, -2} to {3, 2, 1, 0} (the greater the better)
            total_rating = total_rating + player_x_rating

        return total_rating  # TODO modify/scale rating and add/multiply it somehow

    def create_population(self, count):
        return [AiPlayer(x) for x in range(count)]

    def create_population_and_rate_it(self):
        POPULATION_MAX = 1000

        population = self.create_population(POPULATION_MAX)

        for i in range(1, 2000):
            population = self.reproduce(population)
            # TODO add mutations
            print "population: %d: %s" % (i, sorted(map(lambda t: self.fitness(t), population), reverse=True)[:10])

        final_population = map(lambda t: (self.fitness(t), t), population)
        top_from_population = sorted(final_population, key=lambda tup: tup[0], reverse=True)[:50]
        for top in top_from_population:
            print top

        return final_population

    def reproduce(self, population):
        NUMBER_OF_BEST_PARENTS = 10

        population_with_rating = map(lambda t: (self.fitness(t), t), population)
        best_parents_with_rating = sorted(population_with_rating, key=lambda tup: tup[0])[:NUMBER_OF_BEST_PARENTS]

        best_fathers = map(lambda p: p[1], best_parents_with_rating[0::2])
        best_mothers = map(lambda p: p[1], best_parents_with_rating[1::2])

        # TODO add different types of combining:
        # - combine theta 1 and theta 2 separately
        # - combine theta 1 and theta 2 together
        # - combine first part of mother and second part of father (axis should be random)
        # - combine first part of father and second part of mother (axis should be random)
        # - combine
        random.seed()
        next_generation_a = [self.combine_y_axis(random.choice(best_fathers), random.choice(best_mothers)) for i in
                             range(1, 495)]
        next_generation_b = [self.combine_x_axis(random.choice(best_fathers), random.choice(best_mothers)) for i in
                             range(1, 495)]

        return next_generation_a + next_generation_b + best_fathers + best_mothers

    @staticmethod
    def combine_y_axis(father, mother):
        father_theta_1 = father.theta1
        father_theta_2 = father.theta2

        mother_theta_1 = mother.theta1
        mother_theta_2 = mother.theta2

        child_theta_1 = np.concatenate((father_theta_1[:, 0:4], mother_theta_1[:, 4:9]), axis=1)
        child_theta_2 = np.concatenate((father_theta_2[:, 0:4], mother_theta_2[:, 4:9]), axis=1)

        return AiPlayer(None, child_theta_1, child_theta_2)

    @staticmethod
    def combine_x_axis(father, mother):
        father_theta_1 = father.theta1
        father_theta_2 = father.theta2

        mother_theta_1 = mother.theta1
        mother_theta_2 = mother.theta2

        child_theta_1 = np.concatenate((father_theta_1[0:4, :], mother_theta_1[4:9, :]), axis=0)
        child_theta_2 = np.concatenate((father_theta_2[0:4, :], mother_theta_2[4:9, :]), axis=0)

        return AiPlayer(None, child_theta_1, child_theta_2)
