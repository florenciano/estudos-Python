# -*- coding: utf-8 -*-

"""
Existem vários tipos simples de dados pré-definidos no Python, tais como:
	Números (inteiros, reais, complexos, ... )
	Texto

Além disso, existem tipos que funcionam como coleções. Os principais são:
	Lista
	Tupla
	Dicionário

Os tipos no Python podem ser:
	Mutáveis: permitem que os conteúdos das variáveis sejam alterados.
	Imutáveis: não permitem que os conteúdos das variáveis sejam alterados.\

"""

##### NÚMEROS ######

#convertendo de real para inteiro
print "int(3.14) ", int(3.14)

#convertendo de inteiro para número flutuante
print "float(5) ", float(5)

#cálculo de inteiro para número flutuante
print "5.0 / 2 + 3 = ", 5.0 / 2 + 3

#inteiros em outra base
print "int('20', 8) ", int('20', 8) #base 8

#operacões com números complexos
c = 3 + 4j
print 'c = ', c
print "Parte real: ", c.real
print "Parte imaginária: ", c.imag
print "Conjugado: ", c.conjugate()

##### Texto ######

animal = "Hippo"

#Concatenação
print("The animal of the zoo is %s", %animal)