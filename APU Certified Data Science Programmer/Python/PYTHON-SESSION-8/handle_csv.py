"""

Name of developer: Mod Man
Name of program: handle_csv.py
Date first write: 27/06/2023
Date last update: 27/06/2023

"""

# Import/Load the Pandas library
import pandas as pd
csv_file = 'C:\\Users\\evoma\\Desktop\\Data Eng,Snc\\ACDSP\\PYTHON-SESSION-8\\PYTHON-SESSION-8HEALTH_CARE_DS.csv'

"""
To find the data type of the csv file
"""

print(type(csv_file))

"""
To load the data from the csv file into a DataFrame df
"""

df = pd.read_csv(csv_file)
pd.set_option('display.max_columns',4)
pd.set_option('display.max_rows',12)

print(df)

"""
Rename 'id' column to 'ID'
"""

df.rename(columns = {'id': 'ID'},inplace = True)
print(df)

"""
Print the mean, median, std
"""

print(df['age'].mean())
print(df['age'].median())
print(df['age'].std())