class Perceptron():
    def __init__(self, x:list, y:list, w:list, factor:float) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.factor = factor

    def training(self):
        contador = 0
        while contador < len(self.x):
            sumatoria = self.get_sumatoria(self.x[contador], self.w)
            y_calculada = self.get_y_calculada(sumatoria)
            error = self.y[contador] - y_calculada
            if error == 0:
                contador += 1
            else:
                contador = self.change_w(error, contador)
        return self.w

    def change_w(self, error, contador):
        values = []
        for val in self.x[contador]:
            values.append(self.factor * error * val)
        temp = []
        for i in range(len(values)):
            temp.append(self.w[i] + values[i])
        self.w.clear()
        self.w = temp.copy()
        temp.clear()
        contador = 0
        return contador


    def get_sumatoria(self, list_x, w):
        sumatoria = 0
        for i in range(len(list_x)):
            sumatoria += list_x[i]*w[i]
            print(sumatoria)

        return sumatoria
    
    def get_y_calculada(self, sumatoria):
        y_calculada= 0
        if sumatoria >= 0:
            y_calculada = 1
        else:
            y_calculada = -1

        return y_calculada

    def test(self, w_aceptada:list, x_test:list):
        y = 0
        y = self.get_sumatoria(x_test, w_aceptada)
        if y >= 0:
            print('Iris-Setosa')
        else:
            print('Iris-versicolor')