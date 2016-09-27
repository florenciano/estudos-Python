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

animal = "giraffe"

#concatenação
print "O animal do zoo é: " + animal

#interpolacão
print "O %s '%s' (ao contrário) tem um tamanho de %d caracteres." % (animal, animal[::-1].lower(), len(animal))

#strings tratadas como sequência
for ch in animal:
	print ch.upper()

#strings são objetos
if animal.startswith("g"):
	print animal

#o que acontecerá?
print '|' * 20

#zeros a esquerda
print "Hora %02d:%02d" % (9,05)

#hexadecimal
print "#%x" %255

#exponenciação
print "%.2e" %1.257458458

musicos = [
	("Rodrigo", "guitarrista","Relient K"),
	("Rodolfo", "pianista","BB King"),
	("Rodnei", "trompezista","Só pra contrariar")
]
#parâmetros identificados pela ordem
msg = "{0} é {1} do {2}"

for nome, funcao, banda in musicos:
	print(msg.format(nome, funcao, banda))

msg2 = "{nome}, você é o cara que comeu: {food} e fez cara de {gesto}."
print msg2.format(nome="Fernanda", food="açai", gesto="nossa que bosta")

import string
a = string.ascii_letters
b = a[1:]
for x in a:
	if x == "R":
		print x

##### Lista ######

#uma nova Lista
curso = ["Mat", "Bio", "Geo", "Art", "Por", "Rel"]
for x in curso:
	print x

#trocando o último elemento
curso[-1] = "His"
print curso

#incluindo
curso.append("Fis")
print curso

#removendo
curso.remove("Geo")
print curso, len(curso)

#ordena a Lista
curso.sort()
print curso

#inverte a Lista
curso.reverse()
print curso

#imprime numerado
for i, cur in enumerate(curso):
	print i + 1, "=>", cur


#filas e pilhas
lista = ["J", "K", "L", "M"]
print "Lista: ", lista

while lista: #uma lista vazia é considerada como falsa
	print "Saiu", lista.pop(0), "faltam", len(lista)

print "-----"

lista += ["O", "P", "Q", "R"]
while lista:
	print "Saiu", lista.pop(), "faltam", len(lista)


#### Outros tipos de sequencia ###

#conjunto de dados
s1 = set(range(3)) #type 'set'
s2 = set(range(10,7,-1))
s3 = set(range(2,10,2))

#exibe os dados
print 's1: ', s1, '\ns2: ', s2, '\ns3: ', s3

#uniao
s1_s2 = s1.union(s2)
print "União entre s1 e s2: ", s1_s2

#diferença
print "Diferença com s3: ", s1_s2.difference(s3) #saiu o '2' comum entre eles

#interseção
print "interseção com s3: ", s1_s2.intersection(s3)

if s1.issuperset([1,2]):
	print 's1 inclui 1 e 2'

if s1.isdisjoint(s2):
	print 's1 e s2 não tem elementos em comum'


##### Dicionários ######

bolos = {
	"Cenoura" 	:	["Seg", "Ter"],
	"Milho" 	:	["Qua", "Qui", "Sab"],
	"Chocolate"	:	["Seg", "Qui", "Sex", "Sab"],
	"Laranja"	:	["Ter", "Qua", "Sex"],
	"Mandioca"	:	["Qui", "Sex", "Sab"]
}

#mais bolos
bolos["Fuba"] = ["Ter", "Qui", "Sab"]
print bolos

print("")

#items() retorma uma lista de tuplas com a chave e o valor
for bolo, dia in bolos.items():
	print bolo, "=>", dia
