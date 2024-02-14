# -*- coding: utf-8 -*-

"""
Name of developer: Najman
Name of program: handle_big_csv_file.py
Description: 2. Write program in Python to handle a huge csv file
    
Date Created:       Thu, 15 July 2023
Date last update:   Thu, 15 July 2023
"""

import pandas as pd

csv_file = 'C:\\Users\\evoma\\anaconda\\Scripts\\RESPONDENTS.csv'
df = pd.read_csv(csv_file,nrows=1000, skiprows=5000)
print(df)

# define and initialise the integer variable vcounter
vcounter = 0

# split this huge csv file into n number of small files (chunk files)

result = pd.Series([], dtype='float64')
for chunk in pd.read_csv(csv_file, chunksize = 5000):
    chunk.columns = ['age', 'participants']
    result = pd.concat([result, chunk.age, chunk.participants])
    vcounter += 1
    if vcounter == 20:
        break
    print(result)
    print('The total number of chunk files created', vcounter)


