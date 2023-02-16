import csv
import os


def analyze_log(path):
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path}'\n")
        
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Arquivo inexistente: '{path}'\n")

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(f"INFO HERE\n")

def read(path):
    with open(path) as csv_file:
        file = csv.reader(csv_file)
        return [line for line in file]
