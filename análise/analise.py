
import pandas as pd
import matplotlib.pyplot as plt

# Importar os dados
df = pd.read_csv("vendas.csv")

# Calcular o faturamento
df["Faturamento"] = df["Quantidade"] * df["Preco"]

# Exibir os dados
print("\nBASE DE VENDAS")
print(df)

# Indicadores
print("\nFATURAMENTO TOTAL:")
print(f"R$ {df['Faturamento'].sum():,.2f}")

print("\nQUANTIDADE VENDIDA:")
print(df["Quantidade"].sum())

print("\nFATURAMENTO POR PRODUTO:")
vendas = df.groupby("Produto")["Faturamento"].sum()
print(vendas.sort_values(ascending=False))

# Criar gráfico
vendas.sort_values().plot(
    kind="bar",
    title="Faturamento por Produto",
    color="steelblue"
)

plt.ylabel("Faturamento (R$)")
plt.xlabel("Produto")
plt.tight_layout()
plt.show()
