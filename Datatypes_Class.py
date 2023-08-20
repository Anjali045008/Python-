# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 2023

@author: Anjali 
"""

# Data types in Python
n=1 # DataType-->int
print(type(n)) 
a=1.5; # DataType --> Float
print(type(a))
import math #importing math library to get the value of pi
# math is a built-in module in the Python 3 standard library
# that provides standard mathematical constants and functions.
print(math.pi)
# Numeric Operations
n1 = 1; n2 = 2; n3 = 3; n4 = 4; n5 = 5
n11 = n3 + n2 - n1 # Addition & Substraction
print(n11) #4
n12 = (n11 * n4) / n5 # Multiplication & Division
print(n12) #3.2
n13 = n12 ** n2 # Exponent or Power
print(n13) #10.240000000000002
n14 = round(n13, 2) # Round Off with Decimal Places (DP = 2)
print(n14) #309.76

# Python Program for Creation of String
 
# Creating a String with single Quotes
String1 = 'Hello world'
print("String with the use of Single Quotes: ")
print(String1)
 
# Creating a String
# with double Quotes
String2 = "I'm Anjali Kumari"
print("\nString with the use of Double Quotes: ")
print(String2)
print(type(String2))
 
# Creating a String with triple Quotes
String3 = '''I want to join a consulting company'''
print("\nString with the use of Triple Quotes: ")
print(String3)
print(type(String3))
 
# Creating String with triple Quotes allows multiple lines comment
String4 = '''Gamers
            For
            Life'''
print("\nCreating a multiline String: ")
print(String4)

# Python program to demonstrate boolean type
 
print(type(True))
print(type(False))
b1=True
b2=False
print(b1 and b2) #AND Operator
print(b1&b2)
print(b1 or b2) #OR Operator
print(b1|b2)  
print(not b1) # NOT Operator
print(not b2)

 
# Python program to demonstrate None data type
print(type(None))
 