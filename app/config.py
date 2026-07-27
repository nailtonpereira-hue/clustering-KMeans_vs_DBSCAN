import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

APP_DIR = os.path.join(BASE_DIR, "app")

DSL_CSV = os.path.join(DATA_DIR,"raw/cmu/DSL-StrongPasswordData.csv")

CENARIOS_FILE = os.path.join("metadata","cenarios.csv")