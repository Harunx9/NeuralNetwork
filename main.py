# coding: utf-8
__author__ = 'Szymon Wanot and Paweł Siemienik'
from NetworkCore.neuralnetwork import NeuralNetwork


class NnApp():
    def __init__(self):
        self.network = NeuralNetwork(4, 2, 2, 4)
        self.network.create_network()

    def run(self):
        for i in range(100):
            net_out = self.network.update([1, 0, 0, 1])
            print net_out

if __name__ == '__main__':
    app = NnApp()
    app.run()