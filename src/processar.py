import pandas as pd
import numpy as np

from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA


# ======================
# ESTATÍSTICAS
# ======================

def mostrar_estatisticas(nome, clusters):

    valores, quantidades = np.unique(
        clusters,
        return_counts=True
    )

    total = len(clusters)

    print("\n======================")
    print(nome)
    print("======================")

    print(
        "Total de amostras:",
        total
    )


    quantidade_clusters = len(valores)

    if -1 in valores:
        quantidade_clusters -= 1


    print(
        "Quantidade de clusters:",
        quantidade_clusters
    )


    if -1 in valores:

        ruido = quantidades[
            valores == -1
        ][0]

        print(
            "Ruído (-1):",
            ruido,
            f"({ruido/total*100:.2f}%)"
        )


    tamanhos = quantidades[
        valores != -1
    ]


    if len(tamanhos) > 0:

        print(
            "Maior cluster:",
            np.max(tamanhos)
        )

        print(
            "Menor cluster:",
            np.min(tamanhos)
        )

        print(
            "Média por cluster:",
            round(np.mean(tamanhos), 2)
        )


    print("======================")


# ======================
# PROCESSAMENTO
# ======================

def processar_dados(
    arquivo,
    n_clusters=57,
    eps=1.7,
    min_samples=3
):

    # ======================
    # CARREGAR DADOS
    # ======================

    df = pd.read_csv(arquivo)


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


    X = X.fillna(
        X.median()
    )


    valido = (X >= 0).all(axis=1)


    X = X[valido]

    identificacao = identificacao[valido]



    # ======================
    # NORMALIZAÇÃO
    # ======================

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)



    # ======================
    # ANÁLISE DE DISTÂNCIA
    # ======================

    vizinhos = NearestNeighbors(
        n_neighbors=5
    )

    vizinhos.fit(X_scaled)


    distancias, _ = vizinhos.kneighbors(
        X_scaled
    )


    distancias = np.sort(
        distancias[:,4]
    )


    print("\n======================")
    print("DISTÂNCIAS")
    print("======================")

    print(
        "Menor distância:",
        distancias[0]
    )

    print(
        "Mediana:",
        np.median(distancias)
    )

    print(
        "Maior distância:",
        distancias[-1]
    )

    print("======================")



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


    mostrar_estatisticas(
        "K-MEANS",
        cluster_kmeans
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


    mostrar_estatisticas(
        "DBSCAN",
        cluster_dbscan
    )


    print("======================")
    print("EPS usado:", eps)
    print("Clusters encontrados:")
    print(
        np.unique(
            cluster_dbscan,
            return_counts=True
        )
    )
    print("======================")



    # ======================
    # TABELA COMPLETA
    # ======================

    resultado = identificacao.copy()


    resultado["cluster_kmeans"] = cluster_kmeans

    resultado["cluster_dbscan"] = cluster_dbscan



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