import random

sourceFile = open('annagramme.txt', 'w')
s2 =  input("entrer tout ► ")
ITERATIONS =  int(input("Itération ► "))
s=""
for i in range(len(s2)):
    if s2[i]!=" ":
        s+=s2[i]
l = list(s)
for j in range(ITERATIONS):
    random.shuffle(l) 
    r=""
    for i in range(len(s)):
        r+=l[i]
    print(r, file = sourceFile)
sourceFile.close()

