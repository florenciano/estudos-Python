# -*- coding: utf-8 -*-

#abrindo conta no banco Tatú
class Cliente(object):
	def __init__(self, nome, telefone):
		self.nome = nome
		self.telefone = telefone

#movimentando a conta
""" Uma conta para representar uma conta do banco com seus clientes e seu saldo """
class Conta(object):
	def __init__(self, clientes, numero, saldo = 0):
		super(Conta, self).__init__()
		self.clientes = clientes
		self.numero = numero
		self.saldo = saldo
		self.operacoes =[]
		self.deposito(saldo)

	def resumo(self):
		print("CC Número: %s Saldo: %10.2f" % (self.numero, self.saldo))

	def saque(self, valor):
		if self.saldo >= valor:
			self.saldo -= valor
			self.operacoes.append(["SAQUE", valor])

	def deposito(self, valor):
		self.saldo += valor
		self.operacoes.append(["DEPOSITO", valor])

	def extrato(self):
		print("Extrato CC Nº %s\n" % self.numero)
		for x in self.operacoes:
			print("%10s %10.2f" % (x[0], x[1]))
		print("\n    Saldo: %10.2f\n" % self.saldo)

#cadastrando os primeiros clientes
joao = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-1234")

#criando a conta do joao (nome, nº conta, valor inicial)
conta_corrente_joao = Conta(joao, 8759, 0)

#movimentando a conta do joao
conta_corrente_joao.resumo()
conta_corrente_joao.deposito(1000)
conta_corrente_joao.resumo()
conta_corrente_joao.saque(50)
conta_corrente_joao.resumo()
conta_corrente_joao.deposito(190)
conta_corrente_joao.resumo()
conta_corrente_joao.saque(360)
conta_corrente_joao.resumo()
conta_corrente_joao.saque(97.15)
conta_corrente_joao.resumo()
conta_corrente_joao.saque(250)
conta_corrente_joao.resumo()
conta_corrente_joao.extrato()

#classe para armazenar todas as contas do banco Tatu
class Banco(object):
	def __init__(self, nome):
		self.nome = nome
		self.clientes = []
		self.contas = []

	def abre_contas(self, conta):
		self.contas.append(conta)

	def lista_contas(self):
		for c in self.contas:
			print(c)

tatu = Banco("Tatú")
tatu.abre_contas([conta_corrente_joao])
tatu.lista_contas()

