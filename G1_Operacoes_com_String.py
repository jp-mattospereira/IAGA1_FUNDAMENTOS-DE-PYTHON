#Operacoes_com_String.py: realiza operações com uma cadeia de caracteres (String)
#Este código traz um excelente compilado de métodos de String. Em Python, métodos 
# são funções internas que servem para transformar, limpar ou analisar textos de maneira muito rápida.

s = input("informe uma palavra ou uma frase (String): ")

print()
print(s.upper())  # transforma todos os caracteres em maiúsculo
print(s.lower())  # transforma todos os caracteres em minúsculo
print('[', s.center(20), ']')  # centraliza a String em um espaço de 20 caracteres
print('[', s.center(20, '.'), ']')  # centraliza a String em um espaço de 20 caracteres, preenchendo com '.'
print(s.replace('a', '@'))  # substitui todas as ocorrências de 'a' por '@'
print(s.split(' '))  # divide a String em uma lista de palavras, usando o espaço como separador
