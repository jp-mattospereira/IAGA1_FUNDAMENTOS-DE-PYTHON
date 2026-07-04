# Numeros_modular.py: apresenta os ‘n’ primeiros números inteiros positivos (implementação modular)

#Módulo Mostrar
def mostrar(n):
    print("{", end="")
    for i in range(1, n+1):
        print(f"{i}", end=", ")
    print("}", end="")
print()  # imprime uma linha em branco para separar os blocos de código

#Módulo Somar
def somar(n):
    soma = 0
    for i in range(1, n+1):
        soma = soma + i
    return (soma)
print()

#Módulo Resultados
def resultados(n):
    mostrar(n)
    print(f"\n \n Soma = {somar(n)}") 
    print()  # imprime uma linha em branco para separar os blocos de código

#Módulo Principal
resultados(5)
resultados(10)