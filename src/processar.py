import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA


def processar_dados(
    arquivo,
    n_clusters=51,
    eps=0.5,
    min_samples=5
):

    # ======================
    # CARREGAR DADOS
    # ======================

    df = pd.read_csv(arquivo)


    # Guardar usuário
    identificacao = df[
        ["subject"]
    ].copy()


    # ======================
    # PREPARAÇÃO
    # ======================

    X = df.drop(
        columns=[
            "subject",
            "sessionIndex",
            "rep"
        ]
    )


    # valores vazios
    X = X.fillna(
        X.median()
    )


    # remover negativos
    valido = (X >= 0).all(axis=1)

    X = X[valido]

    identificacao = identificacao[valido]


    # ======================
    # NORMALIZAÇÃO
    # ======================

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)


    # ======================
    # KMEANS
    # ======================

    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=42
    )

    cluster_kmeans = kmeans.fit_predict(
        X_scaled
    )


    # ======================
    # DBSCAN
    # ======================

    dbscan = DBSCAN(
        eps=eps,
        min_samples=min_samples
    )

    cluster_dbscan = dbscan.fit_predict(
        X_scaled
    )


    # ======================
    # TABELA COMPLETA
    # ======================

    resultado = identificacao.copy()

    resultado["cluster_kmeans"] = cluster_kmeans

    resultado["cluster_dbscan"] = cluster_dbscan


    # colocar dados originais junto
    dados_originais = df.loc[
        resultado.index
    ]

    resultado = pd.concat(
        [
            dados_originais,
            resultado[
                [
                    "cluster_kmeans",
                    "cluster_dbscan"
                ]
            ]
        ],
        axis=1
    )


    # ======================
    # PCA 3D
    # ======================

    pca = PCA(
        n_components=3
    )

    dados_pca = pca.fit_transform(
        X_scaled
    )


    pca_df = pd.DataFrame(
        dados_pca,
        columns=[
            "PCA1",
            "PCA2",
            "PCA3"
        ],
        index=resultado.index
    )


    resultado_pca = pd.concat(
        [
            identificacao,
            pca_df,
            resultado[
                [
                    "cluster_kmeans",
                    "cluster_dbscan"
                ]
            ]
        ],
        axis=1
    )

    return resultado, resultado_pca