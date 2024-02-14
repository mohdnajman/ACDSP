# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 18:36:19 2023

@author: evoma
"""

course_name = 'PYTHON PROGRAMMING LANGUAGE'
string_to_search = 'MING'
index_position = 0
is_found = False
index_position = course_name.find(string_to_search)
if index_position > 0:
    is_found = True
    print('The string is found in the ' +str(index_position))
elif index_position == 0:
    print('The string is not found')

print(string_to_search in course_name)

# or

print('MING' in 'PYTHON PROGRAMMING LANGUAGE')

# or

print(course_name.find(string_to_search))

"""
2. Write a program in Python to convert a string into upper-case and into lower-case
"""

course_name = 'PYTHON LANGUAGE'
print('Print the course name in upper-case: ' +course_name.upper())
print('Print the course name in lower-case: ' +course_name.lower())
print(course_name.replace('G','g'))
print(course_name.replace('LANGUAGE','IS A PROGRAMMING LANGUAGE'))
print(course_name.replace('LANGUAGE', 'IS ONE OF THE BEST PROGRAMMING LANGUAGES'))

"""
3. Write a program in Python to practice if-else condition
"""

salary = int(input('Please enter your salary: '))
if salary >= 0 and salary <= 1000:
   print('A grade')
elif salary >= 1001 and salary <= 2000:
    print('B grade')
elif salary >= 2001 and salary <= 3000:
    print('C grade')
elif salary >= 3001 and salary <= 5000:
    print('D grade')
elif salary >= 5001 and salary <= 10000:
    print('E grade')
elif salary >= 10001 and salary <= 15000:
    print('G grade')
elif salary >= 15001 and salary <= 20000:
    print('H grade')
elif salary >= 20001 and salary <= 32000:
    print('B grade')
else: print('J grade')

"""
4. Write a program in Python to practice list - data type variable
"""

a = 10 # integer
b = 10.5 # float
my_number_list = [23,41,14,16,50]

print(type(a))
print(type(b))
print(type(my_number_list))

print(my_number_list[0])
print('Length of the list: ' +str(len(my_number_list)))
print('Highest value found in the list: ' +str(max(my_number_list)))
print('Lowest value found in the list: ' +str(max(my_number_list)))