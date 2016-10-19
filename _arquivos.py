# -*- coding: utf-8 -*-

arquivo = open("números.txt", "w")
for linha in range(1,50):
	arquivo.write("%d\n" % linha)
arquivo.close()