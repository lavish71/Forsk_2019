"""
Code Challenge
  Name: 
    Age Calculator
  Filename: 
    age_cal.py
  Problem Statement:
    Lets assume your age is 21 today
    What would be your age after 5 years from today 
    How old were you 10 years back
  Hint: 
    You need to add to calculate future age 
    You need to subtract to calculate your past age 
"""

# Enter your age
user_age = int(input("Enter your age >"))

# Future age
f_years = 5

# Past age 
p_years = 10

future_age = user_age + f_years

past_age = user_age - p_years

print ("Your current age is" + str(user_age))

print ("Your age after "+ str(f_years) + " years will be " + str(future_age))

print ("Your age before "+ str(p_years) +  " years was " + str(past_age) )

