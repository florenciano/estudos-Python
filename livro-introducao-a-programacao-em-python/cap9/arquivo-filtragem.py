# -*- coding: utf-8 -*-
multiplos4 = open("multiplos-de-4.txt", "w")
pares = open("pares.txt", "r")

for l in pares.readlines():
	if int(l) % 4 == 0:
		multiplos4.write(l)

pares.close()
multiplos4.close()
