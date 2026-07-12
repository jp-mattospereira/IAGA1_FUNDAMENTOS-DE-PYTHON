# 13_Ler_Pacientes.py: lê os pacientes IMC cadastrados

import Calculadora_IMC
import Geral

# 1a. etapa: abrir o arquivo de texto no mode de leitura
arquivo = open("pacientes.txt", "r")

# 2a. etapa: ler as linhas do arquivo de texto 
linhas = arquivo.readlines()
for linha in linhas:
    partes = linha.split("; ")
    
    paciente = partes[0]
    pc = float(partes[1])
    alt = float(partes[2])
    
    print(Calculadora_IMC.toString(paciente, pc, alt))

# 3a. etapa: fechar o arquivo de texto
arquivo.close()
