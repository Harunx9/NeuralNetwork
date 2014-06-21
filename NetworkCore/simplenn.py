__author__ = 'harun'
from neuralnetwork import sigmoid, derivative_sigmoid, random


class SimpleNN():
    """
    Mr. Spock pure logic mind
    """

    def __init__(self, number_inputs, number_hidden_layers, number_outputs):
        # network structure definitions
        self.n_inputs = number_inputs
        self.n_outputs = number_outputs
        self.n_hidden_layers = number_hidden_layers
        # network activation list
        self.a_inputs = [1.0 for i in range(self.n_inputs + 1)]
        self.a_outputs = [1.0 for i in range(self.n_outputs + 1)]
        self.a_hidden_layers = [1.0 for i in range(self.n_hidden_layers)]
        # initialize random weights
        self.weight_input = [[random() for i in range(self.n_hidden_layers + 1)] for j in range(self.n_inputs + 1)]
        self.weight_output = [[random() for i in range(self.n_outputs)] for j in range(self.n_hidden_layers + 1)]

        # back propagation changes in weights from momentum
        self.change_input = [[0.0 for i in range(self.n_hidden_layers + 1)] for j in range(self.n_inputs + 1)]
        self.change_output = [[0.0 for i in range(self.n_outputs)] for j in range(self.n_hidden_layers + 1)]

    def think(self, inputs=[]):
        if len(inputs) != self.n_inputs:
            raise ValueError('Incorrect input')

        for i in range(self.n_inputs):
            self.a_inputs[i] = inputs[i]

        for i in range(self.n_hidden_layers):
            total = 0.0
            for j in range(len(self.a_inputs)):
                total += self.a_inputs[j] * self.weight_input[j][i]
            self.a_hidden_layers[i] = sigmoid(total)

        for i in range(self.n_outputs):
            total = 0.0
            for j in range(len(self.a_hidden_layers)):
                total += self.a_hidden_layers[j] * self.weight_output[j][i]
            self.a_outputs[i] = sigmoid(total)
        return self.a_outputs

    def back_propagation(self, targets, learning_rate, momentum_factor):
        if len(targets) != self.n_outputs:
            raise ValueError('Incorrect targets')

        out_delta = [0.0 for i in range(self.n_outputs)]

        for i in range(self.n_outputs):
            out_delta[i] = targets[i] - self.a_outputs[i]
            out_delta[i] *= derivative_sigmoid(self.a_outputs[i])

        hidden_delta = [0.0 for i in range(self.n_hidden_layers)]

        for i in range(len(self.a_hidden_layers)):
            error = 0.0
            for j in range(self.n_outputs):
                error += out_delta[j] * self.weight_output[i][j]
            hidden_delta[i] = derivative_sigmoid(self.a_hidden_layers[i]) * error

        # update output weights
        for i in range(len(self.a_hidden_layers)):
            for j in range(self.n_outputs):
                change = out_delta[j] * self.a_hidden_layers[i]
                self.weight_output[i][j] = self.weight_output[i][j] + (learning_rate * change) \
                                           + (momentum_factor * self.change_output[i][j])
                self.change_output[i][j] = change

        # update input weights
        for i in range(len(self.n_inputs)):
            for j in range(len(self.n_hidden_layers)):
                change = hidden_delta[j] * self.a_inputs[i]
                self.weight_input[i][j] = self.weight_input[i][j] + (learning_rate * change) \
                                            +(momentum_factor * self.change_input[i][j])
                self.change_input[i][j] = change
        # claculate error
        error = 0.0
        for i in range(len(targets)):
            error += 0.5 * ((targets[i] - self.a_inputs[i])**2)
        return error

    def learn(self, iterations, learning_set, learning_rate, momentum_factor):
        for i in xrange(iterations):
            error = 0.0
            for set in learning_set:
                self.think(set[0])
                tmp_error = self.back_propagation(set[1], learning_rate, momentum_factor)
                error += tmp_error

                if i % (iterations / 10) == 0:
                    print 'error threshold '.join(error)

    def test_learning(self, test_set=[]):
        pass