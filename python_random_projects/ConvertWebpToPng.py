import os
from PIL import Image

# Utiliser le répertoire courant
répertoire = os.getcwd()

# Parcourir tous les fichiers du répertoire
for fichier in os.listdir(répertoire):
    if fichier.endswith('.webp'):
        # Chemin complet de l'image webp
        chemin_image_webp = os.path.join(répertoire, fichier)
        
        # Ouvrir l'image webp
        image = Image.open(chemin_image_webp)
        
        # Chemin complet de l'image png de sortie
        chemin_image_png = os.path.join(répertoire, fichier.replace('.webp', '.png'))
        
        # Convertir et enregistrer l'image en png
        image.save(chemin_image_png, 'PNG')
        
        print(f"Converti: {chemin_image_webp} -> {chemin_image_png}")

print("Conversion terminée !")
