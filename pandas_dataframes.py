# -*- coding: utf-8 -*-
"""
Created on Sunday Aug 20 2023

@author: Anjali
"""

#Pandas is a Python library used for working with data sets.
#It has functions for analyzing, cleaning, exploring, and manipulating data.
#Pandas allows us to analyze big data and make conclusions based on statistical theories.
#Pandas can clean messy data sets, and make them readable and relevant.
#Relevant data is very important in data science.


# Create Dataframe : Using Python Dict
import pandas as pd
my_data = {
    'Name': ['Alexa', 'Bixby', 'Cortana', 'Jarvis', 'Lyra', 'Robin', 'Siri'], 
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'], 
    'Education': ['Postgraduate', 'Graduate', 'Postgraduate', 'Doctorate', 'Graduate', 'Graduate', 'Postgraduate'], 
    'Age': [24, 21, 25, 28, 23, 22, 24], 
    'Monthly_Salary': [27000, 25000, 30000, 35000, 26000, 24000, 28000]
    }

my_df = pd.DataFrame(my_data) #creating dataframe
print(my_df)
my_df.to_csv('info.csv') #creating csv file
df = pd.read_csv('mtcars.csv') #Reading csv file from current working directory
print(df)
#Reshape Dataframe 
print(df.columns)
print(df.index)

#A Series only has one data column, whereas a single-column DataFrame contains
#both a data column and an index. The labels for the data are contained in the
#index, which is a second column.

print(my_df.sort_values('Age')) #Sorted the age of dict which we created at strating
#by default Ascending order

#print(my_df.sort_values(['Age', 'Monthly_Salary'], ascending=[True, False])) #doubt

#Subset Dataframe
print(my_df['Name']) # Extract Data of Specific Column as Series
print(my_df[['Name']]) # # Extract Data of Specific Column as Dataframe
print(my_df[['Name', 'Age']]) # Extract Data of Multiple Columns as Dataframe
x=my_df[['Name', 'Age']] #here I took 2 column and storedit in a variable named x 
print(x.sort_values('Age'))#Used sort function to sort the age


print(my_df.iloc[1]) # iloc[Row_Num, Col_Num] : Extract Data by Specific {Row or Column or Both} Number as Series
print(my_df.loc[1:4])## rows at index location between 1 and 4 (inclusive)
print(my_df.iloc[1:4])## rows at index location between 0 and 4 (exclusive)
kk = my_df.loc[0, 'Age'] # loc[row_name, col_name] : Extract Data by Specific {Row or Column or Both} Name as Value (String or Number)
print(kk)

#Filter Dataframe
print(my_df[my_df['Gender'] == 'Female']) # Filter Data with Single Criteria
print(my_df[(my_df['Age'] < 25) & (my_df['Education'] == 'Graduate')]) # Filter Data with Multiple Criteria 

# Combine Dataframe : Concat, Merge
my_df_f = my_df[my_df['Gender'] == 'Female']; my_df_f
my_df_m = my_df[my_df['Gender'] != 'Female']; my_df_m

# Concatenate Dataframe 
my_df_fm = pd.concat([my_df_f, my_df_m], ignore_index=True)
print(my_df_fm)

#The ignore_index parameter enables you to control the index of the new output 
#Pandas object.By default, this is set to ignore_index = False . In this case,
#Pandas keeps the original index values from the two different input dataframes.
#Keep in mind that this can cause duplicate index values which can cause problems.

#Pandas Application : Data Description

print(my_df.head(5)) #Display 1st 5 Rows
print(my_df.tail(5)) #Display last 5 Rows
print(my_df.shape) ## Display Dataframe Dimension : Number of Rows & Columns
