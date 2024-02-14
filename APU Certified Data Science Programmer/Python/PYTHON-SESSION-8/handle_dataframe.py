# -*- coding: utf-8 -*-
"""

Name of developer: Mod Man
Name of program: handle_dataframe.py
Date first write: 27/06/2023
Date last update: 27/06/2023

"""

# Import/Load the Pandas Library
import pandas as pd
emp = {'fname': ['MAD', 'ALI', 'CR7'],
       'lname': ['MAN','G','Siiiiiuuuuuuu'],
       'email': ['najmanxda@gmail.com', 'zlatanibrahimovic@gmail.com','2000tonne@gmail.com']}

"""
To print the contents of the dictionary
"""

print(emp)

"""
To print data type of the emp
"""

print(type(emp))

"""
To load the data to dataframe

DataFrame -> It is 2-dimensional data structure to hold
data in a table form (rows&column)
"""

df = pd.DataFrame(emp)

"""
To print the contents of the dataframe df
"""

print(df)

"""
To print the data found in a column
"""

print(df['fname'])

"""
To add a new column to the DataFrame df
"""

df['full_name'] = df['fname'] + ' ' + df['lname']
print(df)

"""
To delete 'full_name' column from the dataframe df
"""

df.drop(columns = ['full_name'],inplace = True )
print(df)

"""
To rename 'fname' to 'first_name'
"""

df.rename(columns = {'fname': 'first_name'},inplace = True )
print(df)

"""
To print the contents of the dataframe df
"""

print(df)

"""
To print the contents of the dataframe df
"""

print(df)