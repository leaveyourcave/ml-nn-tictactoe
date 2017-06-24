import numpy as np


# X      - array with board                 of size [nn_input_dim x 1] [9x1]
# theta1 - array to combine with a1==X      of size [nn_hidden_dim x nn_input_dim] [9x9]
# theta2 - array to combine with a2         of size [nn_output_dim x nn_hidden_dim] [9x9]
# Y      - array with best move prediction  of size [1 x nn_output_dim] [1x9]
#
class AiPlayer:
    def __init__(self, theta1=None, theta2=None):
        np.random.seed(10)
        self.bias1 = np.zeros((9, 1))

        if theta1 is None:
            self.theta1 = np.random.randn(9, 9)
        else:
            self.theta1 = theta1

        if theta2 is None:
            self.theta2 = np.random.randn(9, 9)
        else:
            self.theta2 = theta2

    def make_next_move(self, x):
        # forward propagation
        a1 = np.asarray(x)

        z2 = a1.dot(self.theta1)
        a2 = AiPlayer.sigmoid(z2)

        z3 = a2.dot(self.theta2)
        a3 = AiPlayer.sigmoid(z3)

        y = a3

        return y.tolist().index(max(y))

    def teach_me(self):
        pass

    @staticmethod
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))
