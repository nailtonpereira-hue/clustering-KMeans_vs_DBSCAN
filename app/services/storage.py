import csv
import os

from app.services.config import DATA_DIR

def read_csv(path):
    file_path = os.path.join(DATA_DIR, path)

    with open(file_path, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))
