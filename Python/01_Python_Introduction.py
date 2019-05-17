"""
Part 1 - Python Introduction

  Instructor      :
  Course Name     :
  Course Length   :
  Description     : 
    Learn the building blocks of the wonderful general purpose programming language Python
  Audience        :
  Course Syllabus :

"""


"""
Python in Industry
  In Google Python is one of the primary language
  Honeywell uses Python for generating documentation  
  Maya uses python for scripting 
  GIS heavy uses python for scripting 
  US Govt does statistical analysis and Data Visualisation
  NASA and Newyork Stock Exchange
  Disney/Pixar Films uses to provide more realistic effect in movies
  Youtube, Instagram, Reddit, Pinterest power their CMS ( Content Management System )
  Facebook uses a lot for internal scripting  
  Face/Speech Recognition
  Controlling Robots and Automation ( MicroPython )
  Data Scientist uses Anaconda with more than 400 packages for science, math, 
  engineering and data analysis

Where we can use Python
    1. For developing Desktop Applications
    2. For developing web Applications
    3. For developing database Applications
    4. For Network Programming
    5. For developing games
    6. For Data Analysis Applications
    7. For Machine Learning
    8. For developing Artificial Intelligence Applications
    9. For IOT


History of Python
  Easy as ABC ( developed at Centrum Wiskunde & Informatica, Netherlands)
  20th Feb 1991 by Guido van Rossum, 
  British Comedy Troupe - Monty Python Flying Circus
  The Zen of Python (19)  


Features of Python
    General Purpose Dynamic Compiled Language 
    Simple and Easy to Learn
    Freeware and Open Source
    High Level Programming Language
    Platform Independent
    Portable
    Dynamically Typed
    Procedure and Object Oriented and Functional  
    Interpreted
    Extensible ( CPython, JPython )
    Embedded
    Extensive Library
    

Installation of IDLE
  Checking the verison of python installed using ( python -- version)
  Check the installation PATH of python 
  (which -a python) (which -a python2) (which -a python3)
  The Terms "Interactive" and "Shell"
  Starting the Python Shell from CMD or TERMINAL ( python )
  REPL ( Read Evaluate Print Loop )is the best environment to learn a language
  Starting Python Shell using IDLE ( Spotlight Search or Windows Search ) 
  How to Quit the Python Shell using quit() or exit() or CRTL+D

"""

#Python Shell as a Calculator (Trainer Hands On)

5 + 2

5 - 2

5 * 2

5 / 2 

#( Ver 2 always return integer value but ver 3 returns float)


#Printing on the Console (Trainer Hands On)
print ("Hello World")


"""
Literals using primitive data types
  Numeric ( int/long)
    4
  Floating Point ( float )
    10.6
  String ( str )
    "Hello World"
  Boolean ( bool )
    True False
  NoneType ( None )
    None

"""


#How to check the data type of a literal (Trainer Hands On)
type (4)

type (10.6)

type (True)
type (False)

type ('FORSK')
type ("FORSK")
type ('''FORSK''')
type ("""FORSK""")

type ( None )


"""
Type Conversion using Global Functions  
  int()
  float()
  str()
  bool()
"""


#How to convert the data type (Trainer Hands On)
int (4)
int (10.6)
int ("10")
int (True)
int (False)


float (4)
float (10.6)
float ("10")
float (True)
float (False)


str (4)
str (10.6)
str ("10")
str (True)
str (False)


bool (4)        # Any integer greater than zero is True
bool (0)

bool (10.6)     # Any float greater than 0.0 is True
bool(0.0)

bool ("10")
bool("")

bool (True)
bool (False)

bool (None)




#Single Line Commenting (Trainer Hands On)
#Using HASH or POUND ( # ) 

# This is a comment line

"""
How to store data in Python variables 
  Variable is like a Box and you put a literal in it 
  Literal can be of any above types
  Introduce the concept of Heap and Stack
  Python variables in Stack are references to objects in Heap
  Actual data is contained in the object
  In Python everything is object

  Identity function id() can be used to find the unique identity of the object it is pointing to 


"""

#   Example for explanation with visual
x = 42 
id(x)
print(x)

x = 78
id(x)
print(x)



# Both a and b point to the same object in heap
a = 42 
id(a)
print(a)

b = 42
id(b)
print(b)


"""
    List of Python inbuilt functions
    1. type() - to check the type of variable
    2. id() - to get address of object
    3. print() - to print the value
"""


"""
Naming Convention (Trainer Hands On)
    A name in Python program is called identifier

    Valid characters for variable names, class name, module name, function name ( Identifiers)
        "A" through "Z" 
        "a" through "z" 
        underscore _ 
        digits 0 through 9 (except for the first character) 
  
  Variable names and identifier names can additionally contain Unicode characters as well.
  
  Rules
      1. Alphabet Symbols (Either Upper case OR Lower case)
      2. If Identifier is start with Underscore (_) then it indicates it is private.
      3. Identifier should not start with Digits.
      4. Identifiers are case sensitive.
      5. We cannot use reserved words as identifiers
      6. There is no length limit for Python identifiers. But not recommended to use too lengthy
      identifiers.
      7. Dollor ($) Symbol is not allowed in Python.

 """

8p = "FORSK"   
!p = "FORSK"
$p = "FORSK"
# Cannot start with a number, Exclamation and $ sign

p!p = "FORSK"
p$p = "FORSK"
# Cannot have a Exclamation or  $ sign or any other special characters

p8 = "FORSK"
# Can have numbers within

+p = "FORSK"
-p = "FORSK"   
*p = "FORSK"
/p = "FORSK"
# Cannot start with or have any Arithmetic Operators
  

for = "FORSK"   
print = "FORSK"

# Cannot use keywords ( 33 Reserved Words)  used in python syntax
# and, as, assert, break, class, continue, def, del, elif, else,
# except, while, finally, for, from, global, if, import, in, is, 
# lambda, yield, nonlocal, not, or, pass, raise, return, with, try, 
# False, True, None



# help()  and then type "keywords" to get the list
# import keyword
# keyword.kwlist


_for = "FORSK" 
# _ is the only special character which is allowed

my age  = 40  
# Space is not allowed between the variable names

my_age = 40 
# underscore is the best way to have long variable names

"""
Best Practice for Naming Convention
  # Discuss UPPERCASE, lowercase and CamelCase way of naming the variables
  # Never use the characters 'l' (lowercase letter "L")
  # Never use the characters  'O' ("O" like in "Ontario")
  # Never use the characters 'I' (like in "Indiana") 
  # Never use single character variable names.
"""

"""
    1.If identifier starts with _ symbol then it indicates that it is private
    2.If identifier starts with __(two under score symbols) indicating that strongly private
        identifier.
    3.If the identifier starts and ends with two underscore symbols then the identifier is
      language defined special name,which is also known as magic methods.

"""

print ("Hello")
#Printing Output of a variable on console (Trainer Hands On)
my_age = 40
print (my_age)


"""
Python contains the following inbuilt data types
    1.int
    2.float
    3.complex
    4.bool
    5.str
    6.bytes
    7.bytearray
    8.range
    9.list
    10.tuple
    11.set
    12.frozenset
    13.dict
    14.None

"""

"""
We can represent int values in the following ways
    1. Decimal form         (a = 10)
    2. Binary form          (a = 0b1111 )
    3. Octal form           (a = 0o123)
    4. Hexa decimal form    (a = 0xFACE )
    Being a programmer we can specify literal values in decimal, binary, octal and hexa
    decimal forms. But PVM will always provide values only in decimal form.

    a=10
    b=0o10
    c=0x10
    d=0b10
    print(a) #10
    print(b) #8
    print(c) #16
    print(d) #2

    Base Conversions
    1.bin(): We can use bin() to convert from any base to binary
    2. oct(): We can use oct() to convert from any base to octal
    3. hex(): We can use hex() to convert from any base to hexa decimal
    
    Complex Data Type:
        A complex number is of the form
        a + bj 
        a is known as Real part 
        b is imaginary part
        j = sqrt of -1
        
        a and b can be int or float
        
    
"""


#One variable can hold different data type (Trainer Hands On)
# Integer
my_var = 8
type(my_var)

# Float
my_var = 26.5
type(my_var)
  
# String
my_var = "FORSK"
type(my_var)
  
# Boolean
my_var = True
type(my_var)
  
# NoneType
my_var = None
type(my_var)


#Understanding Error Messages in Python (Trainer Hands On)



#NameError happens when something does not exists
5 + z

#TypeError happens when there is data type mis match
5 + "a"

#Solution to convert the 5 using the str function to string first and then use it
str(5) + "a"
"5" + "a"

#Syntax Error 
print("Hello)

#Arithmetic Operator  

#+ Addition
7 + 5 

#- Subtraction
7 - 5

#* Multiplication 
7 * 5

#/ Division   
7 / 5

#Ver 2 always return integer value 
#Ver 3 returns float value
#Division by 0 would return ZeroDivisionError
  
#% Modulus 
7 % 5

#** Exponent
7 ** 5

#// Integer Division or Floor Division , always returns integer
7 // 5

"""
Arithmetic Expressions ( BODMAS )
  Python follows the usual order of operations in expressions. 
    exponents and roots
    multiplication and division
    addition and subtraction
"""

3 + 2 * 4

(3 + 2) * 4


#Other Global Function (Trainer Hands On)
#Introduce the round function to show the rounding to nearest integer value 

int ( 5.9 )
round ( 5.9 )
round ( 5.4 )
round ( 5.5 )

"""
Assignment Operator  ( give a hands on using two different number )
  = Assignment 
    ( a = 5 )
  += Addition 
    ( a += 1 ) ( a = a + 1 )
  -= Subtraction 
    ( a -= 1 ) ( a = a - 1 )
  *= Multiplication 
    ( a *= 1 ) ( a = a * 1 )
  /= Division 
    ( a /= 1 ) ( a = a / 1 )
  %= Modulus 
    ( a %= 1 ) ( a = a % 1 )
  **= Exponent 
    ( a **= 1 ) ( a = a ** 1 )
  //= Integer Division or Floor Division 
    ( a //= 1 ) ( a = a // 1 )
"""

#Taking Integer Input from user
age = input ( "Enter your Age > ")
print (age)
print (type(age))
  
age = int(age)
print (age)
print (type(age))


# Best Practice 
age = int(input ( "Enter your Age > "))
print (age)
print (type(age))


#Taking Floating Point Input from user 
temperature  = input ( "Enter your temperature of your city > ")
print (temperature)
print (type(temperature))

  
temperature = float(temperature)
print (temperature)
print (type(temperature))

# Best Practice 
temperature  = float(input ( "Enter your temperature of your city > "))
print (temperature)
print (type(temperature))


#Taking String Input from user using raw_input function 
name = input ( "Enter your Name >")
print (name)
print (type(name))


#Adding two string using + operator  ( Concatenation ) 
"Hello" + "World"

#Add string and number using + operator 
"Hello " + 5

#Add string and number using + operator 
"Hello " + str(5)


#Printing output to the screen using the + operator
str1 = "FORSK"
str2 = "TECHNOLOGIES"
print ( str1 + str2 )
print (str1 + " " + str2)

#Printing output to the screen using the , COMMA operator
print (str1 , str2)


"""
Writing and executing programs in files (Trainer Hands On)
  Creation of .py Python Script in IDLE and Saving it.
  Running of the .py Pyton Script from IDLE
  Running of the .py Python Script from TERMINAL or CMD
  Autocomplete variable names by using ATL + / in IDLE
  Indentation concept to be introduced


Block and Indentation Concept Introduction
  Block with nested block
  Indenting Code


Best Practice for creation of Projects (Trainer Hands On)
  # Step 1
  #  Create a file first.py from IDLE File->New

  # Step 2  
  # Define a new function main

  def main():
    pass

  # Step 3
  # Calling the newly created function  
  main()

  # Step 4
  # Running from CMD or TERMINAL
  # python first.py
"""

"""

Installation of Spyder ( Anaconda )  (Trainer Hands On)
  Explanation of the Different Windows
  Creation of first.py in this environment also
  Running of the Project
  Running of some part of code in Spyder
  Running of the project from command line python
"""




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


"""
Code Challenge
  Name: 
    Height Calculator
  Filename: 
    height_cal.py
  Problem Statement:
    Lets assume your height is 5 Foot and 11 inches 
    Convert 5 Foot into meters and 
    Convert 11 inch into meters and 
    print your total height in meters and 
    print your total heigjt in centimetres also 
  Hint: 
    1 Foot = 0.3048 meters 
    1 inch = 0.0254 meters 
    1 m = 100 cm 
"""


"""
Code Challenge
  Name: 
    Adult Body Mass Index Calculator
  Filename: 
    bmi_cal.py
  Problem Statement:
    Assuming your weight in kilogram and height in meters  
    Calculate your BMI value and print it ?
  Hint: 
    Divide your weight in kilograms (kg) by your height in metres (m)
    Then divide the answer by your height again to get your BMI
"""


"""
Code Challenge
  Name: 
    Ponderal Index Calculator
  Filename: 
    ponderal_cal.py
  Problem Statement:
    Calculate the Ponderal Index of a Person and print it
  Hint: 
    Divide the BMI by your Height ( meters ) to get your Ponderal Index
"""


"""
Code Challenge
  Name: 
    Target Heart Rate Calculator
  Filename: 
    heartrate_cal.py
  Problem Statement:
    Calculate the Maximum Heart Rate and Target Heart Rate Range 
    ( Lower and Higher value ) of a person of a specific age.
    Lets Assume your age is 21 years
  Hint: 
    Subtract your age from 220 to get your Maximum Heart Rate
    Lower end of your Target Heart Rate is 70% of Maximum Heart Rate
    Higher end of your Target Heart Rate is 85% of Maximum Heart Rate
    Heart Rate = Beats per minute 
"""

"""
Code Challenge
  Name: 
    Temperature Calculator
  Filename: 
    temp_cal.py
  Problem Statement:
    Assume today's temperature in Jaipur is 29 degree Centigrade. 
    Calculate the temperate in Degree Fahrenheit and print it.
    Calculate the temperature in Degree Kelvin and print it.
  Hint: 
    Multiply by 9/5 and add 32  to get in Fahrenheit
    Add 273 approximately to get in Kelvin
"""

"""
Code Challenge
  Name: 
    Gas Mileage Calculator
  Filename: 
    mileage_cal.py
  Problem Statement:
    Assume my car travels 100 Kilometres after putting 5 litres of fuel. 
    Calculate the average of my car. 
  Hint: 
    Divide kilmeters by the litres used to get the average
"""


"""
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
 """    

"""
Code Challenge
  Name: 
    Gravity Calculator
  Filename: 
    gravity_cal.py
  Problem Statement:
    Compute the position of the object after falling for 10 seconds. 
    Output the value meters and assume that the acceleration is -9.81  
  Hint: 
    Distance = (Acceleration*Time*Time ) / 2
"""


"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""

"""
CODE CHALLENGES ( Take input from user in all the  code challenges ) 
Challenge 1
Challenge 2
Challenge 3
Challenge 4
Challenge 5
Challenge 6
Challenge 7
Challenge 8
Challenge 9
Challenge 10
"""








