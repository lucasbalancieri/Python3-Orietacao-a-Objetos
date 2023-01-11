class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    # Método
    def dar_likes(self):
        self._likes += 1

    # Getters
    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    # Setters
    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def __str__(self):  # Representação textual do objeto
        return f'Nome: {self.nome}\nAno: {self.ano}\n{self.likes} likes\n'


class Filme(Programa):  # (Programas) <- deixa explicito que Filme tem a classe Programas como classe Mãe (Herança)
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # Chama o __init__ da classe mãe
        self.duracao = duracao

    def __str__(self):  # Representação textual do objeto
        return f'Nome: {self.nome}\n{self.duracao} minutos\nAno: {self.ano}\n{self.likes} likes\n'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):  # Representação textual do objeto
        return f'Nome: {self.nome}\n{self.temporadas} temporadas\nAno: {self.ano}\n{self.likes} likes\n'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):    # Torna a classe iteravel, se comporta como uma lista sem herdar list (Duck typing)
        return self._programas[item]

    def __len__(self):   # Faz com que a classe se comporte Sized
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas


vingadores = Filme('vingadores', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
#   print(f'Nome: {vingadores.nome}\nAno: {vingadores.ano}\nDuração: {vingadores.duracao} minutos\n{vingadores.likes} likes\n')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
# print(f'Nome: {atlanta.nome}\nAno: {atlanta.ano}\n{atlanta.temporadas} Temporadas\n{atlanta.likes} likes\n')

tmep = Filme('todo mundo em pânico', 1999, 120)
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()

demolidor = Serie('demolidor', 2016, 4)
demolidor.dar_likes()
demolidor.dar_likes()

listinha = [atlanta, vingadores, demolidor, tmep]

playlist_fds = Playlist('Fim de Semana', listinha)


for programa in playlist_fds:
    print(programa)  # Não importa de qual tipo seja o objeto, executa o __str__ dentro do objeto iterado (Polimorfismo em __str__).

print(f"Tamanho da playlist: {len(playlist_fds)}")