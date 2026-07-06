# numeros_recursivo.py: apresenta os ‘n’ primeiros números inteiros positivos de forma recursiva

# módulo 'mostrar' usando a recursividade

def mostrar(n, i): # Recebe o valor de n e exibe os n primeiros números inteiros positivos
    if (i <= n): # Condição de parada: enquanto i for menor ou igual a n, continue a recursão
        if (i == 1): # Se i for igual a 1, imprime a abertura do conjunto
            print("{", end="")  
        
        print(f"{i}", end=", ") # Imprime o valor atual de i
        i = i + 1 # Incrementa i em 1
        mostrar(n, i) # Chama a função novamente com i incrementado em 1
    else: # Caso contrário, quando i for maior que n, a recursão termina
        print("}", end="") # Imprime o fechamento do conjunto
        print()  # imprime uma linha em branco para separar os blocos de código

# Módulo 'somar' usando a recursividade
def somar(n, i): # Recebe o valor de n e calcula a soma dos n primeiros números inteiros positivos
    if (i <= n): # Condição de parada: enquanto i for menor ou igual a n, continue a recursão
        novoI = i + 1 # Incrementa i em 1
        return (i + somar(n, novoI)) # Retorna a soma de i com a chamada recursiva da função somar
    else: # Caso contrário, quando i for maior que n, a recursão termina
        return (0) # Retorna 0 para encerrar a recursão
    
# Módulo 'resultados' usando a recursividade
def resultados(n): # Recebe o valor de n e chama os módulos mostrar e somar
    mostrar(n, 1) # Chama a função mostrar com n e i=1
    print(f"\n \n Soma = {somar(n, 1)}") # Chama a função somar com n e i=1 e imprime o resultado
    print()  # imprime uma linha em branco para separar os blocos de código

# Módulo Principal
resultados(3) # Chama a função resultados com o valor 5
resultados(10) # Chama a função resultados com o valor 10
