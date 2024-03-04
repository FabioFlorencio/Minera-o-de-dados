'''
01 - Faça um algoritmo que determine o maior entre N números. A condição de parada é a entrada de um valor 0, ou seja, o algoritmo deve ficar calculando o maior até que a entrada seja igual a 0 (ZERO).

'''

numeros = []

while True:
    qualquer_numero = float(input("Digite um número, caso queira encerrar digite o número 0"))

    if qualquer_numero == 0:
        break

    numeros.append(qualquer_numero)

if numeros:
    maior_numero = max(numeros)    
    print("O maior número é:", maior_numero)
else:
    print("Foi encerrado aplicação pelo usuário!")
