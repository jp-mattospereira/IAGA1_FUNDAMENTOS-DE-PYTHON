# 14_Ler_TXT.py: lê arquivos de texto

from Geral import cls, parada

while True:
    nomeArquivo = input("Informe o nome do arquivo (FIM para encerrar):\n") # 
    if (nomeArquivo.upper() == "FIM"):
        break

    print()

    try: # Tenta abrir o arquivo de texto no modo de leitura
        arquivo = open(nomeArquivo, "r")
        linhas = arquivo.readlines()
        print("*** Conteúdo do arquivo:")
        for linha in linhas:
            print(linha, end="")

        print()
        parada()
        arquivo.close()
        cls()

    except IOError: # Se ocorrer um erro de entrada/saída (por exemplo, se o arquivo não for encontrado), exibe uma mensagem de erro
        print(f"Erro: o arquivo \"{nomeArquivo}\", não foi encontrado.\n")
