def moveDireita(novoVetor, vetor): 
	novoVetor = (vetor[len(vetor) - n:len(vetor)] + vetor[0:len(vetor) - n]) 
	print(novoVetor) 

	
n = 1
vetor = [1, 2, 3, 4, 5, 6] 

moveDireita(n, vetor)