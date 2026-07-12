def analisar_e_listar_palavras(frase):
    # 1. Limpeza de dados: remove o ponto final do término da string, se houver
    if frase.endswith("."):
        frase = frase[:-1] # Esse comando diz ao Python: "Pegue a string inteira, do começo, 
        # mas pare exatamente um caractere antes do fim". 
        #Isso remove o ponto final de forma cirúrgica, deixando a palavra limpa.
        
    # 2. Divisão: quebra a frase em uma lista de palavras usando o espaço como separador
    palavras = frase.split(" ")
    total_palavras = len(palavras)
    
    # 3. Exibição do cabeçalho do relatório
    print(f"Existem {total_palavras} palavras, sao elas:\n")
    
    # 4. Loop de enumeração sequencial (começando do índice 1)
    for indice, palavra in enumerate(palavras, start=1):
        print(f"{indice}a. palavra = {palavra}")

# Módulo Principal (Entry Point protegido)
if __name__ == "__main__":
    entrada = input()
    analisar_e_listar_palavras(entrada)