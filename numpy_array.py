# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 2023

@author: Anjali
"""

#NumPy is a Python library used for working with arrays.

#It also has functions for working in domain of linear algebra, 
#fourier transform, and matrices.

#NumPy stands for Numerical Python.

import numpy as np
from numpy import linalg as npla

# 1-Dimensional Array
A = np.array([1, 2, 3, 4])
print(type(A))
print(A.shape) #(4,) 1 is default thats why it is showing blank 

# 2-Dimensional Array
A1 = np.array([[11, 12, 13], [21, 22, 23]])
print(type(A1))
print(A1.shape) #(2, 3)

# 3-Dimensional Array
A2 = np.array([[[11, 12, 13], [21, 22, 23]], [[31, 32, 33], [41, 42, 44]]]); A2 
print(type(A2))
print(A2.shape) # Dimension = 2 Layers, 2 Rows, 3 Columns

#Arrays : Manipulation

print(A[2]) # 1-d Array Indexing
print(A.reshape(2, 2)) #1-d Array Reshape
print(A.reshape(3,2,1)) #2-d Array->3-d Array Reshape
print(A.reshape(2,2,3)) # 3-d Array Reshape >> {2 Layers, 3 Rows, 2 Columns}
print(A.reshape(4,3)) #3-d --> 2-d Array

#Array Transpose

print(A.T)
print(A1.T)
print(A2.T)

#Arrays : Concatenation

a11 = np.array([[1, 2], [3, 4]])
a12 = np.array([[5, 6]])

a11_12 = np.concatenate((a11, a12), axis=None)
print('Concatenation of a11 and a12\n',a11_12)
a11_12_row = np.concatenate((a11, a12), axis=0)
print('Row-wise Array Concatenation of a11 and a12\n',a11_12_row)
a11_12_column = np.concatenate((a11.T, a12.T), axis=1)
print('Column-wise Concatenation of a11 and a12\n',a11_12_column)
 

#Arrays : Statistics
a4 = np.array([1, 23, 4])
a5 = np.array([56, 7, 8])

# Concatenate & Reshape
a45 = np.concatenate((a4, a5)).reshape(2,3)
print(a45)

# Array Min
print("Mininum in both array\n",np.amin(a45)) 
print("Column minimum\n",np.amin(a45, axis=0)) # Column Min over Row
print("Row minimum\n",np.amin(a45, axis=1)) # Row Min over Column

# Array Max
print("Maimum in both array\n",np.amax(a45)) 
print("Maximum in Column\n",np.amax(a45, axis=0)) # Column Max over Row
print("Maximum in row\n",np.amax(a45, axis=1)) # Row max over Column

# Array Sum
print("Sum of all the elements\n",np.sum(a45))
print("Sum of Column\n",np.sum(a45, axis=0)) # Column Sum over Row
print("Sum of rows\n",np.sum(a45, axis=1)) # Row Sum over Column

# Array Mean
print("Mean of all the elements\n",np.mean(a45)) 
print("Mean of column\n",np.mean(a45, axis=0)) # Column Mean over Row
print("Mean of rows\n",np.mean(a45, axis=1)) # Row Mean over Column

# Array Std.Dev.
print("Standard deviation of all the elements\n",np.std(a45))
print("Standard deviation of column\n",np.std(a45, axis=0)) # Column Std.Dev. over Row
print("Standard deviation of row\n",np.std(a45, axis=1)) # Row Std.Dev. over Column

# Array Covariance & Correlation
print("Covariance\n",np.cov(a4, a5)) # Covariance
print("Correlation\n",np.corrcoef(a4, a5)) # Pearson Correlation


#Numpy Application : Linear Algebra

'''
Eq1 : x + 2y = 4 
Eq2 : 3x + 2y = 8
Solve for x & y
'''
a8 = np.array([[1, 2], [3, 2]]); a8
a9 = np.array([4, 8]); a9

# Solution >> x = 2 | y = 1
print(npla.solve(a8, a9))  

