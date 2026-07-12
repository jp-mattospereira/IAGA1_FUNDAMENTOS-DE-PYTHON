# 4_Tabuada.py: tabuada de um número

def tabuada_I (n): # Recebe um número e retorna a tabuada de 1 a 10
    i = 1 # Inicializa a variável i com 1
    while (i <= 10): # Loop enquanto i for menor ou igual a 10
        print(f"{n} x {i} = {n * i}") # Imprime a tabuada do número n multiplicado por i
        i += 1 # Incrementa i em 1  
        print() # Imprime uma linha em branco para separar os blocos de código


def tabuada_II (n): # Recebe um número e retorna a tabuada de 1 a 10
    for i in range(1, 11): # Loop de 1 a 10
        print(f"{n} x {i} = {n * i}") # Imprime a tabuada do número n multiplicado por i
        print() # Imprime uma linha em branco para separar os blocos de código  

# Módulo Principal (main)
while True: # Loop infinito para permitir que o usuário insira vários números
    print("Informe -1 para encerrar o programa.") # Informa ao usuário como encerrar o programa
    n = int(input("De 0 a 10, informe o número para gerar a tabuada: ")) # Solicita ao usuário que insira o valor de 'n' e converte para inteiro
    if (n == -1): # Verifica se o usuário deseja encerrar o programa
        break # Encerra o loop

    if (n < 0 or n > 10): # Verifica se o número está fora do intervalo de 0 a 10
        print("Número inválido. Informe um número entre 0 e 10.") # Informa ao usuário que o número é inválido
        continue # Retorna ao início do loop para solicitar um novo número  
    else: # Caso o número esteja dentro do intervalo de 0 a 10
        print() # Imprime uma linha em branco para separar os blocos de código  
        print(tabuada_I (n)) # Chama a função tabuada_I com o valor de 'n' e imprime o resultado
        print(tabuada_II (n)) # Chama a função tabuada_II com o valor de 'n' e imprime o resultado

print("Programa encerrado.") # Informa ao usuário que o programa foi encerrado
