# -*- coding: utf-8 -*-
impares = open("impares.txt", "w")
pares = open("pares.txt", "w")

for x in range(0,101):
	if x % 2 == 0:
		pares.write("%d\n" % x)
	else:
		impares.write("%d\n" % x)

impares.close()
pares.close()