n1 = float(input("digite um número"))
n2 = float(input("digite outro número"))
res = n1/n2
print ("resultado sem formatação:", res)
print ("resultado formatado  com format:", format(res,".3f"))
print ("resultado formatado com máscara:","%.3f"%res)
print ("%.3f dividido por %.1f é igual a %.3f" %(n1, n2, res))
# teste
