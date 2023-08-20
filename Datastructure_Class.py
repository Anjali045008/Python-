# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 2023

@author: Anjali
"""

# Basic Data Structures

#Set-->a Set is an unordered collection of data types that is iterable, 
#mutable and has no duplicate elements.

#Sets can be created by using the built-in set() function with an iterable 
#object or a sequence by placing the sequence inside curly braces,
#separated by a ‘comma’.

#A set cannot have mutable elements like a list or dictionary, as it is mutable.  

# Python program to demonstrate Creation of Set in Python
 
# Creating a Set
set1 = set()
set2={} #Another way to create a set
print("Initial blank Set: ")
print(set1,set2)
 
# Creating a Set with the use of a String
set1 = set("Anjali") #It treats A and a separately
set2 = {'a','j','a','l','i'} 
print("\nSet with the use of String: ")
print(set1)
print(type(set2))
print(set2)
 
# Creating a Set with the use of a List
set1 = set(["Hello", "I'm", "Anjali"])
print("\nSet with the use of List: ")
print(set1)
 
# Creating a Set with the use of a tuple
t=("Hello","I'm","Anjali")
print("\nSet with the use of Tuple: ")
print(set(t))
 
# Creating a Set with the use of a dictionary
d={"Anjali":1,"Kumari":2,"BDA":3}
print("\nSet with the use of Dictionary: ")
print(set(d))

# Creating a Set with a List of Numbers (Having duplicate values)
set2 = set([1, 2, 2, 4, 3, 3, 3, 6, 7])
print("\nSet with the use of Numbers: ")
print(set2)
 
# Creating a Set with a mixed type of values in a list

set2 = set([2, 3.4, 'Asd', True, False,'For', None, 'Asd'])
# If I mention 1,0 and True,False then only one of them will come 1,0 or True,False
print("\nSet with the use of Mixed Values")
print(set2)

#Lists cannot be added to a set as elements because Lists are not hashable
# whereas Tuples can be added because tuples are immutable and hence Hashable.
#Hashable-->


# Python program to demonstrate Addition of elements in a Set
 
# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)
 
# Adding element and tuple to the Set
set1.add(2)
set1.add(3)
set1.add(5)
set1.add(4)
set1.add((6, 7)) #Adding Tuple in the set
print("\nSet after Addition of Five elements: ")
print(set1) 

# Removing elements from Set using Remove() method
set1.remove(5)
set1.remove(4)
print("\nSet after Removal of two elements: ")
print(set1)

s1 = {2, 0, 2, 1}
s2 = {2, 0, 2, 3}
s12_union1=s1.union(s2) #union 
s12_union2=s1 | s2      #union
print(s12_union1)
print(s12_union2)
s12_intersection1 = s1.intersection(s2) #Intersection
s12_intersection2 = s1 & s2             #Intersection
print(s12_intersection1)  
print(s12_intersection2)  
s12_difference1 = s1.difference(s2)     #Difference
s21_difference2 = s2 - s1               #Difference
print(s12_difference1)
print(s21_difference2)

#-----------------------------------------------------------------------------#
#In simple language, a list is a collection of things, enclosed in [ ] and separated by commas. 

#The list is a sequence data type which is used to store the collection of data.
#Tuples and String are other types of sequence data types.
L0=[] #Empty List
print(type(L0)) #Dtermining the Type of L0
L1=[2,1,3,4,54]
print(L1)
l2 = list((1, 'Two', None, [True, False])) #Complex List
print(type(l2))
print(l2)

# accessing a element from the list using index number
print("Accessing a element from the list")
print(l2[0])
print(l2[2])

# Creating a Multi-Dimensional List (By Nesting a list inside a List)
List = [['Anjali', 'Kumari'], ['Lucky']]
 
# accessing an element from the Multi-Dimensional List using index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1]) #Accessing the second element from the first list using index
print(List[1][0])

# Creating a List
List1 = [1,2,3]
print(len(List1)) #Getting lenght of List 
 
# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2)) #Getting lenght of List 

# Python program to take space separated input as a string
#split and store it to a list and print the string list
 
# input the list as string
#string = input("Enter elements (Space-Separated): ")
 
# split the strings and store it to a list
#lst = string.split() 
#print('The list is:', lst)   # printing the list

# Python program to demonstrate
# Addition of elements in a List
 
# Creating a List
List = []
print("Initial blank List: ")
print(List)
 
# Addition of Elements in the List
List.append(1)
List.append(2)
List.append(3)
print("\nList after Addition of Three elements: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)
 
# Addition of List to a List
List2 = ['Hello', 'Everyone']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)

# Python program to demonstrate
# Addition of elements in a List
  
# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)
 
# Addition of Element at specific Position (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Python')
print("\nList after performing Insert Operation: ")
print(List)

# Reversing a list
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
print("Reversed List-",mylist[::-1])  #one way to reverse the list
mylist.reverse() #another way to reverse the list
print(mylist)

# Python program to demonstrate Removal of elements in a List
 
# Creating a List
List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)
 
# Removing elements from List using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)

List = [1, 2, 3, 4, 5, 6]
 
# Removing element from the Set using the pop() method
List.pop() # here it will remove last element
print("\nList after popping an element: ")
print(List)
 
# Removing element at a specific location from the Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)
del List[3:] # Removing multiple element from list by index
print("Removing multiple element from list by index",List)

# Python program to demonstrate Removal of elements in a List
 
# Creating a List
List = ['I', 'L', 'O', 'V', 'E', 'P',
        'Y', 'T', 'H', 'O', 'N']
print("Initial List: ")
print(List)
 
# Print elements of a range using Slice operation
Sliced_List = List[3:8] #it will fetch from 3rd to 8th(Excluding)
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)
 
# Print elements from a pre-defined point to end
Sliced_List = List[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_List)
 
# Printing elements from beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)

#Joining the 2 list
l3 = ['a', 'b', 'c']
l4 = [1, 2, 3]
l34 = l3 + l4
print(l34)

#Sorting the given List
L1=[12,3,45,76,32,45,67]
L1.sort() #Sort List in Ascending Order
print(L1)
L1.sort(reverse=True) #Sort List in Descending Order
print(L1)

#-----------------------------------------------------------------------------#
# =============================================================================
# Tuple is a collection of Python objects much like a list. The sequence of values
# stored in a tuple can be of any type, and they are indexed by integers. 
# 
# Values of a tuple are syntactically separated by ‘commas’. Although it is not 
# necessary, it is more common to define a tuple by closing the sequence of 
# values in parentheses. This helps in understanding the Python tuples more easily.
# =============================================================================

# Non-Editable-->Tuple
# Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)
 
# Creating a Tuple with the use of string
Tuple1 = ('Gamers', 'For','Life')
print("\nTuple with the use of String: ")
print(Tuple1)
 
# Creating a Tuple with the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))
 
# Creating a Tuple with the use of built-in function
Tuple1 = tuple('Python')
print("\nTuple with the use of function: ")
print(Tuple1)

#Update Tuple first we will convert it into list and after updating we will 
#again convert it into tuple

t=(0, 1, 1, 2, 3, 5, 8)
t_list=list(t) #converted tuple into list inorder to update it
L1=[34,23,54,67]
#t_list.append(L1) #here we are adding a list into a list
t_list.extend(L1) #here it will add numbers in the list to update that list
print(t_list)
t_new=tuple(t_list)
print(t_new)

#-----------------------------------------------------------------------------#

#Python programming language comes with in-built data structure like list, 
#dictionary, set, tuple, etc. Range in python is another in-built python 
#datatype which is mainly used with loops in python.

r1=range(5)
print(type(r1))
print(list(r1)) #if range will be till 5 it will not include 5 instead(0,1,2,3,4)
r2=range(1,10,2)#1 to 10 with increment of 2 = [1,3,5,7,9] | 10 not included
print(list(r2))
r3=range(5,0,-1)#5 to 0 with decrement of 1 = {5, 4, 3, 2, 1} | 0 not included
print(list(r3))

#-----------------------------------------------------------------------------#
# =============================================================================
 
# In Python, a dictionary can be created by placing a sequence of elements within
# curly {} braces, separated by ‘comma’. Dictionary holds pairs of values, one 
# being the Key and the other corresponding pair element being its Key:value. 
# Values in a dictionary can be of any data type and can be duplicated, whereas 
# keys can’t be repeated and must be immutable.
# =============================================================================
#Dictionary holds key:value pair. Key-Value is provided in the dictionary to 
#make it more optimized. 

# Creating a Dictionary with Integer Keys
a_dict={1:"Anu",
        2:"Jibran",
        3:"Anjali"}
print(a_dict)
print(type(a_dict))

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
  
# Adding elements one at a time
Dict[0] = 'Python'
Dict[1] = 'For'
Dict[2] = 24
print("\nDictionary after adding 3 elements: ")
print(Dict)
# Adding set of values to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)
# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
  
# Adding Nested Key value to Dictionary
Dict[5] = {'Nested': {'1': 'Anu', '2': 'Python'}}
print("\nAdding a Nested Key: ")
print(Dict)

dict1={
    "name":['Anurag','Anjali','Rishi','Shubh'],
    "marks":[86,92,89,70],
    "city":['Raipur','Pune','Delhi','Mumbai']
}

print(dict1.keys()) #List of All Keys will be displayed
print(dict1.values()) #List of All values will be displayed
print(dict1['name'])
dict1['marks'][2]=95 #Updated the Value of a Key
print(dict1)
dict1['Section']= 'A','B','C','H'
print(dict1)
print(dict1.keys())
dict1.pop('Section') #Remove a Key along with its Value
print(dict1)
