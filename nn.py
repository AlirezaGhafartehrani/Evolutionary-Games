import numpy as np


class NeuralNetwork():

    def __init__(self, layer_sizes):
        # TODO
        # layer_sizes example: [10, 20, 1]
        self.W1 = np.random.normal(size=(layer_sizes[1], layer_sizes[0]))
        self.b1 = np.zeros((layer_sizes[1], 1))
        self.W2 = np.random.normal(size=(layer_sizes[2], layer_sizes[1]))
        self.b2 = np.zeros((layer_sizes[2], 1))

    def activation(self, x):
        # TODO
        return 1 / (1 + np.exp(-x))

    def forward(self, x):
        # TODO
        # x example: np.array([[0.1], [0.2], [0.3]])
        A0 = x                                        # 1st layer of perceptron
        A1 = self.activation(self.W1 @ A0 + self.b1)  # 2nd layer of perceptron
        A2 = self.activation(self.W2 @ A1 + self.b2)  # 3rd layer of perceptron
        return A2

        # print("W1")
        # print(type(self.W1))
        # print(self.W1.shape)
        #
        # print("W2")
        # print(type(self.W2))
        # print(self.W2.shape)
        #
        # print("b1")
        # print(type(self.b1))
        # print(self.b1.shape)
        #
        # print("b2")
        # print(type(self.b2))
        # print(self.b2.shape)
        #
        # print("A0")
        # print(type(A0))
        # print(A0.shape)
        # print(A0)
        #
        # print("A1")
        # print(type(A1))
        # print(A1.shape)
        # print(A1)
        #
        # print("A2")
        # print(type(A2))
        # print(A2.shape)
        # print(A2)



