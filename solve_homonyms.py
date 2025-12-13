import os

# --- CONFIGURATION ---
INPUT_FILENAME = "dataset_interplanetary.txt"
OUTPUT_FILENAME = "dataset_interplanetary_unique.txt"


def process_uniqueness(input_file, output_file):
    """
    Lit le fichier d'entrée, assure l'unicité des noms en ajoutant un suffixe
    numérique (_1, _2, etc.) aux doublons, et écrit le résultat.
    """

    name_tracker = {}

    print("--- DÉBUT DU TRAITEMENT D'UNICITÉ ---")
    print(f"Lecture : {input_file}")
    print(f"Écriture : {output_file}")

    if not os.path.exists(input_file):
        print(
            f"[ERREUR] Le fichier {input_file} n'existe pas. Lancez le générateur d'abord.")
        return

    try:
        with (open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out):

            header = f_in.readline()
            if not header:
                print("[ERREUR] Fichier vide.")
                return

            f_out.write(header)

            try:
                total_lines = int(header.strip())
            except ValueError as e:
                raise ValueError("La première ligne n'est pas un nombre.") from e

            line_count = 0

            for line in f_in:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(';')

                if len(parts) < 5:
                    raise ValueError("La ligne est mal formée.")

                original_name = parts[0]

                if original_name in name_tracker:
                    name_tracker[original_name] += 1
                    count = name_tracker[original_name]
                    new_name = f"{original_name}_{count}"
                    parts[0] = new_name
                else:
                    name_tracker[original_name] = 0

                new_line = ";".join(parts)
                f_out.write(new_line + "\n")

                line_count += 1

                if line_count % (total_lines // 10 if total_lines > 10 else 1) == 0:
                    print(".", end="", flush=True)

        print(f"\n[TERMINÉ] Traitement fini.")
        print(f"Fichier unique généré : {OUTPUT_FILENAME}")
        print(f"Nombre total d'enfants traités : {line_count}")

    except Exception as e:
        print(f"\n[ERREUR CRITIQUE] : {e}")


if __name__ == "__main__":
    process_uniqueness(INPUT_FILENAME, OUTPUT_FILENAME)
