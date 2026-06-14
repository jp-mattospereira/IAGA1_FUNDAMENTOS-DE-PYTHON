#realiza as operações matemáticas: dobro, triplo, quadrado, cubo e raiz quadrada.

from math import sqrt

n = int(input("n:"))

dobro = n * 2
triplo = n * 3
quadrado = n ** 2
cubo = n ** 3
raizQuadrada = sqrt(n)

print()
print(f"n.............: {n}, tem-se:")
print(f"dobro.........: {dobro}")
print(f"triplo........: {triplo}")
print(f"quadrado......: {quadrado}")
print(f"cubo...........: {cubo}")
print(f"raiz quadrada..: {raizQuadrada:.4f}")
