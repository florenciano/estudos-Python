# -*- coding: utf-8 -*-
arquivo = open("numeros.txt", "w")

for linha in range(0,100):
	arquivo.write("%d\n" % linha)

arquivo.close()