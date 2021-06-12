class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 91

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    gabriel = Pessoa(nome='Gabriel')
    hanibal = Pessoa(gabriel, nome='Hanibal')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(hanibal.olhos)
    print(gabriel.olhos)
    print(id(Pessoa.olhos), id(hanibal.olhos), id(gabriel.olhos))
    print(Pessoa.metodo_estatico(), hanibal.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), hanibal.nome_e_atributos_de_classes())
