vetor = [10,9,8,7,6,5,4,3,2,1]

def buscaBinaria(vetor, item):
	esquerda = 0 
	direita = len(vetor)-1

	while esquerda <= direita:
		meio = esquerda + direita // 2
		if vetor[meio] == item:
			return meio
		elif vetor[meio] > item:
			
			esquerda = meio + 1
		else:
			direita = meio - 1
	return -1

print(buscaBinaria(vetor, 8))