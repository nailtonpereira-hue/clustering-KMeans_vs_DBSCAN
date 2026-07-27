import pandas as pd

from app.config import DSL_CSV
from src.kmeans import executar_kmeans

# Ler o dataset
df = pd.read_csv(DSL_CSV)

# Executar o K-Means
resultado, metricas = executar_kmeans(df)

# Mostrar métricas
print(metricas)

# Salvar o CSV para o gráfico
resultado[
    ["subject", "media_H", "media_DD", "media_UD", "cluster"]
].to_csv(
    "grafico_kmeans.csv",
    index=False
)

print("Arquivo grafico_kmeans.csv salvo com sucesso!")