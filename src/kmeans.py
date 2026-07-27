import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import adjusted_rand_score, silhouette_score


def executar_kmeans(df, n_clusters=None, random_state=42):

    if n_clusters is None:
        n_clusters = df["subject"].nunique()

    # Colunas utilizadas para as médias
    colunas_h = [c for c in df.columns if c.startswith("H.")]
    colunas_dd = [c for c in df.columns if c.startswith("DD.")]
    colunas_ud = [c for c in df.columns if c.startswith("UD.")]

    # Dados utilizados pelo algoritmo
    X = df.drop(columns=["subject", "sessionIndex", "rep"])

    # Normalização
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Modelo
    modelo = KMeans(
        n_clusters=n_clusters,
        random_state=random_state
    )

    # Agrupamento
    clusters = modelo.fit_predict(X_scaled)

    # Resultado
    resultado = df.copy()

    resultado["cluster"] = clusters

    # ==========================
    # MÉDIAS PARA VISUALIZAÇÃO
    # ==========================

    resultado["media_H"] = resultado[colunas_h].mean(axis=1)
    resultado["media_DD"] = resultado[colunas_dd].mean(axis=1)
    resultado["media_UD"] = resultado[colunas_ud].mean(axis=1)

    # ==========================
    # MÉTRICAS
    # ==========================

    ari = adjusted_rand_score(
        resultado["subject"],
        resultado["cluster"]
    )

    silhouette = silhouette_score(
        X_scaled,
        resultado["cluster"]
    )

    metricas = {
        "Número de usuários": df["subject"].nunique(),
        "Número de clusters": n_clusters,
        "ARI": ari,
        "Silhouette Score": silhouette,
        "Inércia": modelo.inertia_
    }

    return resultado, metricas