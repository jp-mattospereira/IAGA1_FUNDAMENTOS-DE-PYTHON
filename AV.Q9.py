def construir_lista_indexada(a):
    x = []
    
    # 1. Loop para calcular e preencher a lista com as 10 posições
    for i in range(10):
        resultado_calculo = a + i
        x.append(resultado_calculo)
        
    # 2. Loop para exibição formatada com alinhamento rigoroso
    for i in range(10):
        print(f"x[{i}] = {a} + {i} = {x[i]}")

# Módulo Principal (Entry Point protegido)
if __name__ == "__main__":
    # Captura o valor inteiro 'a' digitado pelo usuário
    valor_a = int(input())
    construir_lista_indexada(valor_a)