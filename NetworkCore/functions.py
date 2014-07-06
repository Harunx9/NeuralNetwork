from math import tanh

def sigmoid(activation):
    """
    Simple sigmoid function implementation
    :param activation: activation treshold from neural network
    :return: sigmoid result from activation
    """
    return tanh(activation)


def derivative_sigmoid(activation):
    """
    Derivative form sigmoid function used to learn in back_propagation method
    :param activation:
    :return: result derivative sigmoid
    """
    return 1 - (tanh(activation)**2)
    #return sigmoid(activation)*(1 - sigmoid(activation))