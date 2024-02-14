# -*- coding: utf-8 -*-
"""
Name of developer: Najman
Name of program: sets_and_its_operation.py
Description: 1.	Write functions in Python to handle sets and its operations.
    
Date Created:       Thu, 13 July 2023
Date last update:   Thu, 13 July 2023
"""

"""
Sets - is a data type
     - holds a collection of values/data
     - no duplication is allowed in sets
     - it is faster than the lists, array and dictionary
     - no indexing concept is used in sets
"""

# # set
# s = {1, 3, 2, 4, 6, 5, 3}

# # list
# l = [1, 3, 2, 4, 6, 5, 3]

# print(s)
# print(type(s))

# print(l)
# print(type(l))

""""
find the max and min value in a set
"""

# s1 = {1, 3, 2, 4, 'a', 'Python'}

# s2 = {1, 2, 3, 5, 50, 7}

# print('Highest number: ', max(s2))
# print('Lowest number: ', min(s2))

# lowest_number = min(s2)
# print(type(lowest_number))

"""
print sum of values found in the set s2
"""

# result = sum(s2)
# print(result)

# s1 = {1, 3, 2, 4, 6, 5}
# s2 = {1, 8, 9, 10, 12}
# print('S1: ', s1)
# print('S2: ', s2)
# s2.update(s1)
# print(s1)
# print(s2)

"""
1st method - remove a value from set using .remove (preferred)

'KeyError: ' message will appear if the value is not found 
-> only 1st method will show error message so it is preferred
"""

# s12 = {6, 7, 8, 45, 80}
# print(s12)
# print(len(s12))
# s12.remove(6)
# print(s12)

"""
2nd method - remove a value from set using .discard
-> try to avoid using this method
"""

# s12.discard(45)
# print(s12)

"""
3rd method - remove a value from set using .pop
.pop -> removes the value at first index position
"""

# s12.pop()
# print(s12)
# s12.pop()
# print(s12)

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = {3, 4, 5}

"""
find the same value found in different sets
"""

# s4 = s1.intersection(s2, s3)
# print(s4)
# s4 = s2.intersection(s3)
# print(s4)

"""
find the different value found in different sets
"""

# s5 = s1.difference(s2, s3)
# print(s5)
# s5 = s2.difference(s3)
# print(s5)

"""
find the different value found in different sets
"""

# s4 = list(s1.symmetric_difference(s2))
# print(s4)

# l1 = [1, 2, 3, 1, 2, 3] # list can hold duplicate values 
#                         # and it can be processed
#                         # set can't hold duplicate values
                        
# s1 = set(l1)            # convert to set
# print(l1)
# print(s1)

# convert list to set
employees = ['Zilong', 'David', 'Azlina', 'Chow', 'Pathfinder', 'Dhason']
exp_23years_and_above = ['Dhason', 'David', 'Zilong']
python_devs = ['Azlina', 'Chow', 'Dhason']

emp = set(employees)
exp23 = set(exp_23years_and_above)
pydev = set(python_devs)

result = emp.intersection(exp23, pydev)
print('Python dev and 23 years exp: ', result)

result = emp.difference(exp23, pydev)
print('Not python dev and not 23 years exp: ', result)

result = emp.symmetric_difference(exp23)
print('Employees who does not have 23 years exp: ', result)

result = emp.symmetric_difference(pydev)
print('Employees who are not python developer: ', result)
