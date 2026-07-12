# 5_Matriz.py: monta uma matriz de números

def matriz_I (n): # Recebe um número e retorna uma matriz de 1 a n
    i = 0 # Inicializa a variável i com 0
    while (i < n): # Loop enquanto i for menor que n
        j = 0 # Inicializa a variável j com 1
        while (j < n): # Loop enquanto j for menor ou igual a n
            print(f"{i}{j}", end=" ") # Imprime o valor de j seguido de um espaço, sem quebrar a linha
            j = j + 1 # Incrementa j em 1
        print() # Imprime uma linha em branco para separar os blocos de código
        i = i + 1 # Incrementa i em 1

def matriz_II (n): # Recebe um número e retorna uma matriz de 1 a n
    for i in range(n+1): # Loop de 0 a n
        for j in range(n + 1): # Loop de 0 a n
            print(f"{i} {j}", end=" ") # Impri  me o valor de j seguido de um espaço, sem quebrar a linha
        print() # Imprime uma linha em branco para separar os blocos de código

#módulo Principal (main)
n = int(input("informe o tamanho da matriz: ")) # Solicita ao usuário que insira o valor de 'n' e converte para inteiro
print() # Imprime uma linha em branco para separar os blocos de código

matriz_I (n) # Chama a função matriz_I com o valor de 'n'
print() # Imprime uma linha em branco para separar os blocos de código
matriz_II (n) # Chama a função matriz_II com o valor de 'n'
print() # Imprime uma linha em branco para separar os blocos de código
