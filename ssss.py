import pandas as pd

# Defina os caminhos dos arquivos CSV
caminho_csv1 = 'C:/ARQUIVOS/monetaria.csv'
caminho_csv2 = 'C:/ARQUIVOS/inflacao.csv'
caminho_csv_resultado = 'C:/ARQUIVOS/resultado.csv'

# Leia os arquivos CSV
df_monetaria = pd.read_csv(caminho_csv1)
df_inflacao = pd.read_csv(caminho_csv2)

# Realize o inner join com base na coluna 'paises'
df_resultado = pd.merge(df_monetaria, df_inflacao, on='paises', how='inner')

# Exporte o resultado para um novo arquivo CSV
df_resultado.to_csv(caminho_csv_resultado, index=False)

print(f"Arquivo resultado exportado para {caminho_csv_resultado}")
