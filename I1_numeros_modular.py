# Numeros_modular.py: apresenta os ‘n’ primeiros números inteiros positivos (implementação modular)

#Módulo Mostrar
def mostrar(n): # Recebe o valor de n e exibe os n primeiros números inteiros positivos
    print("{", end="")
    for i in range(1, n+1):
        print(f"{i}", end=", ")
    print("}", end="")
print()  # imprime uma linha em branco para separar os blocos de código

#Módulo Somar
def somar(n): #Recebe o valor de n e calcula a soma dos n primeiros números inteiros positivos
    soma = 0
    for i in range(1, n+1):
        soma = soma + i
    return (soma) #Depois de calcular a soma, o valor é retornado para o módulo principal
print()

#Módulo Resultados
def resultados(n): # Recebe o valor de n e chama os módulos mostrar e somar para exibir os resultados
    mostrar(n)
    print(f"\n \n Soma = {somar(n)}") 
    print()  # imprime uma linha em branco para separar os blocos de código

#Módulo Principal
resultados(5) # Chama a função resultados com o valor 5
resultados(10) # Chama a função resultados com o valor 10