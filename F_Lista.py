#Lista.py: entrada e saída de dados usando uma Lista

n = int(input("Tamanho da lista?"))

print()

soma = 0
l = []

for i in range(n):
    item = int(input(f"{i+1}º item da lista: "))
    soma = soma + item
    l.append(item)
print()

# 1a. forma: print da lista
print(l, "soma =", soma)
print()

# 2a. forma: print da lista por item usando for
for item in l:
    print(item, end=", ")
print("soma =", soma)
print()

#3a. forma: com acesso indexado
print("[", end="")
for i in range (len(l)):
    print(f"{l[i]}", end="")
    if (i != len(l)-1): #não é o último item, então imprime uma vírgula
        print(", ", end="")
print("] soma =", soma)

l.sort() #ordena a lista em ordem crescente
print("\nLista ordenada:", l)