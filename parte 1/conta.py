class Conta:
    # self = endereço de memória onde o objeto foi criado
    # a função def__init__() é o metodo inicializador da classe, busca o objeto na memoria para iniciar a manipulação.
    def __init__(self, numero, titular, saldo, limite):
        print("constriuindo objeto self = {}".format(self))
        ###
        # Por convenção, o __ define que os atributos só devem ser acessados através dos métodos (encapsulamento)ca
        # Ainda é possivel acessar os atributos de maneira direta mas não é uma boa prática.
        ###
        # Atributos da classe Conta
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo de {} é de R$: {}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __validar_saque(self, valor):  # *O __ define que o metodo validar_saque só pode ser usado dentro da classe
        disponivel_para_saque = self.__limite + self.saldo
        return valor <= disponivel_para_saque

    def sacar(self, valor):
        if self.__validar_saque(valor):  # * Aqui
            self.__saldo -= valor
        else:
            print('O valor de R$ {} está indisponível para saque'.format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    # Getters
    ###
    # def get_saldo(self):  # Dessa forma para "pegar" o saldo é preciso conta.get_saldo()
    #   return self.__saldo
    #
    # def get_titular(self):
    #    return self.__titular
    #
    # def get_limite(self):
    #    return self.__limite
    ###
    @property   # Dessa forma é possivel "pegar" o valor de saldo através de conta.saldo
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    # Setters
    ###
    # def set_limite(self, limite):  # Dessa forma para alterar o limite é preciso conta.set_limite(1000.00)
    #    self.__limite = limite
    ###
    @limite.setter  # Dessa forma é possivel alterar o valor de limite através de conta.limite = 1000.00
    def limite(self, limite):
        self.__limite = limite

    ###
    # Portanto, com o @property para getters e @x.setter para setters, é possivel acessar os atributos sem parecer que
    # estão sendo acessados pelos métodos
    ###

    # Metodos Estáticos
    # São metódos da Classe que podem ser acessados sem a criação do objeto
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}