# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 2023

@author: Anjali
"""

#Python program to demonstrate String Datatype

# Creating a String
a="Hello, I am anjali" 
print(a)

# Printing First character
String1="I am Anjali"
print("\nFirst character of String is: ")
print(String1[0])
 
# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])

#Program to reverse a string
name = "Anjali Kumari"
print(name[::-1])


# Python Program to demonstrate String slicing
b="pythonisacasesensitive language"
print(b)

# Printing 1st to 12th character
print("\nSlicing characters from 1-12: ")
print(b[1:12])
 
# Printing characters between 3rd and 2nd last character
print("\nSlicing characters between " +
      "3rd and 2nd last character: ")
print(b[3:-2])

# Splits Word into a List of Individual Characters 
s1 = 'i love Ice coffee' 
print((s1.split())) #splitting of strings gives a list

# Python3 program to show the working of upper() function
text = 'AnjaliKumaRi'
 
# upper() function to convert string to upper case
print("\nConverted String:")
print(text.upper()) #ANJALIKUMARI
 
# lower() function to convert string to lower case
print("\nConverted String:")
print(text.lower()) #anjalikumari
 
# converts the first character to upper case and rest to lower case
print("\nConverted String:")
print(text.title()) #Anjalikumari
 
#swaps the case of all characters in the string upper case character to lowercase and viceversa
print("\nConverted String:")
print(text.swapcase()) #aNJALIkUMArI
 
# convert the first character of a string to uppercase
print("\nConverted String:")
print(text.capitalize()) #Anjalikumari
 
# original string never changes
print("\nOriginal String")
print(text) 

#Returns the number of occurrences of a substring in the string--->count()
A= "Anjali Kumari is a student of BDA"
B = A.count('e')
print(B)



