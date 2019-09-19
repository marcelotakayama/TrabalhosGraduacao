'''
Exercício exemplo de uma soma de dois vetores diferentes em que 
além de serem salvos em uma string, essa nova string que contém a soma
não possuirá nenhum elemento repetido dos dois vetores.
'''

# Vetores já pré-definidos
a = [2, 4, 5, 6]
b = [1, 2, 3, 7]

def somaVetores(a, b):
	# String em que a soma será armazenada
	string = ''    
	# For que adiciona os elementos de 'a' na string
	for x in range(len(a)):
		string += str(a[x]) + ' '
	# For que adiciona os elementos de 'b' na string caso eles não  
	# estejam em 'a' para não repetir elementos
	for y in range(len(b)):
		if b[y] not in a:
			string += str(b[y]) + ' '
	return string

# Método para chamar a função
print(somaVetores(a, b))