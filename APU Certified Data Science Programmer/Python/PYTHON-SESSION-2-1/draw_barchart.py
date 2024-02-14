# -*- coding: utf-8 -*-
"""
Name of developer: Najman
Name of program: draw_barchart.py
Description: 1. Write a program in python to draw bar chart
    
Date Created:       Thu, 22 June 2023
Date last update:   Thu, 22 June 2023
"""

import numpy as np # import nympy library/module
import pandas as pd # import panda library/module
from matplotlib import pyplot as plt # import matplotlib library/module

age = 50
price = 5.3
csv_path = 'C:\\Users\\evoma\\anaconda\\Scripts\\DEVELOPER.csv'
df = pd.read_csv(csv_path)

# read the contents and transfer to df (x-axis)
print(type(df))
plt.style.use('fivethirtyeight')
ages_x = df['age']
x_indexes = np.arange(len(ages_x))

# specify the bar width size
width = 0.25

python_dev = df['python_dev']
java_dev = df['java_dev']
cpplus_dev = df['cpplus_dev']

# label the axis and title
plt.title('Ages vs Developers yearly salary in USD')
plt.xlabel('Age')
plt.ylabel('Developers')

# plot
plt.bar(ages_x - width, python_dev, width, color='#444444', label = 'Python Developers')
plt.bar(ages_x, java_dev, width, color='#0000FF', label = 'Java Developers')
plt.bar(ages_x + width, cpplus_dev, width, color='#FF0000', label = 'C++ Developers')

# legends and x-axis label
plt.legend()
plt.xticks(ticks = ages_x, label = ages_x)


