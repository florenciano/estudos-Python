# -*- coding: utf-8 -*-
import os

#Cria um arquivo e o fecha imediatamente
open("moribundo.txt", "w").close()

#Cria o diretório e o apaga
os.mkdir("vago")
os.rmdir("vago")

#Apaga o arquivo
os.remove("moribundo.txt")