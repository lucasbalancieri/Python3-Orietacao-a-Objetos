# Desafio

class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def formatada(self):
        print("{:02d}/{:02d}/{}".format(self.__dia, self.__mes, self.__ano))