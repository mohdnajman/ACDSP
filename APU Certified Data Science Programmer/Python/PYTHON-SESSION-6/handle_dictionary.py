# -*- coding: utf-8 -*-
"""
Name of developer: Najman
Name of program: handle_dictionary.py
Description: 2.	Write a program in Python to handle ‘dictionary’ data type variables

Date Created:       Thu, 22 June 2023
Date last update:   Thu, 22 June 2023

Dictionary
- special data type like list and tuple
- used to store keys and values (pair)
- the elements/items/values found in a dictionary can be changed

C,C++, JAVA, PYTHON,RM6,000
COBOL - 1989-90 JOB STREET
"""

emp_dict = {'E01': 'Dhason',
            'E02': 'Najman',
            'E03': 'Messi',
            'E04': 'Ronialdo'}
print('Number of pairs(keys & values) found in the emp_dict: ', len(emp_dict))
print('E01: ', emp_dict['E01'])
print('E02: ', emp_dict['E02'])

#emp_dict.pop('E01') # remove the item that paired with E01 key

# loop to print values
for i in emp_dict:
    item = emp_dict[i]
    print(item)

print('List of keys: ')
for kunci in emp_dict.keys():
    item = kunci
    print(item)

# result are boolean type
print('Searching for an item inside the emp_dict')
print('E01' in emp_dict)
print('E01' not in emp_dict)

