class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 91

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    gabriel = Mutante(nome='Gabriel')
    hanibal = Homem(gabriel, nome='Hanibal')
    print(Pessoa.cumprimentar(hanibal))
    print(id(hanibal))
    print(hanibal.cumprimentar())
    print(hanibal.nome)
    print(hanibal.idade)
    for filho in hanibal.filhos:
        print(filho.nome)
    hanibal.sobrenome = 'Padilha'
    del hanibal.filhos
    hanibal.olhos = 1
    del hanibal.olhos
    print(hanibal.__dict__)
    print(gabriel.__dict__)
    print(Pessoa.olhos)
    print(hanibal.olhos)
    print(gabriel.olhos)
    print(id(Pessoa.olhos), id(hanibal.olhos), id(gabriel.olhos))
    print(Pessoa.metodo_estatico(), hanibal.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), hanibal.nome_e_atributos_de_classes())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(gabriel, Pessoa))
    print(isinstance(gabriel, Homem))
    print(gabriel.olhos)
    print(gabriel.cumprimentar())
    print(hanibal.cumprimentar())
