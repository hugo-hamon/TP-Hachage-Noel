import random

# --- CONFIGURATION ---
FILENAME = "dataset_interplanetary.txt"
NUM_ENTRIES = 1_000_000


FIRST_NAMES = [
    # FR
    "Léo", "Gabriel", "Raphaël", "Arthur", "Louis", "Jade", "Louise", "Emma", "Alice", "Ambre",
    "Lucas", "Hugo", "Jules", "Maël", "Liam", "Chloé", "Mia", "Inès", "Léa", "Manon",
    # EN
    "James", "Robert", "John", "Michael", "David", "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth",
    "William", "Richard", "Joseph", "Thomas", "Charles", "Barbara", "Susan", "Jessica", "Sarah", "Karen",
    # ES/IT
    "Santiago", "Mateo", "Sebastián", "Leonardo", "Sofia", "Valentina", "Isabella", "Camila", "Francesco", "Giulia",
    # ASIA
    "Wei", "Hao", "Yì", "Jun", "Haruto", "Yui", "Sakura", "Min-jun", "Seo-yoon", "Ji-woo",
    # POP CULTURE & OTHERS
    "Harry", "Hermione", "Ron", "Luke", "Leia", "Anakin", "Frodo", "Samwise", "Arya", "Jon"
]

LAST_NAMES = [
    # FR
    "Martin", "Bernard", "Thomas", "Petit", "Robert", "Richard", "Durand", "Dubois", "Moreau", "Laurent",
    "Simon", "Michel", "Lefebvre", "Leroy", "Roux", "David", "Bertrand", "Morel", "Fournier", "Girard",
    # EN
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    # DE/Nordic
    "Muller", "Schmidt", "Schneider", "Fischer", "Weber", "Andersson", "Johansson", "Nielsen", "Jensen",
    # ASIA
    "Wang", "Li", "Zhang", "Liu", "Chen", "Yang", "Huang", "Zhao", "Wu", "Zhou", "Sato", "Suzuki", "Takahashi", "Tanaka",
    # POP
    "Potter", "Granger", "Weasley", "Skywalker", "Kenobi", "Baggins", "Stark", "Snow", "Wayne", "Kent"
]

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


def generate_entry():
    """Génère une ligne de données cohérente."""
    prenom = random.choice(FIRST_NAMES)
    nom = random.choice(LAST_NAMES)

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


def main():
    print("--- INITIALISATION DU GÉNÉRATEUR S.L.E.I.D ---")
    print(f"Destination: {FILENAME}")
    print(f"Volume: {NUM_ENTRIES} entrées")
    print("Génération en cours...", end="")

    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            f.write(f"{NUM_ENTRIES}\n")

            for i in range(NUM_ENTRIES):
                line = generate_entry()
                f.write(line + "\n")

                # Barre de progression simple
                if i % (NUM_ENTRIES // 10) == 0:
                    print(".", end="", flush=True)

        print(f"\n[OK] Fichier '{FILENAME}' généré avec succès.")
        print(
            f"Taille approximative : {NUM_ENTRIES * 60 / 1024 / 1024:.2f} MB")

    except IOError as e:
        print(f"\n[ERREUR] Impossible d'écrire le fichier : {e}")


if __name__ == "__main__":
    main()
