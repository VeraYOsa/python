# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:38:17 2021

@author: inesr
"""

#Importing libraries

import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
# import numpy as np

#Variables set up
input_folder = (r'C:\Users\inesr\OneDrive\Documentos\Gapminder_data_project\\')
# input_files = glob.glob(os.path.join(input_folder, "*.csv"))
# extension = 'csv'
os.chdir(input_folder)
input_files = glob.glob('*.csv')
output_folder = (r'C:\Users\inesr\OneDrive\Documentos\Gapminder_data_project\output\\')
output_file = 'gapminder_data.csv'


#%% IMPORT FILES
#Import the file and use the second row as headers

df = pd.DataFrame()
df = pd.read_csv(input_folder+"empires.csv", encoding= 'unicode_escape', skiprows=1)

#Rename columns so they are easy to manipulate

#Apply function to a loop for all the columns in the dataframe
lenght = len(df.columns)

for i in range(lenght):
    df.iloc[:,i]= df.iloc[:,i].apply(lambda x: x.split('[')[0])
    df.iloc[:,i]

df = df.join(df['Year'].str.split('B', expand=True).add_prefix('Year').fillna(0))


#%% Export data to csv
  
# saving the csv
df.to_csv(output_folder + "empire_export.csv")



        
#%% plotting
 
# x axis values
x = df.iloc[:,0]
# corresponding y axis values
y = df.iloc[:,2]
 
# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, markerfacecolor='blue', markersize=2) 
# setting x and y axis range
plt.ylim(1,8)
plt.xlim(1,8)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('My first plot in python')
 
# function to show the plot
plt.show()
