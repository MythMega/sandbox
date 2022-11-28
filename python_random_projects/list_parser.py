#la liste doit etre au format suivant ["x y z","x y z","x y z"]
#Permet de rajouter des étapes intermédiaire entre deux coordonnées, en faisant la motié du chemin entre une coordonnée A & B, à partir d'une liste de
#String "coordonnée_a coordonnée_b coordonée_c", en ajoutant les coordonées intérmédiaire et en les insérants entre celles ci
class List_Parser:
    def parserListCoordonnes(uneListe) -> list:
        resultat = []
        resultat.append(uneListe[0])
        for i in uneListe:
            if not i == uneListe[0]:
                pass
            else:
                currentCoords = i.split(" ")
                currentX = currentCoords[0]
                currentY = currentCoords[1]
                currentZ = currentCoords[2]

                lastCoords = resultat[-1].split(" ")
                lastX = lastCoords[0]
                lastY = lastCoords[1]
                lastZ = lastCoords[2]

                moyX = (lastX+currentX)/2
                moyY = (lastY+currentY)/2
                moyZ = (lastZ+currentZ)/2

                resultat.append(f"{moyX} {moyY} {moyZ}")
                resultat.append(i)
        return resultat