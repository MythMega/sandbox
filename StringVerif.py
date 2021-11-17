from unicodedata import *
from itertools import *

def removeAccents(text):
    text = normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

def isPalindrome(mon_string):
    mon_string = mon_string.upper()
    mon_string = removeBadChar(mon_string)
    mon_string = removeAccents(mon_string)
    a = len(mon_string)
    result = True
    for i in range(a//2):
        target = a-i-1
        if mon_string[i] != mon_string[target]:
            result = False
    return result

def cleanString(mon_string):
    mon_string = mon_string.upper()
    mon_string = removeBadChar(mon_string)
    mon_string = removeAccents(mon_string)
    return mon_string

def removeBadChar(mon_string):
    x = ""
    y = ""
    z = "-, _'.;!?"
    mytable = mon_string.maketrans(x, y, z)
    resultat = mon_string.translate(mytable) 
    return resultat

def areAnagramme(mon_pre_string, mon_deu_string):
    mon_deu_string = cleanString(mon_deu_string)
    mon_pre_string = cleanString(mon_pre_string)
    return sorted(mon_pre_string)==sorted(mon_deu_string)

