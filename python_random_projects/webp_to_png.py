import os
from PIL import Image

def convert_webp_to_png():
    # Obtenez tous les fichiers dans le répertoire courant
    files = os.listdir('.')
    
    # Parcourez tous les fichiers
    for filename in files:
        # Vérifiez si l'extension du fichier est .webp
        if filename.endswith('.webp'):
            # Ouvrez l'image .webp
            img = Image.open(filename)
            # Changez l'extension du nom de fichier en .png
            png_filename = filename[:-5] + '.png'
            # Enregistrez l'image au format .png
            img.save(png_filename, 'PNG')

# Appel de la fonction
convert_webp_to_png()