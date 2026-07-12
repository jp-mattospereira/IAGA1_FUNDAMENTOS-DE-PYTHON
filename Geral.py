#Geral.py: arquivo de módulos com operações gerais
from os import system
from time import sleep

def cls():
    system('cls')
    
def delay(tmp): # tmp em segundos
    sleep(tmp)

def parada():
    print("\nPressione [ENTER] para prosseguir. ", end="")
    input()

def confirmou(rotulo):
    op = input(rotulo)
    if ((op == "S") or (op == "s")):
        return(True)
    else:
        return(False)

def linha(tipo="*", tam=10):
    result = ""
    for i in range(tam):
        result += tipo
    return(result)


def cabecalho(titulo, ctPag, totPag, ctReg):
    if (totPag == 0):
        cls()
        print(f"{titulo}\n")
    else:
        if (ctPag != 0):
            parada()
        cls()
        ctPag = ctPag + 1
        print(f"{titulo} Página {ctPag} de {totPag}.\n")
        ctReg = 0
    return(ctPag, ctReg)
