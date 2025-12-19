import random
import csv
import os

# --- CONSTANTS ---
FILE_PRENOMS = "insee_data/prenom.csv"
FILE_PATRONYMES = "insee_data/patronymes.csv"

# --- CONFIGURATION ---
FILENAME = "dataset_interplanetary.txt"
NUM_ENTRIES = 1_000_000


FIRST_NAMES = []
LAST_NAMES = []

STREET_TYPES = ["Rue", "Avenue", "Boulevard", "Impasse", "Chemin",
                "Place", "Allée", "Lane", "Street", "Road", "Way", "Drive"]

STREET_NAMES = [
    "de la Paix", "Victor Hugo", "de la République", "Pasteur", "des Fleurs", "du Moulin",
    "Main", "Broadway", "High", "Park", "Oak", "Pine", "Maple", "Cedar", "Elm", "Washington",
    "Piccadilly", "Oxford", "Regent", "Abbey", "Baker",
    "Sakura", "Fuji", "Kyoto",
    "Privet Drive", "Diagon Alley", "Grimmauld Place", "Bagshot Row", "Evergreen Terrace", "Wisteria Lane"
]

CITIES = [
    "Paris", "Lyon", "Marseille", "Bordeaux", "Lille",
    "London", "Manchester", "Liverpool", "Edinburgh",
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Tokyo", "Osaka", "Kyoto",
    "Berlin", "Munich", "Hamburg",
    "Madrid", "Barcelona", "Seville",
    "Rome", "Milan", "Naples",
    "Beijing", "Shanghai", "Seoul", "Sydney", "Toronto", "Gotham", "Metropolis", "Hogsmeade"
]


def load_csv_column(filepath, column_name):
    """Charge une colonne spécifique d'un fichier CSV dans une liste."""
    data_list = []
    if not os.path.exists(filepath):
        print(f"Fichier introuvable : {filepath}")
        return []

    try:
        with open(filepath, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data_list.extend(
                row[column_name].strip()
                for row in reader
                if column_name in row and row[column_name]
            )
    except Exception as e:
        print(f"Problème lors de la lecture de {filepath} : {e}")

    return data_list


def generate_entry(first_names, last_names):
    """Génère une ligne de données cohérente."""
    prenom = random.choice(first_names).capitalize()
    nom = random.choice(last_names).capitalize()

    # Age pondéré : beaucoup d'enfants (1-12), des ados (13-17), peu de majeurs
    age_roll = random.random()
    if age_roll < 0.7:
        age = random.randint(1, 12)
    elif age_roll < 0.95:
        age = random.randint(13, 17)
    else:
        # Quelques erreurs...
        age = random.randint(18, 99)

    # Adresse
    num = random.randint(1, 999)
    type_voie = random.choice(STREET_TYPES)
    nom_voie = random.choice(STREET_NAMES)
    zip_code = random.randint(10000, 99999)
    ville = random.choice(CITIES)
    adresse = f"{num} {type_voie} {nom_voie}, {zip_code} {ville}"

    est_sage = 1 if random.random() < 0.7 else 0

    # Format CSV : Nom;Prenom;Age;Adresse;Sage
    return f"{nom};{prenom};{age};{adresse};{est_sage}"


def main(first_names, last_names):
    print(f"Destination: {FILENAME}")
    print(f"Volume: {NUM_ENTRIES} entrées")
    print("Génération en cours...", end="")

    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            f.write(f"{NUM_ENTRIES}\n")

            for i in range(NUM_ENTRIES):
                line = generate_entry(first_names, last_names)
                f.write(line + "\n")

                if i % (NUM_ENTRIES // 10) == 0:
                    print(".", end="", flush=True)

        print(f"\nFichier '{FILENAME}' généré correctement.")
        print(
            f"Taille approximative : {NUM_ENTRIES * 60 / 1024 / 1024:.2f} MB")

    except IOError as e:
        print(f"\nImpossible d'écrire le fichier : {e}")


if __name__ == "__main__":
    FIRST_NAMES = load_csv_column(FILE_PRENOMS, "prenom")
    LAST_NAMES = load_csv_column(FILE_PATRONYMES, "patronyme")
    main(FIRST_NAMES, LAST_NAMES)
