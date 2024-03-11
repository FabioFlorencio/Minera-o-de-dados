'''
    2 -Criar série de 10 números inteiros;

'''
import random

lista_num_aleatorios = []

for i in range(10):
    num = random.randint(0,100) 
    lista_num_aleatorios.append(num)
    
print(lista_num_aleatorios)    


