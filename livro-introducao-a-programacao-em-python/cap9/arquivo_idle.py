Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> # -*- coding: utf-8 -*-
arquivo = open("numeros.txt", "w")

for linha in range(0,100):
	arquivo.write("%d\n" % linha)

arquivo.close()
SyntaxError: multiple statements found while compiling a single statement
>>> 
