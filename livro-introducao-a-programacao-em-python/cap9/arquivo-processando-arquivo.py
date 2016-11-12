# -*- coding: utf-8 -*-
largura = 79

entrada = open("_entrada.txt")

for linha in entrada.readlines():
	if linha[0] == ";":
		continue #ignora a linha
	elif linha[0] == ">":
		print(linha[1:].rjust(largura))
	elif linha[0] == "*":
		print(linha[1:].center(largura))
	elif linha[0] == "=":
		print(linha.replace(linha,"*" * largura))
	else:
		print(linha)

entrada.close()