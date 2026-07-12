# 10_Meus_Divisores.py: mostrar todos os divisores de um número

from Meu_Math import divisores, ehPrimo
from Vetor import saida


while True:
    n = int(input("Digite um número inteiro positivo (ou -1 para sair): "))
    if n == -1:
        break

    x = divisores(n)
    print(saida(f"Divisores de {n}", x))
    if ehPrimo(n):
        print(f"{n} é um número primo.\n")

print()
