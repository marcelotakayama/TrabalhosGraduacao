def sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False        
                print(lista)
    return lista

vetor = [3,5,9,11,15,17,19, 0]

num = int(input("Digite um número: "))
vetor [-1] = num

print(vetor)
sort(vetor)