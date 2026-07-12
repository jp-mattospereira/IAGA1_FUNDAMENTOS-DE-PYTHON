# 16_Unidades.py: nome das unidades numéricas (usando Tuplas).

from random import randint

def descricao_unidade(i):
    unidades = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', \
                'seis', 'sete', 'oito', 'nove') # TUPLA com os nomes das unidades numéricas

    return(unidades[i])

# módulo principal (main)
n = int(input('Qtas unidades serão sorteadas? '))

print()

for i in range(n):
    unid = randint(0, 9)

    print(f"{unid} {descricao_unidade(unid)}")
