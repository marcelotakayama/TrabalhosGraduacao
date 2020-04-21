'''
Nome: Marcelo Takayama
TIA: 31942407
'''

# Função que calcula o resultado do polinômio
def calculaPolinomio(l, x):
    xis = 0
    xp =1 
    for a in l:
        xis += a * xp 
        xp = x * xp 
    return xis

print (calculaPolinomio([1,2,1],2))
print (calculaPolinomio([3,-6,9,12],3))