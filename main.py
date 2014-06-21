# coding: utf-8
__author__ = 'Szymon Wanot and Paweł Siemienik'
from NetworkCore.simplenn import SimpleNN as NeuralNetwork
import learningset


class NnApp():
    def __init__(self):
        self.network = NeuralNetwork(2, 2, 1)

    def run(self):
        self.network.learn(200, learningset.LEARNING_SET, 0.5, 0.01)
        print "I'm learned"
        self.network.test_learning(learningset.TEST_SET, True)

if __name__ == '__main__':
    app = NnApp()
    app.run()