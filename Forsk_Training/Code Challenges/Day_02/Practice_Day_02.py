# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:46:48 2019

@author: dell
"""


"""
Hands On 1
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 

"""
list1 = list(range(1,21))

list1[0::2]

list1[1::2]


"""
Hands On 2
# Make a function to find whether a year is a leap year or not, return True or False 

"""

def leap_yr(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("True")
    else:
        print("False")
year = int(input("Enter Year : "))
leap_yr(year)


"""
Hands On 3
# Make a function days_in_month to return the number of days in a specific month of a year
"""

#user = input("Enter name of the Month : ")
#user1 = user.lower()
#
#a=['jan','feb','march','apr','may','jun','jul','aug','sep','oct','nov','dec']
#b=[31,28,31,30,31,30,31,31,30,31,30,31]
#
#if user == a[n]:
#    print(b[n])


year = int(input("Enter the Year : "))
month = input("Enter first three letters of the Month : ")
mon_low = month.lower()

if mon_low == "jan":
    print("Number of days in January is 31")
elif mon_low == "mar":
    print("Number of days in March is 31")
elif mon_low == "apr":
    print("Number of days in April is 30")
elif mon_low == "may":
    print("Number of days in May is 31")
elif mon_low == "jun":
    print("Number of days in June is 30")
elif mon_low == "jul":
    print("Number of days in July is 31")
elif mon_low == "aug":
    print("Number of days in August is 31")
elif mon_low == "sep":
    print("Number of days in September is 30")
elif mon_low == "oct":
    print("Number of days in October is 31")
elif mon_low == "nov":
    print("Number of days in November is 30")
elif mon_low == "dec":
    print("Number of days in December is 31")
else:
    print("You may have entered nothing ot wrong spelling of the month")

def leap_yr(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("Number of days in February is 29")
    else:
        print("Number of days in February is 28")

if mon_low == "feb":
    leap_yr(year)
    

"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']

vowels = list("AEIOUaeiou")

final_list = []

for i in state_name:
  temp_list = []
  for j in i:
      if j not in vowels:
        temp_list.append(j)
  final_list.append("".join(temp_list))
print(final_list)



"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""

user = int(input("Enter number : "))
n=1
for i in range(user+1):
    print(i*"*")
for i in range(user-1,0,-1):
    print(i*"*")


"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""

user = input("Enter input : ").split()
#user = [int(i) for i in user]
for i in user:
    if int(i) > 0 and str(i)==str(i)[::-1]:
        print(i, True)
    else:
        print(i, False)









