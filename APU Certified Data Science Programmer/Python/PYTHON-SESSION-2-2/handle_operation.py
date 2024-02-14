# -*- coding: utf-8 -*-
"""

Name of developer: Najman
Name of program: handle_operation.py
Description: Learning

Date Created:       Thu, 6 July 2023, 19:56:00
Date last update:   Thu, 6 July 2023

Author: evoman
"""

filename = 'C:\\Users\\evoma\\anaconda\\Scripts\\mytxtfile.txt'
f = open(filename,'r') #r is the mode of operation

"""
mode of operation 
r > reading operation
w --> writing operation mode
r --> reading and appending operation
"""

print('Variable type of filename:', type(filename))
print('Variable type of f:', type(f))
print('Print the data found in this file:')
#print(f)

"""
Read the data found in the file and store it inside the variable 'content'
"""

my_content = f.read()
print(my_content)
print("Mode of operation:", f.mode)
print('File name:', f.name)
print('Is closed?', f.closed)

#close the file 'f'
f.close()
print("Is closed?", f.closed)

#read the first 16 characters found in the file
f = open(filename, 'r')
content = f.read(16)
print(content)
print('Pointer position:', f.tell())

#read the next 16 characters found in the file
f = open(filename, 'r')
content = f.read(16)
print(content)
print('Pointer position:', f.tell())

#readline() functions read the data found in a file line-byline
f = open(filename, 'r')
eachline = f.readline()
print(eachline)

eachline = f.readline()
print(eachline)
print('Data type:', type(eachline))

#readlines() function read all the found in a file and saves it in a list variable
f = open(filename, 'r')
eachline = f.readlines()
print(eachline)
print('Data type:', type(eachline))

#read the data found in a file using 'for loop'
#lstrip() is a function to trim/remove the blank spaces
#found in the left side of a string

f = open(filename, 'r')
eachline = f.readlines()
for line in eachline:
    print(line)

print(type(eachline))
f.close()

#writing operations 'w' in files:

    
f = open(filename, 'w')
f.write('Python')
f.write('C')
f.write('C++')
f.write('C#')
f.write('Java')
f.write('PASCAL')
f.write('CLIPPER')
f.write('FOXPRO')
f.close()
