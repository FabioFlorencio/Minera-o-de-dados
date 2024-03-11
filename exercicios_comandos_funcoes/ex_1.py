'''
    1 - Criar uma função que receba dois valores do tipo String e retorne  a concatenação de valores em uma frase;    

'''
def juntar_frases (frase1, frase2):
    concatenar = frase1 + ' ' + frase2
    return concatenar

frase1 = input(str(f'Digite uma frase:'))
frase2 = input(str(f'Digite outra frase:'))

frase_concatenada = juntar_frases(frase1, frase2)

print(frase_concatenada)

