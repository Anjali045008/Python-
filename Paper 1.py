#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Question: Task 1
#Write a python code which will count the number of unique letters and their frequency.
#Test the code with the word ‘Anaconda’. (Note: Remove Case Sensitivity)
#Input: Anaconda
#Output 1: Number of Unique Letters = 5.
#Output 2: {a: 3, c: 1, d: 1, n: 2,# o: 1}

#Solution:

def count_unique_letters(word): #Use define function. In Python, def is a keyword used to define a function. It's short for "define."
    # Convert the input word to lowercase
    word = word.lower()

    # Initialize an empty dictionary to store letter frequencies
    letter_frequency = {}

    # Iterate through the characters in the word
    for char in word:#For loop is being used
        # Check if the character is a letter
        if char.isalpha():
            # If the letter is not in the dictionary, add it with a count of 1
            if char not in letter_frequency:
                letter_frequency[char] = 1
            else:
                # If the letter is already in the dictionary, increment its count
                letter_frequency[char] += 1

    # Calculate the total number of unique letters
    num_unique_letters = len(letter_frequency)

    return num_unique_letters, letter_frequency

# Test the function with the input 'Anaconda'
word = 'Anaconda'
num_unique, frequency = count_unique_letters(word)

print(f"Output 1: Number of Unique Letters = {num_unique}")
print(f"Output 2: {frequency}")






# In[3]:


#Task 2 A student’s evaluation is done based on 4 components: Class_Test (10%), Mid_Term (20%), Project (30%) & End_Term (40%).
#Write a python code to generate a random score between 10 & 90 (use python library: random) and get the evaluation bifurcation (Round off to Nearest Integer).
#Example
#Input = 80 (marks)
#Class_Test = 8 (marks)
#Mid_Term = 16 (marks)
#Project = 24 (marks)
#End_Term = 32 (marks)
#Solution:

import random #random is a Python standard library module that provides functions to generate random numbers. It's used here to simulate the student's total score

# Generate random score between 10 and 90
total_score = random.randint(10, 90) #In Python, randint is a function provided by the random module that generates a random integer between two specified values, inclusive.

# Calculate component scores based on weightage
class_test_score = total_score * 0.10
mid_term_score = total_score * 0.20
project_score = total_score * 0.30
end_term_score = total_score * 0.40

# Round off component scores to nearest integer
class_test_rounded_Score = round(class_test_score)
mid_term_rounded_Score = round(mid_term_score)
project_rounded_Score = round(project_score)
end_term_rounded_Score = round(end_term_score)

# Print the input total score
print("Input Total Score:", total_score)
print()

# Print the rounded scores for each component
print("Component Scores:")
print("Class Test:", class_test_rounded_Score, "marks")
print("Mid Term:", mid_term_rounded_Score, "marks")
print("Project:", project_rounded_Score, "marks")
print("End Term:", end_term_rounded_Score, "marks")



# In[12]:


#Task 3
#Write a python code to display the letters occurring commonly in 2 words.
#Test the code with the words ‘Python’ & ‘Anaconda’. (Note: Remove Case Sensitivity)
#Input 1: Python
#Input 2: Anaconda
#Output: [o, n]

#Solution:

def find_common_letters(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    common_letters = set(word1) & set(word2)
    return common_letters

word1 = 'Python'
word2 = 'Anaconda'

common_letters = find_common_letters(word1, word2)

print(f"Common letters between '{word1}' and '{word2}':")
for letter in common_letters:
    print(letter)


# In[11]:


#Task 4 Write a python code to generate a random score between 0 & 100 (use python library: random). Print the following as output:
#The score
#‘Grade F’ : If the score is less than 40
#‘Grade C’ : If the score is between 40 & 59
#‘Grade B’ : If the score is between 60 & 84
#‘Grade A’ : If the score is between 85 & 100

#Solution:
import random

# Generate a random score between 0 and 100
score = random.randint(0, 100) #In Python, randint is a function provided by the random module that generates a random integer between two specified values, inclusive.

# Assign grades based on the score
if score < 40:
    grade = 'Grade F'
elif 40 <= score <= 59:
    grade = 'Grade C'
elif 60 <= score <= 84:
    grade = 'Grade B'
else:
    grade = 'Grade A'

# Print the score and corresponding grade
print("The score:", score)
print(grade)


# In[10]:


#Task 5 Write a python code to generate a random number between 1 & 99 (use python library: random). Print the following as output:
#The random number [say, 9]
#List of even numbers up to the random number [2, 4, 6, 8]
#List of odd numbers up to the random number [1, 3, 5, 7, 9]
#List of prime numbers up to the random number [2, 3, 5, 7]
#Solution:

import random

# Generate a random number between 1 and 99
random_number = random.randint(1, 99) #In Python, randint is a function provided by the random module that generates a random integer between two specified values, inclusive.

# Print the random number
print("The random number:", random_number)
print()

# List of even numbers up to the random number
even_numbers = [num for num in range(2, random_number + 1) if num % 2 == 0]
print("List of even numbers up to the random number:", even_numbers)
print()

# List of odd numbers up to the random number
odd_numbers = [num for num in range(1, random_number + 1) if num % 2 != 0]
print("List of odd numbers up to the random number:", odd_numbers)
print()

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# List of prime numbers up to the random number
prime_numbers = [num for num in range(2, random_number + 1) if is_prime(num)]
print("List of prime numbers up to the random number:", prime_numbers)


# In[13]:


#Task 6:

import random

# Generate a random 4-digit number between 1000 and 9999
random_number = random.randint(1000, 9999) #In Python, randint is a function provided by the random module that generates a random integer between two specified values, inclusive.

# Print the random number
print("Random 4-digit number:", random_number)

# Calculate and print each digit with its place value
thousands_digit = random_number // 1000
hundreds_digit = (random_number // 100) % 10
tens_digit = (random_number // 10) % 10
units_digit = random_number % 10

print("Thousands digit:", thousands_digit, "with place value:", thousands_digit * 1000)
print("Hundreds digit:", hundreds_digit, "with place value:", hundreds_digit * 100)
print("Tens digit:", tens_digit, "with place value:", tens_digit * 10)
print("Units digit:", units_digit, "with place value:", units_digit)


# In[14]:


#Task 7
#Write a python code to generate 5 random numbers between -9 & +9 (use python library: random). Print the list of 5 random numbers and their sum.

#Solution:

import random

# Generate a list of 5 random numbers between -9 and +9
random_numbers = [random.randint(-9, 9) for _ in range(5)]

# Print the list of random numbers
print("List of random numbers:", random_numbers)

# Calculate the sum of the random numbers
sum_of_numbers = sum(random_numbers)

# Print the sum of the random numbers
print("Sum of random numbers:", sum_of_numbers)


# In[15]:


#Task 8
#Write a python code to calculate the number of Years, Months & Days, with respect to Today, given a Date.

#Solution:

from datetime import datetime #datetime is a module in Python's standard library used for working with dates and times.

# Get the input date from the user (in yyyy-mm-dd format)
input_date_str = input("Enter a date (yyyy-mm-dd): ")

# Convert the input date string to a datetime object
input_date = datetime.strptime(input_date_str, '%Y-%m-%d')

# Get today's date as a datetime object
today_date = datetime.today()

# Calculate the difference between the two dates
date_difference = today_date - input_date

# Calculate the number of years, months, and days
years = date_difference.days // 365
remaining_days = date_difference.days % 365
months = remaining_days // 30
days = remaining_days % 30

# Print the result
print(f"Number of Years: {years}")
print(f"Number of Months: {months}")
print(f"Number of Days: {days}")


# In[7]:


#Task 9:Write a python code to generate the following ‘diamond’ pattern.
#Solution:
#function to print diamon star pattern
def pattern(rows):
    #intialize variables k1 and k2
    k1=1
    k2=rows-1

    #1St outer loop for each row in the upper half
    for i in range(0,rows):
        #Inner loop to print elements in a particular row
        for j in range(0,rows):
            #if j>=k2 print *
            if j>=k2:
                print(' * ',end=' ')
            #if j<k2 print blank space
            else:
                print(' ',end=' ')
        #decrement k2
        k2-=1
        #print new line character for each row
        print()

    #2nd Outer loop for each row in the lower half
    for i in range(0,rows):
         #Inner loop to print elements in a particular row
        for j in range(0,rows):
            #if j>=k1 print *
            if j>=k1:
                print(' * ',end=' ')
            #if j<k1 print blank space
            else:
                print(' ',end=' ')
        #increment k1
        k1+=1
        #print new line character for each row
        print()

#Taking input
n=int(input('Enter the number of Rows : '))
#Calling Function
pattern(n)


# In[17]:


#Task 10
#Write a python code to create a list of 10 random letters (say List A). Create a copy of List A (say List B).
#Shuffle both List A & B. Treat each element of List A (say a) as Source and the corresponding element of List B (say b) as Destination.
#It is assumed that a from list A is connected to b from List B. Map the network of all connected elements such that an inquiry of any element will show the connected paths to & from the element

#Solution:

import random

def generate_random_letters_list(length):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_letters = [random.choice(letters) for _ in range(length)]
    return random_letters

def shuffle_and_build_network(list_a, list_b):
    combined_lists = list(zip(list_a, list_b))
    random.shuffle(combined_lists)
    shuffled_list_a, shuffled_list_b = zip(*combined_lists)

    network = {}
    for source, destination in zip(list_a, shuffled_list_b):
        if source not in network:
            network[source] = []
        network[source].append(destination)

    return network

def print_connected_paths(network, element, visited=None):
    if visited is None:
        visited = set()
    if element in network and element not in visited:
        visited.add(element)
        connected_elements = network[element]
        print(f"Connected paths from {element}: {', '.join(connected_elements)}")

        for connected_element in connected_elements:
            print_connected_paths(network, connected_element, visited)

list_a = generate_random_letters_list(10)
list_b = list(list_a)  # Create a copy of list_a
random.shuffle(list_a)
random.shuffle(list_b)

network = shuffle_and_build_network(list_a, list_b)

# Choose an element from list_a to start exploring the network
start_element = list_a[0]
print_connected_paths(network, start_element)

