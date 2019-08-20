'''
Marcelo Nao Takayama
TIA: 31942407
'''

################################################################################################

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

###############################################################################################

#Define a função principal do programa
def main():
    vetor = [0]*100
    quantidade = 0
    escolha = -1

    while escolha != 8:
        print('Escolha a operação que você deseja realizar: ')
        print('1- Adicionar um elemnto no final da posição.')
        print('2- Adicionar um elemento em uma posição da coleção.')
        print('3- Remover um elemento em uma posição na coleção.')
        print('4- Remover a primeira ocorrência do elemento na coleção.')
        print('5- Remover todas as ocorrências de um elemento na coleção.')
        print('6- Verificar se dado um elemento está contido na coleção.')
        print('7- Verificar se dado um valor existem dois elementos na coleção que somados é igual a um valor informado.')
        print('8- Sair')

        if escolha == 1:
            adicionaFinal(vetor, valor, tamanhoVetor)

main()



