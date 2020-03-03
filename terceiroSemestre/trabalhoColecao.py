'''
Marcelo Nao Takayama
TIA: 31942407
'''

################################################################################################

# FUNÇÃO NÚMERO 1

# Função para adicionar no final do vetor

def adicionaFinal(v, qtd, num):
	if qtd < 100:
		v[qtd] = num	
		qtd = qtd + 1
	return qtd

#################################################################################################

# FUNÇÃO NÚMERO 2

# Função para adicionar em uma posição específica do vetor

def adicionaPosicao(pos, num, vetor, qtd):
	if pos <= qtd and qtd < 100:
		posx = len(vetor)-1
		if pos != 0:
			for i in range (len(vetor)-1):
				vetor[posx] = vetor[posx -1]			
				posx -= 1					
			vetor[pos] = num
		else:
			print('Posição não válida')
	

######################################################################################################

# FUNÇÃO NÚMERO 3

#Função para remover o elemento de uma posição específica

def removePosicao(vetor,pos):
	i = 0
	if pos != vetor[i]:
		print('Essa posição não é válida')
	else:
		vetor[:] = [x for i,x in enumerate(vetor) if i!=pos]
	return vetor

######################################################################################################


# FUNÇÃO NÚMERO 4

#Função para remover a primeira ocorrência do elemento na coleção

def removePrimeiro(vetor, elem):
	for i in range (len(vetor)):
		if vetor[i]==elem:
			for x in range (i, len(vetor)-1):
				vetor[x] = vetor [x + 1]

			break
	print()
	print(vetor)
	return vetor


######################################################################################################

# FUNÇÃO NÚMERO 5

#Função para remover todas as ocorrências de um elemento na coleção

def removeTodos(vetor, elem):
	for i in range (len(vetor)):
		if vetor[i]==elem:
			vetor[i]=0
	return(vetor)


######################################################################################################

#FUNÇÃO NÚMERO 6

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

# FUNÇÃO NÚMERO 7

#Função para verificar se tem dois valores somados igual ao valor

def verificaSoma(vetor, elem):
	for a in range (len(vetor)):
		for b in range(len(vetor)):
			if vetor[a] + vetor[b] == elem:
				print()
				print('True')
				break
			else:
				print()
				print('False')
				break 
		break



######################################################################################################

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

#####################################################################################################

# Função principal do programa
def main():
	vetor = [0]*100
	qtd = 0
	escolha = -1

	while escolha != 8:
		print("_____________________________________________________")
		print()
		print('MENU DE ESCOLHAS')
		print()
		print('1- Adicionar um número no final do vetor')
		print('2- Adicionar um número em uma posição do vetor')
		print('3- Remover uma posição específica do vetor')
		print('4- Remover a primeira ocorrência de um elemento no vetor')
		print('5- Remover todas as ocorrências de um elemento no vetor')
		print('6- Verificar se um valor se encontra no vetor')
		print('7- Função para verificar se a soma de dois valores é igual ao elemento inserido')
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
			pos = int(input('Informe a posição em que deseja inserir um número: '))
			num = int(input('Digite o número que deseja inserir: '))
			adicionaPosicao(pos, num, vetor, qtd)
		
		elif escolha == 3:
			pos = int(input('Digite a posição que deseja remover: '))
			removePosicao(vetor, pos)

		elif escolha == 4:
			elem = int(input('Digite o número que deseja remover a primeira ocorrência no vetor: '))
			removePrimeiro(vetor, elem)
			qtd -= 1

		elif escolha == 5:
			elem = int(input("Digite o número em que se deseja remover todas as ocorrências no vetor: "))
			removeTodos(vetor, elem)

		elif escolha == 6:
			valor = int(input("Digite o valor que deseja procurar: "))
			verificaPosicao(vetor, valor)

		elif escolha == 7:
			elem = int(input('Digite o valor que deseja verificar: '))
			verificaSoma(vetor, elem)

		elif escolha == 8:
		 	break
		
		if escolha <= 7 and escolha >= 1:
			print()
			printVetor(vetor, qtd)

main()