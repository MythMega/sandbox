from PIL import Image
import os

SIZE_X = 112
SIZE_Y = 112

def resize_images():
    # Récupérer la liste des fichiers d'images dans le répertoire courant
    image_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    for file_name in image_files:
        # Ouvrir l'image d'origine avec prise en charge de la transparence
        img = Image.open(file_name).convert('RGBA')
        width, height = img.size

        # Calculer les marges pour centrer l'image de base dans le nouveau canevas transparent
        left_margin = (SIZE_X - width) // 2
        top_margin = (SIZE_Y - height) // 2

        # Créer un nouveau canevas transparent avec une taille de 112x112 pixels
        new_img = Image.new('RGBA', (SIZE_X, SIZE_Y), (0, 0, 0, 0))
        new_img.paste(img, (left_margin, top_margin), mask=img)

        # Enregistrer l'image redimensionnée avec le suffixe "-edited"
        new_file_name = os.path.splitext(file_name)[0] + "-edited" + os.path.splitext(file_name)[1]
        new_img.save(new_file_name)

        print(f"Image {file_name} redimensionnée et enregistrée sous {new_file_name}")

# Appeler la fonction pour redimensionner les images
resize_images()