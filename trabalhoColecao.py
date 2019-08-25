'''
Marcelo Nao Takayama
TIA: 31942407
'''

################################################################################################

# Função para adicionar no final do vetor
def adicionaFinal(v, qtd, num):
	if qtd < 100:
		v[qtd] = num	
		qtd = qtd + 1
	return qtd

#################################################################################################
# Função para adicionar em uma posição específica do vetor
def adicionaPosicao(posicao, num, vetor):
	vetor[posicao] = num    

##################################################################################################
def moveDireita(novoVetor, vetor): 
	n = 1
	vetor = vetor 
	novoVetor = (vetor[len(vetor) - n:len(vetor)] + vetor[0:len(vetor) - n]) 
	print(novoVetor) 
 
#######################################################################################################

#Função para printar o vetor de forma mais bonita

def printVetor(vetor, qtd):
	i = 0
	print('vetor: [', end = ' ')
	while i < qtd:
		print(vetor[i], end = ' ')
		i += 1
	print(']', end = ' ')
	print()

######################################################################################################
# Função principal do programa
def main():
	vetor = [0]*100
	qtd = 0
	escolha = -1

	while escolha != 8:
		print('1- Adicionar um número no final do vetor')
		print('2- Adicionar um número em uma posição do vetor')
		print('3- Opção 3')
		print('4- Opção 4')
		print('5- Opção 5')
		print('6- Opção 6')
		print('7- Opção 7')
		print('8- Sair do programa')

		escolha = int(input('Informe a opção que deseja realizar: '))

		if escolha == 1:
			num = int(input('Digite o número que deseja inserir: '))
			qtd = adicionaFinal(vetor, qtd, num)

		elif escolha == 2:
			posicao = int(input('Informe a posição em que deseja inserir um número: '))
			num = int(input('Digite o número que deseja inserir: '))
			adicionaPosicao(posicao, num, vetor)

		
		# elif escolha == 3:

		# elif escolha == 4:

		# elif escolha == 5:

		# elif escolha == 6:

		# elif escolha == 7:

		# elif escolha == 8:
		# 	break
		
		if escolha <= 7 and escolha >= 1:
			printVetor(vetor, qtd)

main()
