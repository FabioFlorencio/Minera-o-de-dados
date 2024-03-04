

#Importação do Pandas
import pandas as pd

#DataFrame
dados = {
    "Nome": ["Ana", "João", "Pedro"],
    "Idade": [45, 10, 35],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}

df = pd.DataFrame(dados)
#print(df)

idades = df["Idade"]
#print(idades.mean())

# Acrescenta uma nova coluna no DataFrame
df["Estado"] = ["SP", "RJ", "MG"]

df = df.sort_values("Idade")

#print(df)

#df.to_csv(exemplo_df.csv)
