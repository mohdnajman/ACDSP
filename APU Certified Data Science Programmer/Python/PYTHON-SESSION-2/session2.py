# -*- coding: utf-8 -*-
"""
Name of developer: Najman
Name of program: session2.py
Description: Lesson 2
    
Date Created:       Thu, 15 June 2023
Date last update:   Thu, 15 June 2023
"""

cars_array = ['Proton', 'Volvo', 'BMW']
numbers_array = [5,15,25,2,7]
letter = ['c', 'd', 'a', 'b']
 # cars and number is an array
 # an array holds a set of values or elements
 # position / index of an array starts with 0

# print all the elements in the array
for x in cars_array:
    print(x)
    
for x in numbers_array:
    print(x)
    
# print the numbers of elements in the array
print('Number of elements is cars_array' +str(len(cars_array)))
print('Number of elements is numbers_array' +str(len(numbers_array)))

name = 'Mohammad Najman bin Md Noor'

print('number of letters found in my name', len(name))

salary = 2300
tv_price = 199.90

print(type(salary))
print(type(tv_price))

# to remove 'BMW' from the cars_array
cars_array.remove('BMW')

print(cars_array)

# to add new car name into cars_array
cars_array.append('Honda')
cars_array.append('Ferrari')

print(cars_array)

# remove an element based on particular position or index
cars_array.pop(1)

print(cars_array)

# sort the elements
# ascending order
numbers_array.sort()
print('Ascending order: ', numbers_array)
# descending order
numbers_array.sort(reverse=True)
print('Descending order: ', numbers_array)

# find the position of an element in the array
x = cars_array.index('Ferrari')
print(x)

# add a new element to specific index/location
cars_array.insert(1, 'Kancil')
print(cars_array)

# remove all the elements in an array
cars_array.clear()
print(cars_array)

num_array = [5, 23, 50, 14, 70]

total_value = 0

for x in num_array:
    total_value = total_value + x
    print(total_value)
    
else:
    print('Total is: ' +str(total_value))