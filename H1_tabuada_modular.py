#tabuada_modular.py: tabuada de um número (implementação modular)

def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
    print()  # imprime uma linha em branco para separar as tabuadas

# módulo principal
tabuada(5)
tabuada(7)
tabuada(9)
