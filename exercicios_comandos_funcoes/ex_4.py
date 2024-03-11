'''
    Criar uma função que receba a variável anterior e verifique se o mesmo é um número PRIMO.

'''

num = int(input('Numero: '))
e_Primo = 0

for i in range(1, (num + 1)):        
  if num % i == 0:
    e_Primo += 1
    
if e_Primo  == 2 :
  print('È um número primo')
else:
  print('não é um número primo')
  


