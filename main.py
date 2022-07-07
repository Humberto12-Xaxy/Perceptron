from random import random
from Data import Data
from Perceptron import Perceptron


if __name__ == '__main__':
    data_training = Data('Training.data')
    X, Y = data_training.get_data()
    factor = round(random(), 4)
    
    w = [round(random(),4) for i in range(len(X[0]))]

    perceptron = Perceptron(X, Y, w, factor)

    aceptada = perceptron.training()
    print('Test Perceptron'.center(21, '-'))
    test_values = input('Ingrese las 4 entradas(separados por ,): ')
    data_string = test_values.split(',')
    data = []
    for value in data_string:
        data.append(float(value))
    data.insert(0, 1)
    perceptron.test(aceptada, data)