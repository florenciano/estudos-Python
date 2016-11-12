#! /usr/bin/env python
def valida_inteiro(mensagem, minimo, maximo):
	while True:
		v = int(input(mensagem))
		if v >= minimo or v <= maximo:
			return v
		else:
			print("Digite um valor entre %d e %d" % (minimo, maximo))
	print("Você deve digitar um valor um numero inteiro")

