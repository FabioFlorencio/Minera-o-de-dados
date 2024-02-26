# Variáveis

nome = "Fábio Florêncio de Mendonça"
idade = 41


print(f"Nome: {nome}")
print(f"Idade: {idade}")

# Operações Matemáticas
# +, -, *, /

soma = idade + 5
subtracao = idade - 5
multiplicacao = idade * 5 
divisao = idade / 5

print(f"\nSoma: {soma}")
print(f"Subtração:{subtracao}")
print(f"Multiplicação:{multiplicacao}")
print(f"Divisão:{divisao}\n")

# Concatenação

frase = "Nome:" + nome + ", idade: " + str(idade) + " anos."

print(f"Frase concatenada: {frase}")

# Operações de comparação

teste_idade = idade >= 18
teste_nome = nome == "fábio florêncio de mendonça"

print(f"\nIdade é true? {teste_idade}")
print(f"Nome é true? {teste_nome}\n")

# Funções

tamanho_nome = len(nome)

print(f"Quantidade de caracteres:{tamanho_nome}\n")

# Laços 

for i in range(6):
    print(i)

print("\n")

numero = 1 

while numero <= 5:
    print(numero)
    numero += 1












