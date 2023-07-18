import os
from PIL import Image

# Variables pour stocker les dimensions maximales
max_hauteur = 0
max_largeur = 0
# Obtenir le chemin absolu du dossier actuel
dossier_actuel = os.path.dirname(os.path.abspath(__file__))

# Parcourir les fichiers du dossier actuel
for fichier in os.listdir(dossier_actuel):
    # Vérifier si le fichier est une image
    if fichier.endswith(('.jpg', '.jpeg', '.png')):
        # Construire le chemin absolu du fichier
        chemin_fichier = os.path.join(dossier_actuel, fichier)
        
        # Ouvrir l'image et obtenir sa taille
        with Image.open(chemin_fichier) as img:
            largeur, hauteur = img.size
            
            
            # Afficher la taille de l'image
            print(f"Image : {fichier}")
            print(f"Largeur : {largeur}px")
            print(f"Hauteur : {hauteur}px")
            print()
            
            # Mettre à jour les dimensions maximales si nécessaire
        if hauteur > max_hauteur:
            max_hauteur = hauteur
        if largeur > max_largeur:
            max_largeur = largeur

# Afficher les dimensions maximales
print("Hauteur maximale :", max_hauteur)
print("Largeur maximale :", max_largeur)