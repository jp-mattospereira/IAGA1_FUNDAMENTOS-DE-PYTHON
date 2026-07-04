# Tabuada_sequencial.py: tabuada de um número (implementação sequencial)
# Este código é um excelente exemplo para demonstrar como o loop for funciona para automatizar tarefas
# repetitivas — neste caso, gerar tabuadas. O termo "implementação sequencial" no título indica que o
# código faz isso bloco por bloco (primeiro a tabuada do 5, depois a do 7, e por fim a do 9), repetindo
# a mesma estrutura de código três vezes.

n=5
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
print()  # imprime uma linha em branco para separar as tabuadas
 
n=7
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
print()  # imprime uma linha em branco para separar as tabuadas

n=9
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
print()  # imprime uma linha em branco para separar as tabuadas