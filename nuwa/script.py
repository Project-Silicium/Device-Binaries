import subprocess

# Chemin vers le fichier d'entrée contenant les noms d'INF et les GUID
input_file = "/home/alfa/Téléchargements/apriori"

# Ouvrir le fichier d'entrée en mode lecture
with open(input_file, 'r') as file:
    # Parcourir chaque ligne dans le fichier
    for line in file:
        # Diviser la ligne en mots séparés par des espaces
        words = line.split()
        # Si la ligne contient un GUID
        if len(words) > 1 and '-' in words[1]:
            # Extraire le GUID
            guid = words[1]
            # Exécuter la commande rg -i GUID
            result = subprocess.run(["rg", "-i", guid], capture_output=True, text=True)
            # Récupérer la sortie de la commande
            output = result.stdout.strip()
            # Si la commande a retourné un résultat, ajouter Binaries/i005d/ devant le chemin
            if output:
                path = output.split(':')[0]
                new_path = "INF " + "Binaries/nuwa/" + path
                print(new_path)
            else:
                print("GUID non trouvé:", guid)
        else:
            # Si la ligne ne contient pas de GUID, laisser la ligne telle quelle
            print(line.strip())
