import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

APP_DIR = os.path.join(BASE_DIR, "app")

DSL_CSV = os.path.join(DATA_DIR, "cmu", "DSL-StrongPasswordData.csv")

KMEANS_GRAFICO = os.path.join(
    DATA_DIR,
    "resultados",
    "grafico",
    "grafico_kmeans.csv"
)

PCA_GRAFICO = os.path.join(
    DATA_DIR,
    "resultados",
    "grafico",
    "pca_clusters.csv"
)