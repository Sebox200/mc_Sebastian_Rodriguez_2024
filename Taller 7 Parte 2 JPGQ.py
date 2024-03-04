import math
print("Se Va A Evaluar e^-0.75 Por Medio De la segunda Aproximación")

iteraciónes = 1
signo = 1
x = -0.75
n = 2
Es = (0.5 * 10**-8) * 100
Ea = 100
e = 1
a = 1

while Ea > Es and e > Es:
    valor_anterior = e
    
    e += (1 / x * signo * (x**a / math.factorial(n)))

    Ea = abs((e - valor_anterior) / e) * 100

    iteraciónes += 1
    n += 2
    signo *= -1
    a += 1

print(e)
print(Ea)
print(iteraciónes)
