# -*- coding: utf-8 -*-
from clientes import Cliente

""" Uma conta para representar uma conta do banco com seus clientes e seu saldo """
class Conta(object):
	def __init__(self, clientes, numero, saldo = 0):
		super(Conta, self).__init__()
		self.clientes = clientes
		self.numero = numero
		self.saldo = saldo

	def resumo(self):
		print("CC Número: %s Saldo: %10.2f" % (self.numero, self.saldo))

	def saque(self, valor):
		self.saldo -= valor

	def deposito(self, valor):
		self.saldo += valor

