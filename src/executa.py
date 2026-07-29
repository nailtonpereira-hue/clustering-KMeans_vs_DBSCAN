import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from processar import processar_dados
from app.services.config import KMEANS_GRAFICO, PCA_GRAFICO, DSL_CSV 


completo, grafico = processar_dados(
    DSL_CSV,
    n_clusters=5
)


grafico.to_csv(
    PCA_GRAFICO,
    index=False
)