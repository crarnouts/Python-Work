# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:14:48 2019

@author: arnou
"""

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd


# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names,'drives_right':dr,'cars_per_cap':cpc}


my_dict2 = {'country':names,'drives_right':dr,'cars_per_cap':cpc}


# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

cars2 =pd.DataFrame(my_dict)
# Print cars
print(cars)

cars = cars.append(cars2, ignore_index = True)

print(cars)



df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AC'))
df

df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df.append(df2)

df.append(df2, ignore_index=True)


############### Add rows to an empty dataframe ###########################

import datetime as dt

df = pd.DataFrame(columns=['A', 'B'])

df2 = pd.DataFrame([[dt.datetime.now(), 6], [dt.datetime.now(), 8]], columns=list('AB'))
df = df.append(df2)

df

s1 = pd.Series([5, 6, 7])
s2 = pd.Series([7, 8, 9])

df = pd.DataFrame([list(s1), list(s2)],  columns =  ["A", "B", "C"])

df.loc[-1] = [2, 3, 4]  # adding a row
df.index = df.index + 1  # shifting index
df = df.sort_index()  # sorting by index


total_rows = len(df.index)






