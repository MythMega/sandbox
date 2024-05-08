# Va upscale toutes les vidéos en 1920*1080 dans le répertoire, nécessite Python et FFMPEG d'installé.

import os
import subprocess

# Parcourir tous les fichiers dans le répertoire courant
for fichier in os.listdir('.'):
    # Vérifier si le fichier est un .mp4
    if fichier.endswith('.mp4'):
        # Utiliser ffmpeg pour obtenir la résolution du fichier
        cmd = f'ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {fichier}'
        resolution = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        # Vérifier si la résolution est différente de 1920x1080
        if resolution != '1920x1080':
            # Utiliser ffmpeg pour upscale la vidéo à 1920x1080
            cmd = f'ffmpeg -i {fichier} -vf scale=1920:1080 {fichier[:-4]}_upscaled.mp4'
            subprocess.run(cmd, shell=True)