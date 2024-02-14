# -*- coding: utf-8 -*-
"""
Name of developer: Najman
Name of program: pyth_calcu.py
Description: 1.	Write functions in Python to do addition, subtraction, division and multiplication operations


Date Created:       Thu, 11 July 2023, 19:56:00
Date last update:   Thu, 11 July 2023

@author: evoma
"""

# addition operation

def addi(pfirst_no, psecond_no):
    lvresult = pfirst_no + psecond_no
    return lvresult

# substraction operation

def subst(pfirst_no, psecond_no):
    lvresult = pfirst_no - psecond_no
    return lvresult

# division operation

def divi(pfirst_no, psecond_no):
    lvresult = pfirst_no / psecond_no
    return lvresult

# multiplication operation

def multi(pfirst_no, psecond_no):
    lvresult = pfirst_no * psecond_no
    return lvresult

a = addi(100,20)
print('Addition result:', a)
print('Data type:', type(a))
print('Memory id/location:', id(a))
# another way to print the result
# print('Addition result:' str(a))
b = subst(100,20)
print('Substraction result:', b)
print('Data type:', type(b))
print('Memory id/location:', id(b))
c = divi(100,20)
print('Division result:', c)
print('Data type:', type(c))
print('Memory id/location:', id(c))
d = multi(100,20)
print('Multiplication result:', d)
print('Data type:', type(d))
print('Memory id/location:', id(d))

def calcu(pfirst_no,psecond_no,poperator):
    lvresult = 0 #this is a local variable
    if poperator == '+':
        lvresult = pfirst_no + psecond_no
    elif poperator == '-':
        lvresult = pfirst_no - psecond_no
    elif poperator == '/':
        lvresult = pfirst_no / psecond_no
    elif poperator == '*':
        lvresult = pfirst_no * psecond_no
    else :
        print('Enter a valid symbol')
    return lvresult