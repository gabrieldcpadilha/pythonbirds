from unittest import TestCase

from oo.carro import Motor, Direcao


class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

    def teste_frear(self):
        motor = Motor()
        motor.frear()
        self.assertEqual(0, motor.velocidade)

    def teste_girar_a_direita(self):
        direcao = Direcao()
        direcao.girar_a_direita()
        self.assertEqual('Leste', direcao.valor)

    def teste_girar_a_esquerda(self):
        direcao = Direcao()
        direcao.girar_a_esquerda()
        direcao.girar_a_esquerda()
        self.assertEqual('Sul', direcao.valor)
