# Operacoes_Aritmeticas.py: realiza as operações aritméticas básicas: adição, subtração, multiplicação e divisão inteira e real

def somar(a, b): # Recebe dois números e retorna a soma
    return (a + b)

def subtrair(a, b): # Recebe dois números e retorna a subtração
    return (a - b)

def multiplicar(a, b): # Recebe dois números e retorna a multiplicação
    return (a * b)

def dividir_inteira(a, b): # Recebe dois números e retorna a divisão inteira
    return (a // b)

def dividir_real(a, b): # Recebe dois números e retorna a divisão real
    return (a / b)

def toString(a, b): # Recebe dois números e retorna uma string com os resultados das operações
    result = f" {a} + {b} = {somar(a, b)}\n" \
             f" {a} - {b} = {subtrair(a, b)}\n" \
             f" {a} * {b} = {multiplicar(a, b)}\n" \
             f" {a} // {b} = {dividir_inteira(a, b)}\n" \
             f" {a} / {b} = {dividir_real(a, b):.2f}" # Formata a divisão real para duas casas decimais
    
    return (result)


# Módulo Principal (main)
a = int(input("A: ")) # Solicita ao usuário que insira o valor de 'a' e converte para inteiro
b = int(input("B: ")) # Solicita ao usuário que insira o valor de 'b' e converte para inteiro
print() # Imprime uma linha em branco para separar os blocos de código  
print(toString(a, b)) # Chama a função toString com os valores de 'a' e 'b' e imprime o resultado