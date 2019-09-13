def sort(lista):
    elementos = len(vetor)-1
    x = False
    while not x:
        x = True
        for i in range(elementos):
            if vetor[i] > vetor[i+1]:
                vetor[i], vetor[i+1] = vetor[i+1],vetor[i]
                x = False        
                print(vetor)
    return vetor

vetor = [3,5,9,11,15,17,19, 0]

num = int(input("Digite um número: "))
vetor [-1] = num

print(vetor)
sort(vetor)