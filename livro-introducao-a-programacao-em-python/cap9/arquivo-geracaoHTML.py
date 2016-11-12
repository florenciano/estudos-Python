# -*- coding: utf-8 -*-
# pagina = open("criar-pagina-html.html", "w")
pagina = open("criar-pagina-html-apartir-dicionario.html", "w")
filmes = {
	"drama" : ["Cidadão Kane", "O poderoso Chefão"],
	"comédia" : ["Tempos modernos", "Americam Pie", "Se beber não case"],
	"policial" : ["Chuva negra", "Desejo de matar", "Difícil de matar"],
	"guerra" : ["O resgate do soldado Ryan", "Platoon", "Rambo II"]
}

pagina.write("""
<html lang="pt-br">
<head>
	<meta charset="UTF-8">
	<title>Filmes</title>
</head>
<body>
""")
#gerando títulos
for genero, filme in filmes.items():
	pagina.write("<h1>%s</h1>" % ( genero[0].upper() + str(genero[1:].lower()) ))

	#gerando listas com os nomes dos filmes
	pagina.write("<ul>")

	for nome in filme:
		pagina.write("<li>%s</li>" % nome)

	pagina.write("</ul>")

pagina.write("""
</body>
</html>
""")
pagina.close()
