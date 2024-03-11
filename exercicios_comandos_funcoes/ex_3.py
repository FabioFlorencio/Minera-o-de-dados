'''
    Criar uma função que receba a série de números criados anteriormente e retorne uma média dos valores (Utilizar a função SUM e LEN);
'''

import random

lista_num_aleatorios = []

def calcula_media_valores(lista_num_aleatorios):
    result_media = sum(lista_num_aleatorios) / len(lista_num_aleatorios)
    return result_media 

for i in range(10):
    num = random.randint(0,100)
    lista_num_aleatorios.append(num)

print(lista_num_aleatorios)     

retorna_media = calcula_media_valores(lista_num_aleatorios)

print(f'Média dos valores aleatórios:{retorna_media}')
