# -*- coding: utf-8 -*-
"""
Name of developer: Najman
Name of program: pyth_calcu-2.py
Description: 1.	Write functions in Python to do addition, subtraction, division and multiplication operations


Date Created:       Thu, 11 July 2023, 19:56:00
Date last update:   Thu, 11 July 2023

@author: evoma
"""

gvfirst_no = 100
gvsecond_no = 20
print('Type:', type(gvfirst_no))
print('ID:', id(gvfirst_no))
print('Type:', type(gvsecond_no))
print('ID:', id(gvsecond_no))

def calc():
    lvresult = ( gvfirst_no + gvsecond_no)
    # lvresult is a local variable
    # local value cant be used outside 'def calc()'
    return lvresult