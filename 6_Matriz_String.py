# 6_Matriz_String.py: monta uma matriz triangular inferior com os caracteres de uma String

def matriz_string (s): # Recebe uma String e retorna uma matriz triangular inferior com os caracteres da String
    n = len(s) # Calcula o tamanho da String
    for i in range(n): # Loop de 0 a n-1
        for j in range(i + 1): # Loop de 0 a i
            print(s[j], end=" ") # Imprime o caractere da String na posição j seguido de um espaço, sem quebrar a linha
        print() # Imprime uma linha em branco para separar os blocos de código

# Módulo Principal (main)
s = input("Informe uma String: ") # Solicita ao usuário que insira uma String
print() # Imprime uma linha em branco para separar os blocos de código
matriz_string (s) # Chama a função matriz_string com a String fornecida
