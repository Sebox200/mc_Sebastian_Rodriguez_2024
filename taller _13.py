import math

def taylor_aprox(x, n):
    aprox = 0
    for i in range(n + 1):
        aprox += ((-1)**i * x**i) / math.factorial(i)
    return aprox

def error_rel(Vv, aprxV):
    return abs((Vv - aprxV) / Vv) * 100

def main():
    x_base = 0.5
    x_t = 0.505
    x_objetivo = x_t - x_base  
    Vv = math.exp(-x_t) 
    print("Valor verdadero de f(x) en x = 0.505:", Vv)

    for n in range(16):
        aprxV = taylor_aprox(x_objetivo, n)  
        err = error_rel(Vv, aprxV)
        print(f"Aproximación de orden {n}: {aprxV}, Error relativo: {err}%")

if __name__ == "__main__":
    main()
