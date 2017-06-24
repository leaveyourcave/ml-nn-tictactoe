import random


class RandomPlayer:
    def __init__(self):
        pass

    def make_next_move(self, squares):
        indices = [i for i, item in enumerate(squares) if item == 0]
        return random.choice(indices)
