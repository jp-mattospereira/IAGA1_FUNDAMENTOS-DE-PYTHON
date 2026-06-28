#Este código mistura o conceito de manipulação de textos (Strings) com aqueles dois loops alinhados
#  (for dentro de for) que estudamos antes.
# O objetivo dele é ler uma palavra que você digitar e imprimi-la no terminal em formato de "escada" 
# ou "pirâmide", letra por letra, separadas por uma barra vertical |.

while True:
    S = input("Digite uma palavra (ou 'sair' para encerrar): ")
    if (S.upper() == "SAIR"):
        print("Programa encerrado.")
        break
    print()

    for i in range(len(S)): 
        for j in range(i + 1):
            print(S[j], end=" |") 
        print()

    