# -*- coding: utf-8 -*-
"""
Created on Tue Aug  17 2023

@author: Anjali
"""
#=============================================================================
 
#=============================================================================
x = 0
num = int(input("Enter number"))
while x < num:
    print("Countdown",x)
    x = x + 1
#=============================================================================
num=int(input('enter a number :'))
while num>0:
    print('countdown',num)
    num=num-1
print('done')

for i in range(5,0,-1):
  print('countdown',i)
  
#=============================================================================
  #take string as a input anaconda split it into 2 list vowel and consonants
  
string = input('String: ')
  
print('Vowels: ')
for ch in string:
   if ch in "AEIOUaeiou":
      print(ch, end=', ')
  
print('\nConsonants: ')
for ch in string:
   if ch not in "AEIOUaeiou ":
      print(ch, end=', ')
        
w=['a','n','a','c','o','n']    
vl=[]
cl=[]
vowel=['a','e','i','o','u']
for L in w:
    if L in vowel:
        vl.append(L)
    else:
     cl.append(L)
#=============================================================================
#=============================================================================
ml=[1,2,2.4,3.1,'anu','anjali','rishi',True,False,'',]#use type function to solve this
num_int=[]
num_float=[]
string_list=[]
bool_list=[]
none_list=[]
  
# Segregate elements into different lists based on type
for item in ml:
    item_type = type(item)
      
    if item_type in (int, float):
        num_int.append(item)
    elif item_type == str:
        string_list.append(item)
    elif item_type == bool:
        bool_list.append(item)
    elif item_type == type(None):
        none_list.append(item)
  
print("\nNumber List:\t", num_int)
print("\nString List:\t", string_list)
print("\nBoolean List:\t", bool_list)
print("\nNone List:\t", none_list)
#=============================================================================
#=============================================================================
  
def myadd(num1,num2):
      num3 = (num1 + num2)/2
      return num3
   
num1, num2 = 5, 15
ans = myadd(num1, num2)
print("The average of",num1, "and", num2, "results" ,ans)
#=============================================================================
#=============================================================================

''' 
Create a Vowel List and Count Function 'vlc' such that, for a given Word, vlc:
1. Creates a List of Vowels
2. Counts the Number of Vowels 
'''
def vlc(word):
    vowel = ['a', 'e', 'i', 'o', 'u']
    vl = [] # empty vowel list
    vc = 0 # vowel count
    char_list = list(word)
    for c in char_list:
        if c in vowel:
            vl.append(c)
            vc = vc + 1
    print('vowel list:', vl)
    print('vowel count:', vc)
    return(vl, vc)
word="Anuragsharma"
a=vlc('AnuragSharma')
print(a)

#for loop

for i in range(1,8):# for loop
     print(i)

#Writing table for any any number and taking input from user     
i=1
a=int(input("Enter the number for which you want a table for"))
for i in range(1,11):
     print(a,"X",i,"=",a*i)
     i+=1

#Create a list and say Hello to a person whose name start with any particular letter     
l1=["Anurag","Rishi","Dhruv","Kartik","Lucky","Anjali"]
for name in l1:
     if name.startswith("A"):
         print("Hello " + name)