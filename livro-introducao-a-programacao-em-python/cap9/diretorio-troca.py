# -*- coding: utf-8 -*-
import os

os.chdir("dir-a")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("dir-b")
print(os.getcwd())
os.chdir("../dir-c")
print(os.getcwd())

#voltando ao diretório raiz
os.chdir("../")
print(os.getcwd())

#criando diretórios intermediários
os.makedirs("avo/pai/filho")

#alterando nomes diretórios
os.rename("avo", "lorem")

"""
OBS: como este script já rodou, o diretório criado já exite
e o python acusará erro se tentar executar denovo...
O correto seria apagar o diretório 'lorem' e todo o seu conteúdo
para testar este script outra vez.
"""