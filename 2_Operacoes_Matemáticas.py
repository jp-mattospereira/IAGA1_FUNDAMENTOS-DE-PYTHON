#2_Operacoes_Matemáticas.py: realiza as operações matemáticas: dobro, triplo, quadrado, cubo e raiz quadrada 

from math import sqrt # Importa a função sqrt do módulo math para calcular a raiz quadrada

def dobro(a): # Recebe um número e retorna o dobro
    return (a * 2)

def triplo(a): # Recebe um número e retorna o triplo
    return (a * 3)

def quadrado(a): # Recebe um número e retorna o quadrado
    return (a ** 2) 

def cubo(a): # Recebe um número e retorna o cubo
    return (a ** 3)

def raiz_quadrada(a): # Recebe um número e retorna a raiz quadrada
    return (sqrt(a))


def toString(a): # Recebe um número e retorna uma string com os resultados das operações
    result = f"Sendo o número fornecido = {a}, tem-se que:\n" \
             f" O dobro é: {dobro(a)}\n" \
             f" O triplo é: {triplo(a)}\n" \
             f" O quadrado é: {quadrado(a)}\n" \
             f" O cubo é: {cubo(a)}\n" \
             f" A raiz quadrada é: {raiz_quadrada(a):.4f}" # Formata a raiz quadrada para duas casas decimais
    
    return (result)

# Módulo Principal (main)
a = int(input("A: ")) # Solicita ao usuário que insira o valor de 'a' e converte para inteiro
print() # Imprime uma linha em branco para separar os blocos de código
print(toString(a)) # Chama a função toString com o valor de 'a'

