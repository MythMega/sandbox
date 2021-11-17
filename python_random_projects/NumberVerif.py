from math import *
from typing import List

### return True if it's a number
def isNumber(une_variable):
    verification = False
    try:
        my_number = int(une_variable)
        return True
    except ValueError:
        return True

### return a list of all divisors
def getDivisors(my_number):
    divisor = 0
    list_divisors = []
    for i in range(2,my_number):
        if my_number%i == 0:
            divisor = i
            list_divisors.append(divisor)
    return list_divisors


### print info (Prime) about a number, and divisor if it isn't a Prime
def isPrime(my_number):
    is_prime = True
    divisor = 0
    for i in range(2,my_number):
        if my_number%i == 0:
            is_prime=False
            divisor = i
            break

    if is_prime==True:
        print(f'Le nombre {my_number} est premier')
    else:
        print(f'Le nombre {my_number} nest pas premier, il est divisible par {divisor}')


### return true if number is prime
def isPrime_bool(my_number):
    is_prime = True
    divisor = 0
    for i in range(2,my_number):
        if my_number%i == 0:
            is_prime=False
            divisor = i
            break
    if is_prime==True:
        return True
    else:
        return False

### return true if number is pair
def isPair(my_number):
    if my_number%2==0:
        return True
    else :
        return False

### return true if number is positive
def isPositive(my_number):
    if my_number>=0:
        return True
    else:
        return False

### return a positive number
def toPositive(my_number):
    return sqrt(my_number * my_number)

#les nombres parfaits, qui sont égaux à la somme de leurs diviseurs entiers naturels sauf eux-mêmes. On en connaît 48 
def isPerfect(my_number):
    myDivisorList = list()
    mon_calcul = 0
    for i in range(1,my_number):
        if my_number%i==0:
            myDivisorList.append(i)
    for i in range(len(myDivisorList)):
        mon_calcul += myDivisorList[i]
    if mon_calcul == my_number:
        return True
    else:
        return False

### return True if b is a (multiple) of b
def isMultiple(my_number,my_divisor):
    if my_number%my_divisor==0:
        return True
    else:
        return False
