# coding: utf-8
__author__ = 'Szymon Wanot and Paweł Siemienik'
from math import exp
from random import random


class Neuron():
    def __init__(self, input_number):
        self.input_number = input_number
        self.input_weights = []

    def random_weights(self):
        self.input_number = [random() for i in range(self.input_number)]

    def count_input(self, inputs=[]):
        for i in range(self.input_number):
            self.input_count += inputs[i] * self.input_weights[i]


class NeuralLayer():
    def __init__(self, neuron_number, input_per_neuron):
        self.neuron_number = neuron_number
        self.input_per_neuron = input_per_neuron
        self.neurons = [Neuron(self.input_per_neuron) for i in range(self.neuron_number)]


class NeuralNetwork():
    def __init__(self, number_inputs, number_hidden_layers, number_outputs, neuron_per_hidden_layer):
        self.number_inputs = number_inputs
        self.number_hidden_layers = number_hidden_layers
        self.number_outputs = number_outputs
        self.neuron_per_hidden_layer = neuron_per_hidden_layer
        self.hidden_layers = []
        self.bias = 0

    def create_network(self):
        for i in range(self.hidden_layers):
            self.hidden_layers.append(NeuralLayer(self.neuron_per_hidden_layer, self.number_inputs))

    def put_weights(self, weight_list):
        for layer in self.hidden_layers:
            for neuron in layer.neurons:
                neuron.input_weights = weight_list

    def update(self, input_list):
        outputs = []
        # validate inputs
        if len(input_list) != self.number_inputs:
            print "Incorrect inputs"
            return outputs

        for layer in range(self.number_hidden_layers):
            #move to next layer
            if layer > 0:
                input_list = outputs

            #clear output
            del outputs[:]
            for neuron in self.hidden_layers[layer].neurons:
                activation = neuron.count_input(input_list)
                activation += neuron.input_weights[self.number_inputs-1] * self.bias
                outputs.append(activation)
        return outputs

    def sigmond(self, activation, response):
        return 1 / (1 + exp(-activation / response))
