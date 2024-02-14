# -*- coding: utf-8 -*-
"""
Name of developer: Najman
Name of program: handle_tuple.py
Description: 1.	Write a program in Python to handle ‘tuple’ data type variables

Date Created:       Thu, 22 June 2023
Date last update:   Thu, 22 June 2023

Tuple
- a special data type like list
- faster than list
- used to hold data permanently
- used to keep heterogenous data types
"""

mytuple_a = (5,10, 23,50,5.3,'Kailan',[4,5,6])
print(type(mytuple_a))
print('List the elements/items/values found in the tuple a: ', mytuple_a)

mytuple_b = 5,10, 23,50,5.3,'Kailan',[4,5,6]
print(type(mytuple_b))
print('List the elements/items/values found in the tuple b: ', mytuple_b)
"""
print('1st element found in the tuple a: ', mytuple_a[0])
print('6th element found in the tuple a: ', mytuple_a[5])
print('7th element found in the tuple a: ', mytuple_a[6])
print('The last element in the tuple a: ', mytuple_a[-1])
print('The 2nd last element in the tuple a: ', mytuple_a[-2])
print('The number elements found in the tuple a: ', len(mytuple_a))
print('elements found in 2nd to 4th index: ', mytuple_a[2:4])
print('Elements/items/values from 1st to 3rd index position: ', mytuple_a[:3])
print('Elements/items/values from 3rd index position: ', mytuple_a[3:])

print('Kailan' in mytuple_a) # true statement operator
print('Kailan' not in mytuple_a) # false statement operator
"""

for i in mytuple_a:
    print(type(i))
    print(i)