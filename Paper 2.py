#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Task 1
#Solve for x, y & z where:
#Eq1 : x + y + z = 2 | Eq2 : 6x - 4y + 5z = 31 | Eq3: 5x + 2y + 2z = 13

#Solution:

import numpy as np
from numpy import linalg as npla

# Coefficients of the equations
coefficients = np.array([[1, 1, 1], [6, -4, 5], [5, 2, 2]])
constants = np.array([2, 31, 13])

# Solve the system of equations
solution = npla.linalg.solve(coefficients, constants)

x, y, z = solution
print("Solution using NumPy:")
print("x =", x)
print("y =", y)
print("z =", z)


# In[18]:


#task 2 2. Create & Update Dictionary
2.1. Create a Employee Dictionary 'emp_dict' with following Information:
Name Education Gender
ABC Graduate Male
DEF Postgraduate Female
GHI Postgraduate Male
JKL Graduate Other
MNO Graduate Female
PQR Postgraduate Female
STU Graduate Male
#Solution: 2.1

emp_dict={'Name':['ABC','DEF','GHI','JKL','MNO','PQR','STU'],
          'Education':['Graduate','Postgraduate','Postgraduate','Graduate','Graduate','Postgraduate','Graduate'],
          'Gender':['Make','Female','Male','Other','Female','Female','Male']

}
emp_dict



# In[20]:


#Task 2.2
# 2.2. Update the Employee Dictionary 'emp_dict' with following Information: [05 marks]
# Age
# 22
# 27
# 26
# 23
# 24
# 30
# 21

#Update the Employee Dictionary 'emp_dict' with following Information:

emp_dict['Age']= 22,27,26,23,24,30,21 #added age as a key and different age as a value
emp_dict


# In[1]:


# #Question-3.1 & #3.2 
# 3. Create & Update Dataframe
# 3.1. Create a Dataframe 'emp_df' from the Dictionary 'emp_dict' [05 marks]
# 3.2. Update the Dataframe 'emp_df' with the following Information: [05 marks]
# Salary_Lakhs Bonus%
# 6 12.50
# 15 8.75
# 20 6.25
# 5 10.20
# 10 13.60
# 18 11.40
# 12 9.80
import pandas as pd

# 3.1 Create the DataFrame from the provided dictionary
emp_dict = {
    "Name": ["ABC", "DEF", "GHI", "JKL"],
    "Education": ["Graduate", "Postgraduate", "Graduate", "Postgraduate"],
    "Gender": ["Male", "Female", "Male", "Female"],
    "Age": [25, 30, 28, 22]
}

emp_df = pd.DataFrame(emp_dict)

# 3.2 Update the DataFrame with Salary_Lakhs and Bonus% information
salary_bonus_data = {
    "Salary_Lakhs": [6, 15, 20, 5, 10, 18, 12],
    "Bonus%": [12.50, 8.75, 6.25, 10.20, 13.60, 11.40, 9.80]
}

salary_bonus_df = pd.DataFrame(salary_bonus_data)

emp_df = pd.concat([emp_df, salary_bonus_df], axis=1)

# 3.3 Update the DataFrame with additional information
additional_info = {
    "Name": ["VWX", "YZA", "BCD"],
    "Education": ["Postgraduate", "Graduate", "Postgraduate"],
    "Gender": ["Male", "Female", "Other"],
    "Age": [35, 28, 32],
    "Salary_Lakhs": [14, 7, 8],
    "Bonus%": [5.50, 7.75, 14.80]
}

additional_info_df = pd.DataFrame(additional_info)

emp_df = pd.concat([emp_df, additional_info_df])

# 3.4 
# 3.4. Create a Column ‘Gross_Salary_Lakhs’ with the following information: [05 marks]
# Gross_Salary_Lakhs = Salary_Lakhs * (1 + Bonus%)


# Create the 'Gross_Salary_Lakhs' column
emp_df["Gross_Salary_Lakhs"] = emp_df["Salary_Lakhs"] * (1 + emp_df["Bonus%"] / 100)

# Display the updated DataFrame
print(emp_df)


# In[13]:


#Task 3
#3.1-
import pandas as pd

# Provided emp_dict dictionary
emp_dict = {
    'Name': ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU'],
    'Education': ['Graduate', 'Postgraduate', 'Postgraduate', 'Graduate', 'Graduate', 'Postgraduate', 'Graduate'],
    'Gender': ['Make', 'Female', 'Male', 'Other', 'Female', 'Female', 'Male']
}

# Convert emp_dict into a DataFrame
emp_df = pd.DataFrame(emp_dict)

# Print the resulting DataFrame
print(emp_df)





# In[16]:


# Task 3.2
# Provided emp_dict dictionary
emp_dict = {
    'Name': ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU'],
    'Education': ['Graduate', 'Postgraduate', 'Postgraduate', 'Graduate', 'Graduate', 'Postgraduate', 'Graduate'],
    'Gender': ['Make', 'Female', 'Male', 'Other', 'Female', 'Female', 'Male']
}

# Convert emp_dict into a DataFrame
emp_df = pd.DataFrame(emp_dict)

# Add salary and bonus information to the DataFrame
salary_bonus_data = [
    {'Salary_Lakhs': 6, 'Bonus%': 12.5},
    {'Salary_Lakhs': 15, 'Bonus%': 8.75},
    {'Salary_Lakhs': 20, 'Bonus%': 6.25},
    {'Salary_Lakhs': 5, 'Bonus%': 10.2},
    {'Salary_Lakhs': 10, 'Bonus%': 13.6},
    {'Salary_Lakhs': 18, 'Bonus%': 11.4},
    {'Salary_Lakhs': 12, 'Bonus%': 9.8}
]
emp_df


# In[22]:


#Task 3.3
# Provided emp_dict dictionary
emp_dict = {
    'Name': ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU'],
    'Education': ['Graduate', 'Postgraduate', 'Postgraduate', 'Graduate', 'Graduate', 'Postgraduate', 'Graduate'],
    'Gender': ['Make', 'Female', 'Male', 'Other', 'Female', 'Female', 'Male']
}

# Convert emp_dict into a DataFrame
emp_df = pd.DataFrame(emp_dict)

# Add salary and bonus information to the DataFrame
salary_bonus_data = [
    {'Salary_Lakhs': 6, 'Bonus%': 12.5},
    {'Salary_Lakhs': 15, 'Bonus%': 8.75},
    {'Salary_Lakhs': 20, 'Bonus%': 6.25},
    {'Salary_Lakhs': 5, 'Bonus%': 10.2},
    {'Salary_Lakhs': 10, 'Bonus%': 13.6},
    {'Salary_Lakhs': 18, 'Bonus%': 11.4},
    {'Salary_Lakhs': 12, 'Bonus%': 9.8}
]
# Convert the salary and bonus data into a DataFrame
salary_bonus_df = pd.DataFrame(salary_bonus_data)

# Update emp_df with salary and bonus information
emp_df['Salary_Lakhs'] = salary_bonus_df['Salary_Lakhs']
emp_df['Bonus%'] = salary_bonus_df['Bonus%']

# Additional information to be added
additional_data = [
    {'Name': 'VWX', 'Education': 'Postgraduate', 'Gender': 'Male', 'Age': 35, 'Salary_Lakhs': 14, 'Bonus%': 5.5},
    {'Name': 'YZA', 'Education': 'Graduate', 'Gender': 'Female', 'Age': 28, 'Salary_Lakhs': 7, 'Bonus%': 7.75},
    {'Name': 'BCD', 'Education': 'Postgraduate', 'Gender': 'Other', 'Age': 32, 'Salary_Lakhs': 8, 'Bonus%': 14.8}
]

# Convert the additional data into a DataFrame
additional_df = pd.DataFrame(additional_data)

# Concatenate emp_df and additional_df to update the DataFrame
emp_df = pd.concat([emp_df, additional_df], ignore_index=True)

# Print the updated DataFrame
print(emp_df)


# In[23]:


#Task 3.4

import pandas as pd

# Provided emp_dict dictionary
emp_dict = {
    'Name': ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU'],
    'Education': ['Graduate', 'Postgraduate', 'Postgraduate', 'Graduate', 'Graduate', 'Postgraduate', 'Graduate'],
    'Gender': ['Make', 'Female', 'Male', 'Other', 'Female', 'Female', 'Male']
}

# Convert emp_dict into a DataFrame
emp_df = pd.DataFrame(emp_dict)

# Add salary and bonus information to the DataFrame
salary_bonus_data = [
    {'Salary_Lakhs': 6, 'Bonus%': 12.5},
    {'Salary_Lakhs': 15, 'Bonus%': 8.75},
    {'Salary_Lakhs': 20, 'Bonus%': 6.25},
    {'Salary_Lakhs': 5, 'Bonus%': 10.2},
    {'Salary_Lakhs': 10, 'Bonus%': 13.6},
    {'Salary_Lakhs': 18, 'Bonus%': 11.4},
    {'Salary_Lakhs': 12, 'Bonus%': 9.8}
]

# Convert the salary and bonus data into a DataFrame
salary_bonus_df = pd.DataFrame(salary_bonus_data)

# Update emp_df with salary and bonus information
emp_df['Salary_Lakhs'] = salary_bonus_df['Salary_Lakhs']
emp_df['Bonus%'] = salary_bonus_df['Bonus%']

# Additional information to be added
additional_data = [
    {'Name': 'VWX', 'Education': 'Postgraduate', 'Gender': 'Male', 'Age': 35, 'Salary_Lakhs': 14, 'Bonus%': 5.5},
    {'Name': 'YZA', 'Education': 'Graduate', 'Gender': 'Female', 'Age': 28, 'Salary_Lakhs': 7, 'Bonus%': 7.75},
    {'Name': 'BCD', 'Education': 'Postgraduate', 'Gender': 'Other', 'Age': 32, 'Salary_Lakhs': 8, 'Bonus%': 14.8}
]

# Convert the additional data into a DataFrame
additional_df = pd.DataFrame(additional_data)

# Concatenate emp_df and additional_df to update the DataFrame
emp_df = pd.concat([emp_df, additional_df], ignore_index=True)

# Calculate the 'Gross_Salary_Lakhs' column
emp_df['Gross_Salary_Lakhs'] = emp_df['Salary_Lakhs'] * (1 + emp_df['Bonus%'] / 100)

# Print the updated DataFrame
print(emp_df)


# In[24]:


#Task 4.1 - Subset Dataframes
# 4.1. Create a Subset ‘emp_df_ss’ from ‘emp_df’ with the following Variables: {Name, Age,
# Gross_Salary_Lakhs}


import pandas as pd

# Define the employee data as a list of dictionaries
employee_data = [
    {'Name': 'ABC', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 22},
    {'Name': 'DEF', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 27},
    {'Name': 'GHI', 'Education': 'Postgraduate', 'Gender': 'Male', 'Age': 26},
    {'Name': 'JKL', 'Education': 'Graduate', 'Gender': 'Other', 'Age': 23},
    {'Name': 'MNO', 'Education': 'Graduate', 'Gender': 'Female', 'Age': 24},
    {'Name': 'PQR', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 30},
    {'Name': 'STU', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 21}
]

# Create the DataFrame using the existing employee data
emp_df = pd.DataFrame(employee_data)

# Add the 'Salary_Lakhs' and 'Bonus%' columns
emp_df['Salary_Lakhs'] = [6, 15, 20, 5, 10, 18, 12]
emp_df['Bonus%'] = [12.50, 8.75, 6.25, 10.20, 13.60, 11.40, 9.80]

# Calculate 'Gross_Salary_Lakhs' based on the formula
emp_df['Gross_Salary_Lakhs'] = emp_df['Salary_Lakhs'] * (1 + emp_df['Bonus%'] / 100)

# Specify the variables for the subset
subset_variables = ['Name', 'Age', 'Gross_Salary_Lakhs']

# Create the subset 'emp_df_ss'
emp_df_ss = emp_df[subset_variables]

# Print the resulting emp_df_ss
print(emp_df_ss)



# In[25]:


#Task 5.1 - Sort Dataframes
# 1. Create a Copy of 'emp_df' Named as 'emp_df_age_sorted' and Sort {Highest to Lowest}
# by 'Age' [05 marks]

import pandas as pd

# Define the employee data as a list of dictionaries
employee_data = [
    {'Name': 'ABC', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 22},
    {'Name': 'DEF', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 27},
    {'Name': 'GHI', 'Education': 'Postgraduate', 'Gender': 'Male', 'Age': 26},
    {'Name': 'JKL', 'Education': 'Graduate', 'Gender': 'Other', 'Age': 23},
    {'Name': 'MNO', 'Education': 'Graduate', 'Gender': 'Female', 'Age': 24},
    {'Name': 'PQR', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 30},
    {'Name': 'STU', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 21}
]

# Create the DataFrame using the existing employee data
emp_df = pd.DataFrame(employee_data)

# Add the 'Salary_Lakhs' and 'Bonus%' columns
emp_df['Salary_Lakhs'] = [6, 15, 20, 5, 10, 18, 12]
emp_df['Bonus%'] = [12.50, 8.75, 6.25, 10.20, 13.60, 11.40, 9.80]

# Calculate 'Gross_Salary_Lakhs' based on the formula
emp_df['Gross_Salary_Lakhs'] = emp_df['Salary_Lakhs'] * (1 + emp_df['Bonus%'] / 100)

# Specify the sorting column and order (highest to lowest)
sort_column = 'Age'
sort_order = False  # False indicates descending order

# Create the sorted DataFrame 'emp_df_age_sorted'
emp_df_age_sorted = emp_df.sort_values(by=sort_column, ascending=sort_order).copy()

# Print the resulting emp_df_age_sorted
print(emp_df_age_sorted)


# In[26]:


#Task 5.2 - Sort Dataframes
# 5.2. Create a Copy of 'emp_df' Named as 'emp_df_age_salary_sorted' and Sort: First by 'Age'
# {Lowest to Highest}, Second by 'Gross_Salary_Lakhs' {Highest to Lowest} 


import pandas as pd

# Define the employee data as a list of dictionaries
employee_data = [
    {'Name': 'ABC', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 22},
    {'Name': 'DEF', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 27},
    {'Name': 'GHI', 'Education': 'Postgraduate', 'Gender': 'Male', 'Age': 26},
    {'Name': 'JKL', 'Education': 'Graduate', 'Gender': 'Other', 'Age': 23},
    {'Name': 'MNO', 'Education': 'Graduate', 'Gender': 'Female', 'Age': 24},
    {'Name': 'PQR', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 30},
    {'Name': 'STU', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 21}
]

# Create the DataFrame using the existing employee data
emp_df = pd.DataFrame(employee_data)

# Add the 'Salary_Lakhs' and 'Bonus%' columns
emp_df['Salary_Lakhs'] = [6, 15, 20, 5, 10, 18, 12]
emp_df['Bonus%'] = [12.50, 8.75, 6.25, 10.20, 13.60, 11.40, 9.80]

# Calculate 'Gross_Salary_Lakhs' based on the formula
emp_df['Gross_Salary_Lakhs'] = emp_df['Salary_Lakhs'] * (1 + emp_df['Bonus%'] / 100)

# Specify the sorting columns and orders
sort_columns = ['Age', 'Gross_Salary_Lakhs']
sort_orders = [True, False]  # True for ascending, False for descending

# Create the sorted DataFrame 'emp_df_age_salary_sorted'
emp_df_age_salary_sorted = emp_df.sort_values(by=sort_columns, ascending=sort_orders).copy()

# Print the resulting emp_df_age_salary_sorted
print(emp_df_age_salary_sorted)


# In[2]:


# Task 6.1 - Filter Dataframe
# Create a Dataframe ‘emp_df_filtered’ to Filter ‘emp_df’ using the following Information:
# 'Age' >= 25 & 'Gender' = 'Female'


import pandas as pd

# Define the employee data as a list of dictionaries
employee_data = [
    {'Name': 'ABC', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 22},
    {'Name': 'DEF', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 27},
    {'Name': 'GHI', 'Education': 'Postgraduate', 'Gender': 'Male', 'Age': 26},
    {'Name': 'JKL', 'Education': 'Graduate', 'Gender': 'Other', 'Age': 23},
    {'Name': 'MNO', 'Education': 'Graduate', 'Gender': 'Female', 'Age': 24},
    {'Name': 'PQR', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 30},
    {'Name': 'STU', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 21}
]

# Create the DataFrame using the existing employee data
emp_df = pd.DataFrame(employee_data)

# Add the 'Salary_Lakhs' and 'Bonus%' columns
emp_df['Salary_Lakhs'] = [6, 15, 20, 5, 10, 18, 12]
emp_df['Bonus%'] = [12.50, 8.75, 6.25, 10.20, 13.60, 11.40, 9.80]

# Calculate 'Gross_Salary_Lakhs' based on the formula
emp_df['Gross_Salary_Lakhs'] = emp_df['Salary_Lakhs'] * (1 + emp_df['Bonus%'] / 100)

# Define the filter conditions
age_condition = emp_df['Age'] >= 25
gender_condition = emp_df['Gender'] == 'Female'

# Apply the filter conditions to create 'emp_df_filtered'
emp_df_filtered = emp_df[age_condition & gender_condition]

# Print the resulting emp_df_filtered
print(emp_df_filtered)


# In[28]:


#Task 6.2 - Filter Dataframe
# Create 2 Subsets: ‘emp_df_grad’ & ‘emp_df_postgrad’ from ‘emp_df’ containing
# Information of Employees having ‘Education’ as ‘Graduate’ & ‘Postgraduate’, respectively

import pandas as pd

# Define the employee data as a list of dictionaries
employee_data = [
    {'Name': 'ABC', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 22},
    {'Name': 'DEF', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 27},
    {'Name': 'GHI', 'Education': 'Postgraduate', 'Gender': 'Male', 'Age': 26},
    {'Name': 'JKL', 'Education': 'Graduate', 'Gender': 'Other', 'Age': 23},
    {'Name': 'MNO', 'Education': 'Graduate', 'Gender': 'Female', 'Age': 24},
    {'Name': 'PQR', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 30},
    {'Name': 'STU', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 21}
]

# Create the DataFrame using the existing employee data
emp_df = pd.DataFrame(employee_data)

# Add the 'Salary_Lakhs' and 'Bonus%' columns
emp_df['Salary_Lakhs'] = [6, 15, 20, 5, 10, 18, 12]
emp_df['Bonus%'] = [12.50, 8.75, 6.25, 10.20, 13.60, 11.40, 9.80]

# Calculate 'Gross_Salary_Lakhs' based on the formula
emp_df['Gross_Salary_Lakhs'] = emp_df['Salary_Lakhs'] * (1 + emp_df['Bonus%'] / 100)

# Define the filter conditions for 'Education'
graduate_condition = emp_df['Education'] == 'Graduate'
postgraduate_condition = emp_df['Education'] == 'Postgraduate'

# Create the subsets 'emp_df_grad' and 'emp_df_postgrad' based on the filter conditions
emp_df_grad = emp_df[graduate_condition].copy()
emp_df_postgrad = emp_df[postgraduate_condition].copy()

# Print the resulting subsets
print("Graduate Employees:")
print(emp_df_grad)

print("\nPostgraduate Employees:")
print(emp_df_postgrad)



# In[29]:


#TASK 7 - Merge Dataframe
# Create a Dataframe ‘emp_df_merged’ to Inner Merge ‘emp_df_grad’ having only following
# Variables {Name, Gender, Age} with ‘emp_df_postgrad’ having only following Variables
# {Name, Gender, Gross_Salary_Lakhs} on ‘Gender’

import pandas as pd

# Define the employee data for 'emp_df_grad' and 'emp_df_postgrad' as lists of dictionaries
data_grad = [
    {'Name': 'ABC', 'Gender': 'Male', 'Age': 22},
    {'Name': 'JKL', 'Gender': 'Other', 'Age': 23},
    {'Name': 'MNO', 'Gender': 'Female', 'Age': 24},
    {'Name': 'STU', 'Gender': 'Male', 'Age': 21}
]

data_postgrad = [
    {'Name': 'DEF', 'Gender': 'Female', 'Gross_Salary_Lakhs': 15.0},
    {'Name': 'GHI', 'Gender': 'Male', 'Gross_Salary_Lakhs': 20.0},
    {'Name': 'PQR', 'Gender': 'Female', 'Gross_Salary_Lakhs': 18.0}
]

# Create 'emp_df_grad' and 'emp_df_postgrad' DataFrames using the provided data
emp_df_grad = pd.DataFrame(data_grad)
emp_df_postgrad = pd.DataFrame(data_postgrad)

# Perform an inner merge on 'Gender' to create 'emp_df_merged'
emp_df_merged = pd.merge(emp_df_grad[['Name', 'Gender', 'Age']], emp_df_postgrad[['Name', 'Gender', 'Gross_Salary_Lakhs']], on='Gender', how='inner')

# Print the resulting emp_df_merged
print(emp_df_merged)


# In[30]:


#Task 8.1 - Group Dataframe
# 8. Group Dataframe
# 8.1. Group ‘emp_df’ to Create a Table ‘emp_df_gen_edu’ using ‘Gender’ & ‘Education’ having
# Count of Employees


import pandas as pd

# Define the employee data as a list of dictionaries
employee_data = [
    {'Name': 'ABC', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 22},
    {'Name': 'DEF', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 27},
    {'Name': 'GHI', 'Education': 'Postgraduate', 'Gender': 'Male', 'Age': 26},
    {'Name': 'JKL', 'Education': 'Graduate', 'Gender': 'Other', 'Age': 23},
    {'Name': 'MNO', 'Education': 'Graduate', 'Gender': 'Female', 'Age': 24},
    {'Name': 'PQR', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 30},
    {'Name': 'STU', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 21}
]

# Create the DataFrame using the existing employee data
emp_df = pd.DataFrame(employee_data)

# Add the 'Salary_Lakhs' and 'Bonus%' columns
emp_df['Salary_Lakhs'] = [6, 15, 20, 5, 10, 18, 12]
emp_df['Bonus%'] = [12.50, 8.75, 6.25, 10.20, 13.60, 11.40, 9.80]

# Calculate 'Gross_Salary_Lakhs' based on the formula
emp_df['Gross_Salary_Lakhs'] = emp_df['Salary_Lakhs'] * (1 + emp_df['Bonus%'] / 100)

# Group 'emp_df' by 'Gender' and 'Education' and count employees in each group
emp_df_gen_edu = emp_df.groupby(['Gender', 'Education']).size().reset_index(name='Count')

# Print the resulting emp_df_gen_edu
print(emp_df_gen_edu)


# In[31]:


#Task 8.2 - Group Dataframe
# 8.2. Group ‘emp_df’ to Create a Table ‘emp_df_gen_age_sal’ using ‘Gender’ with Average of
# Variables {Age & Gross_Salary_Lakhs}

import pandas as pd

# Define the employee data as a list of dictionaries
employee_data = [
    {'Name': 'ABC', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 22, 'Gross_Salary_Lakhs': 6.75},
    {'Name': 'DEF', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 27, 'Gross_Salary_Lakhs': 15.25},
    {'Name': 'GHI', 'Education': 'Postgraduate', 'Gender': 'Male', 'Age': 26, 'Gross_Salary_Lakhs': 20.5},
    {'Name': 'JKL', 'Education': 'Graduate', 'Gender': 'Other', 'Age': 23, 'Gross_Salary_Lakhs': 6.50},
    {'Name': 'MNO', 'Education': 'Graduate', 'Gender': 'Female', 'Age': 24, 'Gross_Salary_Lakhs': 10.30},
    {'Name': 'PQR', 'Education': 'Postgraduate', 'Gender': 'Female', 'Age': 30, 'Gross_Salary_Lakhs': 20.70},
    {'Name': 'STU', 'Education': 'Graduate', 'Gender': 'Male', 'Age': 21, 'Gross_Salary_Lakhs': 12.60}
]

# Create the DataFrame using the existing employee data
emp_df = pd.DataFrame(employee_data)

# Group 'emp_df' by 'Gender' and calculate the average of 'Age' and 'Gross_Salary_Lakhs' for each group
emp_df_gen_age_sal = emp_df.groupby('Gender').agg({'Age': 'mean', 'Gross_Salary_Lakhs': 'mean'}).reset_index()

# Rename the columns for clarity
emp_df_gen_age_sal = emp_df_gen_age_sal.rename(columns={'Age': 'Average_Age', 'Gross_Salary_Lakhs': 'Average_Gross_Salary_Lakhs'})

# Print the resulting emp_df_gen_age_sal
print(emp_df_gen_age_sal)


# In[32]:


#Task 9 - Panel Dataframe from Cross-Sectional Dataframe
# 9. Create Panel Dataframe from Cross-Sectional Dataframe
# 9.1. From the following Cross-Sectional Dataframe 'df_cross_section': [05 marks]
# Company 2023 2024
# ZYX 123 321
# WVU 456 654
# TSR 789 987
# Create the following Panel Dataframe 'df_panel':
# Company Year Profit
# TSR 2023 789
# TSR 2024 987
# WVU 2023 456
# WVU 2024 654
# ZYX 2023 123
# ZYX 2024 321

import pandas as pd

# Create the cross-sectional DataFrame 'df_cross_section'
data = {
    'Company': ['ZYX', 'WVU', 'TSR'],
    2023: [123, 456, 789],
    2024: [321, 654, 987]
}

df_cross_section = pd.DataFrame(data)

# Convert the cross-sectional DataFrame to a panel DataFrame 'df_panel'
df_panel = df_cross_section.melt(id_vars='Company', var_name='Year', value_name='Profit')

# Print the resulting df_panel
print(df_panel)

