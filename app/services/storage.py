import csv
import os

from app.config import DATA_DIR

def list_csv(folder="raw/local"):
	path = os.path.join(DATA_DIR, folder)
	arquivos = []
	for arquivo in os.listdir(path):
		if arquivo.endswith(".csv"):
			arquivos.append(arquivo)
	return arquivos

def read_csv(path):
	file_path = os.path.join(DATA_DIR, path)
	with open(file_path, "r", encoding="utf-8") as file:
		reader = csv.DictReader(file) 
		return list(reader)
