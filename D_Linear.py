# Linear.py: mostrar uma sequência de pares e ímpares

print(list(range(11)))

print()

for i in range(11):
    if ((i % 2) == 0):
        print(i, end=" ")
    else:
        print(end="  ")

print("\n")

for i in range(11):
    if ((i % 2) == 1):
        print(i, end=" ")   
    else:
        print(end="  ")

print("\n")

for i in range(11):
    if ((i % 2) == 0):
        print(i, end=" ")
    else:
        print(end="  ")


