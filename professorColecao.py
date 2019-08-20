def adicionaFinal(v,qtd, elemento):
    if qtd < 100:
        #indere o elemento
        v[qtd]=elemento
        #incremente a quantidade de elementos validos
        qtd+=1

    return qtd

def printValidos(colecao,qtd) :
    i=0
    print('colecao:',end=' ')
    while i < qtd:
        print(colecao[i],end=' ')
        i+=1
    print(']',end=' ')
    print()
        
#-- MAIN()
def main():
    #declaracao da colecao de elementos
    colecao = [0]*100
    #variável para controlar a quantidade de elementos 
    qtd=0
    opc = -1
    #comecar o menu
    while opc != 8:
        #imprime as opcoes do menu
        print("1-adicionar no final")
        print("2-adicionar em uma posicao")
        print("3-....")
        print("8-sair")
        opc = int(input())
        if opc == 1:
            elem = int(input("digite um elemento para inserir:"))
            qtd = adicionaFinal(colecao, qtd, elem)
        elif opc == 2:
            print("adicionar em uma posicao") 

        if 1<= opc and opc <= 7:
            printValidos(colecao,qtd)
        
main()