from random import *

def encryptString(string_used, cle_cryptage):
    result = ""
    result += chr(cle_cryptage+97)
    for i in range(len(string_used)):
        if randint(0,1) == 1:
            result += "!l-"
        val = ord(string_used[i])
        val += cle_cryptage
        result += chr(val)
    print(result)

def decrypt(string_used):
    result = ""
    cle_cryptage = ord(string_used[0]) - 97
    for i in range(1, len(string_used)):

        toADD = True

        if str(string_used[i]) == "!" and str(string_used[i+1]) == "l" and str(string_used[i+2]) == "-":
            toADD = False
        if str(string_used[i-1]) == "!" and str(string_used[i]) == "l" and str(string_used[i+1]) == "-":
            toADD = False
        if str(string_used[i-2]) == "!" and str(string_used[i-1]) == "l" and str(string_used[i]) == "-":
            toADD = False
        
        if toADD == True :
            val = ord(string_used[i])
            val -= cle_cryptage
            result += chr(val)
    print(result)

mon_string = input("enter string (string) : ")
operation = int(input("enter operation. 1 = encrypt; 2 = decrypt (int) : "))
if operation == 1:
    cle = int(input("enter crypting key (int) : "))


if operation == 1:
    encryptString(mon_string, cle)
elif operation == 2:
    decrypt(mon_string)
else:
    print("you got an error")