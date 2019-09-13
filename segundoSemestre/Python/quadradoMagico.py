'''
Nome: Marcelo Nao Takayama
TIA: 31942407

'''
############################################################
tamanho = 3

def quadradoMagico(matriz):
	somaDiagonal1 = 0 

	# Diagonal Primária
	for x in range  (0, tamanho):
		somaDiagonal1 += matriz[x][x]

	# Diagonal Secundária
	somaDiagonal2 = 0
	y = 0
	for x in range(tamanho-1, -1, -1):
		somaDiagonal2 += matriz[x][y]
		y += 1

	if somaDiagonal1 != somaDiagonal2:
		return False
	return True

	# Linhas
	for x in range (0, tamanho):
		somaLinha = 0
		for y in range(0, tamanho):
			somaLinha += matriz[x][y]
		if somaLinha != somaDiagonal1:
			return False
		return True

	# Colunas
	for x in range (0, tamanho):
		somaColuna = 0
		for y in range(0, tamanho):
			somaColuna += matriz[y][x]
		if somaDiagonal1 != somaColuna:
			return False
		return True
	
############################################################

matriz = [[ 8, 0, 7 ],
		  [ 4, 5, 6 ],
		  [ 3, 10, 2]]

if (quadradoMagico(matriz)):
	print('A matriz é um quadrado mágico')
else:
	print('A matriz não é um quadrado mágico')