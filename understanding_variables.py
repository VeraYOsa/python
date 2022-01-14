# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 17:17:11 2022

@author: inesr
"""

import pandas as pd
from scipy import stats
import os
import glob
import matplotlib.pyplot as plt

#Variables set up
input_folder = (r'C:\Users\inesr\OneDrive\Documentos\Gapminder_data_project\\')
# input_files = glob.glob(os.path.join(input_folder, "*.csv"))
# extension = 'csv'
os.chdir(input_folder)
input_files = glob.glob('*.csv')
output_folder = (r'C:\Users\inesr\OneDrive\Documentos\Gapminder_data_project\output\\')
output_file = 'gapminder_data.csv'

df = pd.DataFrame()
for i in input_files:
    df[i] = pd.read_csv(input_folder+i).melt(id_vars=['country'], 
                                             var_name='year', value_name=i).set_index(['country', 'year']).dropna()
df = df.rename(columns = lambda x : str(x)[:-4])  # remove the ".csv" from the column name
df = df.fillna(0)           #using pandas


#%%
#Convert k, m, b to units
#Define function to remove the symbols and multiply to obtain units
 
def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x*1
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'k' in x:
        if len(x) > 1:
            return float(x.replace('k', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'm' in x:
        if len(x) > 1:
            return float(x.replace('m', '')) * 1000000
        return 1000000.0
    if 'TR' in x:
        if len(x) > 1:
            return float(x.replace('TR', '')) * 1000000000000
        return 1000000000.0
    if 'B' in x:
        if len(x) > 1:
            return float(x.replace('B', '')) * 1000000000
        return 1000000.0
    if 'b' in x:
        if len(x) > 1:
            return float(x.replace('b', '')) * 1000000000
        return 1000000.0
    # if 'B' in x:
    #     return float(x.replace('B', '')) * 1000000000
    # return 0.0
    # if 'b' in x:
    #     return float(x.replace('b', '')) * 1000000000
    return x

#Apply function to a loop for all the columns in the dataframe
lenght = len(df.columns)

for i in range(lenght):
    df.iloc[:,i]= df.iloc[:,i].apply(value_to_float)
    df.iloc[:,i]


df = df.reset_index(level=['country', 'year'])
df = df[(df['year'] == '1980')]

#%% histogram

n, bins, patches = plt.hist(x=df['child_mortality_0_5_year_olds_dying_per_1000_born'], bins='auto', alpha=0.7,rwidth=0.85)
df.dtypes
df.isnull().mean()  #gives you the % of missing values from each column
df.describe()
