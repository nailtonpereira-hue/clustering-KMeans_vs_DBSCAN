from sklearn.neighbors import NearestNeighbors
from kneed import KneeLocator
import numpy as np
import matplotlib.pyplot as plt


def encontrar_eps(X, min_samples=5):

    vizinhos = NearestNeighbors(
        n_neighbors=min_samples
    )

    vizinhos.fit(X)

    distancias, _ = vizinhos.kneighbors(X)

    distancias = np.sort(
        distancias[:, min_samples - 1]
    )


    kneedle = KneeLocator(
        range(len(distancias)),
        distancias,
        curve="convex",
        direction="increasing"
    )


    if kneedle.knee is None:
        raise Exception(
            "Não foi possível encontrar o cotovelo do gráfico"
        )


    eps = distancias[kneedle.knee]


    print("======================")
    print("EPS encontrado:", eps)
    print("======================")


    plt.figure(figsize=(10,5))
    plt.plot(distancias)

    plt.axhline(
        eps,
        color="red",
        linestyle="--",
        label=f"eps={eps:.3f}"
    )

    plt.legend()
    plt.grid()
    plt.show()


    return eps