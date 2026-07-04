# numeros_sequencial.py: apresenta os ‘n’ primeiros números inteiros positivos (implementação sequencial)

n = 5

print("{ ", end="")
for i in range(1, n + 1):
    print(f"{i}", end="")
print(" }", end="")

print()  # imprime uma linha em branco para separar os blocos de código
      
soma = 0
for i in range(1, n + 1):
    soma += i
print(f"soma = {soma}")
print()  # imprime uma linha em branco para separar os blocos de código}")
