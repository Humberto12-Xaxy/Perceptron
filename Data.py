class Data():
    def __init__(self, file:str) -> None:
        self.file = file
        self.X = []
        self.Y = []

    def read_data(self):
        list_temp = []
        file = open(self.file)
        list_values = []
        for line in file:
            list_temp = line.rsplit()
            list_values.append(list_temp[0].split(','))
        return list_values

    def get_data(self):
        list_values = self.read_data()

        list_tempY = []
        for list in list_values:
            list_tempX = []
            for val in list:
                if val != 'Iris-setosa' and val != 'Iris-versicolor':
                    list_tempX.append(float(val))
                else:
                    if val == 'Iris-setosa':
                        list_tempY.append(1)
                    else:
                        list_tempY.append(-1)
            list_tempX.insert(0, 1)

            self.X.append(list_tempX)
            self.Y = list_tempY
        
        return self.X, self.Y


    

