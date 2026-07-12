#3_Estruturas_De_Decisao.py: sinal de um número: negativo, neutro ou positivo

def sinal_I (n):
    if (n < 0): # Verifica se o número é negativo
        return ("O número fornecido é negativo.")
    if (n == 0): # Verifica se o número é neutro
        return ("O número fornecido é neutro.") 
    if (n > 0): # Verifica se o número é positivo
        return ("O número fornecido é positivo.")

def sinal_II (n):
    if (n< 0): # Verifica se o número é negativo
        return ("O número fornecido é negativo.")   
    else: # Caso contrário, verifica se o número é neutro ou positivo
        if (n == 0): # Verifica se o número é neutro
            return ("O número fornecido é neutro.") 
        else: # Caso contrário, o número é positivo
            return ("O número fornecido é positivo.")
        
def sinal_III (n):
    if (n < 0): # Verifica se o número é negativo
        return ("O número fornecido é negativo.")   
    elif (n == 0): # Verifica se o número é neutro
        return ("O número fornecido é neutro.") 
    else: # Caso contrário, o número é positivo
        return ("O número fornecido é positivo.")

# Módulo Principal (main)
tam = int(input("Quantos valores serão informados? ")) # Solicita ao usuário que insira a quantidade de valores a serem fornecidos e converte para inteiro

for i in range(tam): # Loop para iterar sobre a quantidade de valores fornecidos
    print() # Imprime uma linha em branco para separar os blocos de código

    n = int(input(f"Informe o {i + 1}º valor: ")) # Solicita ao usuário que insira o valor e converte para inteiro
    print(sinal_I (n)) # Chama a função sinal_I com o valor fornecido e imprime o resultado
    print(sinal_II (n)) # Chama a função sinal_II com o valor fornecido e imprime o resultado
    print(sinal_III (n)) # Chama a função sinal_III com o valor fornecido e imprime o resultado
