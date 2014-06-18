# coding: utf-8
__author__ = 'Szymon Wanot and Paweł Siemienik'


class Neuron():
    def __init__(self, input_number, input_weights):
        self.input_number = input_number
        self.input_weights = input_weights

    def count_input(self):
        for i in range(self.input_number):
            self.input_count += i * self.input_weights[i]


class NeuralLayer():
    def __init__(self, neuron_number, input_per_neuron):
        self.neuron_number = neuron_number
        self.input_per_neuron = input_per_neuron


class NeuralNetwork():
    def __init__(self, layers):
        self.layers = layers