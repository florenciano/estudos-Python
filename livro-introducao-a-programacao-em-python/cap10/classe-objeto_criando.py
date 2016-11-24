# -*- coding: utf-8 -*-
class Televisao():
	"""docstring for Televisao"""
	def __init__(self, cinit, cmin, cmax):
		self.ligada = False
		self.canal = cinit
		self.cmin = cmin
		self.cmax = cmax
	def muda_canal_para_cima(self):
		if (self.canal + 1 <= self.cmax):
			self.canal += 1
		else: # ao chegar no último canal volta ao início
			self.canal = self.cmin
	def muda_canal_para_baixo(self):
		if (self.canal - 1 >= self.cmin):
			self.canal -= 1
		else: # ao chegar no primeiro canal volta ao final
			self.canal = self.cmax

# criando obj definindo parâmetros (cinit), (cmin) e (cmax)
tv = Televisao(12,1,32)

# testando os canais de nosso obj
for x in range(0,36):
	tv.muda_canal_para_cima()
	print(tv.canal)
