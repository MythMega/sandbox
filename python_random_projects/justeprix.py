from math import ceil
from random import *

def verif(monGuess, leResultat):
    if monGuess == leResultat:
        print(f"C'est gagné, GG ! Le résultat était bien {leResultat}")
        return True
    else:
        if monGuess < leResultat:
            print("C'est plus ! (+)")
        else:
            print("C'est moins ! (-)")
        return False

def selectionResultat(unNiveau):
    monMaxSecret = 10**unNiveau
    monMinSecret = 10**ceil(unNiveau/10)
    monSecret = randint(monMinSecret, monMaxSecret)
    print(f"Vous avez choisis le niveau de difficulté {unNiveau}, donc la valeur à trouver est inclue entre {monMinSecret} et {monMaxSecret}.")
    return monSecret

#start

unNiveau = int(input("Entrez une difficulté de 1 à 10: "))
monSecret = selectionResultat(unNiveau)
resultat = False
while (resultat == False):
    print("----")
    unGuess = int(input("tentez de trouver : "))
    resultat = verif(unGuess, monSecret)
print