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

def adicionaPosicao(posicao, num, vetor, novoVetor):
	if posicao == [0]:
		vetor[posicao] = num
	else:
		moveDireita(vetor, vetor)  
		vetor[posicao] = num  

##################################################################################################

def moveDireita(novoVetor, vetor): 
	n = 1
	vetor = vetor
	novoVetor = (vetor[len(vetor) - n:len(vetor)] + vetor[0:len(vetor) - n]) 
	return novoVetor
 
#######################################################################################################

#Função para printar o vetor de forma mais visual

def printVetor(vetor, qtd):
	i = 0
	print('********************************************************')
	print('Vetor: [', end = ' ')
	while i < qtd:
		print(vetor[i], end = ' ')
		i += 1
	print(']', end = ' ')
	print()
	print('********************************************************')

######################################################################################################

#Função para verificar se o valor se encontra no vetor

def verificaPosicao(vetor, valor):
	a = vetor
	b = [i for i in range(len(a)) if a[i]==valor]
	if valor not in vetor:
		print()
		print('--------------------------------------------------------')
		print("O valor está na(s) posições: -1")
		print('--------------------------------------------------------') 
	else:
		print()
		print('--------------------------------------------------------')
		print("O valor está na(s) posições: ", b)
		print('--------------------------------------------------------') 

######################################################################################################

#Função para remover todas as ocorrências de um elemento na coleção

def removeTodos(vetor, elem):
	for i in range (len(vetor)):
		if vetor[i]==elem:
			vetor[i]=0
	return(vetor)

######################################################################################################

#Função para remover o elemento de uma posição específica

def removePosicao(vetor,pos):
	i = 0
	if pos != vetor[i]:
		print('Essa posição não é válida')
	else:
		vetor[:] = [x for i,x in enumerate(vetor) if i!=pos]
	return vetor

######################################################################################################
# Função principal do programa
def main():
	vetor = [0]*100
	qtd = 0
	escolha = -1

	while escolha != 8:
		print()
		print("_________________________________________________________")
		print()
		print('MENU DE ESCOLHAS')
		print()
		print('1- Adicionar um número no final do vetor')
		print('2- Adicionar um número em uma posição do vetor')
		print('3- Remover uma posição específica do vetor')
		print('4- Opção 4')
		print('5- Remover todas as ocorrências de um elemento no vetor')
		print('6- Verificar se um valor se encontra no vetor')
		print('7- Opção 7')
		print('8- Sair do programa')
		print()
		print("_________________________________________________________")
		print()

		escolha = int(input('Informe a opção que deseja realizar: '))
		print()

		if escolha == 1:
			num = int(input('Digite o número que deseja inserir: '))
			qtd = adicionaFinal(vetor, qtd, num)

		elif escolha == 2:
			posicao = int(input('Informe a posição em que deseja inserir um número: '))
			num = int(input('Digite o número que deseja inserir: '))
			adicionaPosicao(posicao, num, vetor)

		
		elif escolha == 3:
			pos = int(input('Digite a posição que deseja remover: '))
			removePosicao(vetor, pos)

		# elif escolha == 4:

		elif escolha == 5:
			elem = int(input("Digite o número que deseja remover: "))
			removeTodos(vetor, elem)

		elif escolha == 6:
			valor = int(input("Digite o valor que deseja procurar: "))
			verificaPosicao(vetor, valor)

		# elif escolha == 7:

		elif escolha == 8:
		 	break
		
		if escolha <= 7 and escolha >= 1:
			print()
			printVetor(vetor, qtd)

main()