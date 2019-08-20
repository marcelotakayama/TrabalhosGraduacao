'''
Marcelo Nao Takayama
TIA: 31942407
'''

# Função para adicionar um elemento no final do vetor 
def adicionaFinal (vetor, valor):
	vetor += [valor]
	return vetor


# Define o tamanho do vetor
tamanhoVetor = int(input('Digite o tamanho do vetor: '))
vetor = [0] * tamanhoVetor


while True: 
	valor = int(input('Informe o valor a ser adicionado no final do vetor: '))

	print(adicionaFinal(vetor, valor))

	# Verifica se o vetor possui menos de 100 posições
	if len(vetor) == 100:
		break
		
print('O vetor não possui mais posições possíveis para serem adicionadas!')


#def adicionaPosicao(vetor, posicao):