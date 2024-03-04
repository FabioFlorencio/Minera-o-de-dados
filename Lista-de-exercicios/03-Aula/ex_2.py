'''  
2 -Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero e imprimir o resultado da divisão do primeiro valor lido pelo segundo valor.

'''

while True:
    
    valor_informado_1 = float(input("Digite o primeiro valor: "))
    valor_informado_2 = float(input("Digite o segundo valor: "))
    
    if valor_informado_2 != 0:
        resultado = valor_informado_1 / valor_informado_2
        print("O resultado da divisão é:", resultado)
        break
    else:
        print("O segundo valor digitado não pode ser ZERO. Por favor, digite outro número")
