class Pessoa:
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
    for filho in hanibal.filhos:
        print(f'Filhos de {hanibal.nome}: ', end='')
        print(filho.nome)
    hanibal.sobrenome = 'Padilha'
    print(hanibal.__dict__)
    del hanibal.filhos
    print(hanibal.__dict__)
    print(gabriel.__dict__)
