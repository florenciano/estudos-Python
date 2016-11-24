# -*- coding: utf-8 -*-
from bancos import Conta

#abrindo conta no banco Tatú
class Cliente(object):
	"""docstring for Cliente"""
	def __init__(self, nome, telefone):
		self.nome = nome
		self.telefone = telefone

#cadastrando os primeiros clientes
joao = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-1234")

#testando a funcionalidade da conta
Conta.resumo()
