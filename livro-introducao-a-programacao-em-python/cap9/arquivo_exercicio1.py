# -*- coding: utf-8 -*-

# abrindo os arquivos pares.txt e impares.txt
pares = open("pares.txt", "r")
impares = open("impares.txt", "r")

lista = []

# lendo os arquivos pares.txt e impares.txt
for x in pares.readlines():
	lista.append(int(x))

pares.close()

for x in impares.readlines():
	lista.append(int(x))

impares.close()

# imprimindo o conteúdo deles
print(lista.sort(reverse=True))
