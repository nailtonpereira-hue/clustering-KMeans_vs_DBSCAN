import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


import pandas as pd

from sklearn.preprocessing import StandardScaler

from processar import processar_dados
from testes import encontrar_eps

from app.services.config import (
    PCA_GRAFICO,
    DSL_CSV
)


# ======================
# PREPARAR DADOS PARA EPS
# ======================

df = pd.read_csv(
    DSL_CSV
)


X = df.drop(
    columns=[
        "subject",
        "sessionIndex",
        "rep"
    ]
)


X = X.fillna(
    X.median()
)


scaler = StandardScaler()

X_scaled = scaler.fit_transform(
    X
)


# ======================
# CALCULAR EPS
# ======================

eps = encontrar_eps(
    X_scaled,
    min_samples=38
)


# ======================
# PROCESSAR
# ======================

completo, grafico = processar_dados(
    DSL_CSV,
    eps = 1.7,
    min_samples = 3
)


grafico.to_csv(
    PCA_GRAFICO,
    index=False
)