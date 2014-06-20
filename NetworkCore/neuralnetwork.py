# coding: utf-8
__author__ = 'Szymon Wanot and Paweł Siemienik'
from math import exp
from random import random
import nnconf


class Neuron():
    """
    class representing neuron
    """
    def __init__(self, input_number):
        """
        :param input_number: number of inputs to neuron
        :return:
        """
        self.input_number = input_number
        self.input_count = 0
        self.input_weights = []
        self.random_weights()

    def random_weights(self):
        """
        randomization of weights in neuron
        :return:
        """
        self.input_weights = [random() for i in range(self.input_number)]

    def count_input(self, inputs=[]):
        """
        counting inputs to neuron
        :param inputs: input list to neuron
        :return: sum of i[x] * w[x]
        """
        for i in range(len(inputs)):
            self.input_count += inputs[i] * self.input_weights[i]
        return self.input_count


class NeuralLayer():
    """
    Simple implementation of neuron layer struct
    """
    def __init__(self, neuron_number, input_per_neuron):
        self.neuron_number = neuron_number
        self.input_per_neuron = input_per_neuron
        self.neurons = [Neuron(self.input_per_neuron) for i in range(self.neuron_number)]


class NeuralNetwork():
    def __init__(self, number_inputs, number_hidden_layers, number_outputs, neuron_per_hidden_layer, regression=False):
        self.number_inputs = number_inputs
        self.number_hidden_layers = number_hidden_layers
        self.number_outputs = number_outputs
        self.neuron_per_hidden_layer = neuron_per_hidden_layer
        self.hidden_layers = []
        self.bias = nnconf.CONFIG.get('bias', 0)
        self.inputs = []
        self.outputs = []
        self.regression = regression

    def create_network(self):
        self.outputs = [1.0 for i in range(self.number_outputs)]
        self.inputs = [1.0 for i in range(self.number_inputs)]
        for i in range(self.number_hidden_layers):
            self.hidden_layers.append(NeuralLayer(self.neuron_per_hidden_layer, self.number_inputs))
        # TO DEBUG
        print self.inputs
        for layer in self.hidden_layers:
            for neuron in layer.neurons:
                print neuron.input_weights
        print self.outputs

    def put_weights(self, weight_list):
        for layer in self.hidden_layers:
            for neuron in layer.neurons:
                neuron.input_weights = weight_list

    def update(self, input_list):
        self.outputs = []
        # validate inputs
        if len(input_list) != self.number_inputs:
            print "Incorrect inputs"
            return self.outputs

        for layer in range(self.number_hidden_layers):
            #move to next layer
            if layer > 0:
                input_list = self.outputs

            #clear output
            del self.outputs[:]
            for neuron in self.hidden_layers[layer].neurons:
                activation = neuron.count_input(input_list)
                activation += neuron.input_weights[self.number_inputs-1] * self.bias
                self.outputs.append(sigmoid(activation))
        return self.outputs

    def back_propagation(self, targets, learning_rate, momentum_factor):
        if len(targets) != self.number_outputs:
            raise ValueError, 'incorrect data'

        out_deltas = [0.0 for i in range(self.number_outputs)]

        for i in range(self.number_outputs):
            out_deltas[i] = targets[i] - self.outputs[i]
            if not self.regression:
                out_deltas[i] *= derivative_sigmoid(self.outputs[i])

        hidden_deltas = [0.0 for i in range(self.number_hidden_layers)]
        for i in range(self.number_hidden_layers):
            error_treshold = 0.0
            for j in range(self.number_outputs):
                error_treshold += out_deltas[j] * self.hidden_layers[i].neurons[i].input_weights[j]
            #hidden_deltas[i] = derivative_sigmoid(self.hidden_layers[i].)


    def train(self):
        pass

    def test(self):
        pass


def sigmoid(activation):
    """
    Simple sigmoid function implementation
    :param activation: activation treshold from neural network
    :return: sigmoid result from activation
    """
    return 1 / (1 + exp(-activation))


def derivative_sigmoid(activation):
    """
    Derivative form sigmoid function used to learn in back_propagation method
    :param activation:
    :return: result derivative sigmoid
    """
    return 1 - activation**2