# -*- coding: utf-8 -*-
import time

agora = time.time()
print(agora)
print(time.ctime(agora))

#converte o obj time para o nosso formato
now = time.localtime()
print("Ano: %d" % now.tm_year)
print("Mês: %d" % now.tm_mon)
print("Dia: %d" % now.tm_mday)
print("Hora: %d" % now.tm_hour)
print("Minuto: %d" % now.tm_min)
print("Dia da Semana: %d" % now.tm_wday)
print("Dia do ano: %d" % now.tm_yday)
print("Horário de verão: %d" % now.tm_isdst)
