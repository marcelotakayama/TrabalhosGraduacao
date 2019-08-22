'''
Marcelo Nao Takayama
TIA: 31942407
'''

################################################################################################

# Função para adicionar no final do vetor
def adicionaFinal(v, quantidade, num, final):
	if quantidade < 100:
		v[final - quantidade] = num	
		quantidade = quantidade + 1
	return quantidade, final

#################################################################################################
# Função para adicionar em uma posição específica do vetor
def adicionaPosicao(posicao, num, vetor):
	    vetor[posicao] = num    

##################################################################################################
def moveVetor(lists, num, vetor): 
    output_list = [vetor] 
      
    for item in range(len(lists) - num, len(lists)): 
        output_list.append(lists[item]) 
        
    for item in range(0, len(lists) - num):  
        output_list.append(lists[item]) 
          
    return output_list 
   
rotate_num = 1
list_1 = [1, 2, 3, 4, 5, 6] 
 
#######################################################################################################

# Função principal do programa
def main():
	vetor = [0]*100
	quantidade = 0
	escolha = -1
	final = 99

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
			quantidade, final = adicionaFinal(vetor, quantidade, num, final)
			print(vetor)

		elif escolha == 2:
			posicao = int(input('Informe a posição em que deseja inserir um número: '))
			num = int(input('Digite o número que deseja inserir: '))
			adicionaPosicao(posicao, num, vetor)
			print(vetor)

		
		
		# elif escolha == 3:

		# elif escolha == 4:

		# elif escolha == 5:

		# elif escolha == 6:

		# elif escolha == 7:

		# elif escolha == 8:
		# 	break
		
main()

