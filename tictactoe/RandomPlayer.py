import random


class RandomPlayer:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
        pass

    def make_next_move(self, squares):
        indices = [i for i, item in enumerate(squares) if item == 0]
        return random.choice(indices)
