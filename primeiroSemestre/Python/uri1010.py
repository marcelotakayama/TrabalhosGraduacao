c1, n1, v1 = input().split()
c2, n2, v2 = input().split()

c1 = int(c1)
n1 = int(n1)
v1 = float(v1)
c2 = int(c2)
n2 = int(n2)
v2 = float(v2)

calculo = n1*v1 + n2*v2

print  ("VALOR A PAGAR: R$",format(calculo, ".2f"))