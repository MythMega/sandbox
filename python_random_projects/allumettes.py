def displayAllumettes(nbrAllumettes, allumettesMax):
    resultat = " [ "
    for _ in range(nbrAllumettes):
        resultat += "|"
    for _ in range(allumettesMax-nbrAllumettes):
        resultat += "•"
    resultat += " ] "
    return resultat

allumettesMax = int(input("Nombre max d'allumettes : "))
nbrAllumettes = allumettesMax
print(f"Il y a {allumettesMax} allumettes au début")
running = True
display = displayAllumettes(nbrAllumettes, allumettesMax)
while(running == True):
    print("-----------")
    action = 0
    while(action < 1 or action > 3):
        action = int(input("Nombre d'allumettes à enlever (1 à 3) : "))
        if (action < 1 or action > 3):
            print("Error, retry, fdp")
        else:
            nbrAllumettes -= action
    if nbrAllumettes > 0:
        print(f"Il reste {nbrAllumettes} allumettes.")
        display = displayAllumettes(nbrAllumettes, allumettesMax)
        print(display)
    else:
        print("c'est perdu")
        running = False