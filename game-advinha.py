def escolher():
	n = int(input("Escolha um número entre 1 e 10: "))
	#limpa a tela
	for x in range(0,80):
		print("")
	return n

meu_numero = escolher()

def advinhar():
	tentativas = 3
	while tentativas > 0:
		palpite = int(input("Qual o seu palpite? "))
		if palpite == meu_numero:
			print("Você acertou! Parabéns!")
			break
		elif tentativas >= 2:
			print("Você errou! Você tem mais", (tentativas - 1), "tentativas.")
		else:
			print("Você errou todas as tentativas! Perdeu.")
		tentativas -= 1