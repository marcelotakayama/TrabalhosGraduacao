a,b,c = input().split()

a = float(a)
b = float(b)
c = float(c)

triangulo = (a * c) / 2
circulo = (c * c) * 3.14159
trapezio = ((a+b) * c)/2
quadrado = b * b
retangulo = a * b

print("TRIANGULO:", format(triangulo, ".3f"))
print("CIRCULO:", format(circulo, ".3f"))
print("TRAPEZIO:", format(trapezio, ".3f"))
print("QUADRADO:", format(quadrado, ".3f"))
print("RETANGULO:", format(retangulo, ".3f"))
        

