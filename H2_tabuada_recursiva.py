# tabuada_recursiva.py: tabuada de um número implementado de forma recursiva

# Até agora, vínhamos usando loops (for ou while) para repetir tarefas. A recursividade faz a mesma 
# repetição, mas de um jeito diferente: é uma função que chama a si mesma para resolver um problema 
# em etapas menores. Pense nisso como aquelas bonecas russas (Matrioskas), onde você abre uma e tem 
# outra igual dentro, até chegar na menor de todas.

# módulo 'tabuada' usando recursividade

def tabuada(n, i): # Recebe dois parâmetros: n (o número para o qual queremos a tabuada) e i (o multiplicador atual)
    if (i <= 10): # Condição de parada: enquanto i for menor ou igual a 10, continue a recursão
        print(f"{n} x {i} = {n * i}") # Imprime o resultado da multiplicação
        i = i+1 # Incrementa i em 1
        tabuada(n, i) # Chama a função novamente com i incrementado em 1
    else: # Caso contrário, quando i for maior que 10, a recursão termina
        print() # Imprime uma linha em branco para separar os blocos de código

# Módulo Principal
tabuada(5, 1) # Chama a função tabuada com n=5 e i=1, iniciando a tabuada do 5
tabuada(7, 1) # Chama a função tabuada com n=7 e i=1, iniciando a tabuada do 7
tabuada(9, 1) # Chama a função tabuada com n=9 e i=1, iniciando a tabuada do 9
