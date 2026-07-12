def mapear_sinal_lista():
    # 1. Leitura do tamanho da lista
    n = int(input())
    
    primeira_lista = []
    segunda_lista = []
    
    # 2. Captura dos elementos e aplicação das regras de negócio
    for _ in range(n):
        elemento = int(input())
        primeira_lista.append(elemento)
        
        # Classificação do sinal do elemento
        if elemento < 0:
            segunda_lista.append(-1)
        elif elemento == 0:
            segunda_lista.append(0)
        else:
            segunda_lista.append(1)
            
    # 3. Exibição dos resultados no formato exato exigido
    print(primeira_lista)
    print(segunda_lista)

# Módulo Principal (Entry Point protegido)
if __name__ == "__main__":
    mapear_sinal_lista()