class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


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

