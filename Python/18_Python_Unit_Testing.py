import math

def is_prime(n):
  """Determine if a non-negative integer is prime"""
  if n < 2 :
    return False

  # OFF BY ONE Error, solution is to add +1  
  for i in range (2, int(math.sqrt(n)) + 1 ):
    if n % i == 0 :
      return False
  return False



"""
# create a file prime.py 


open the python interpreter 

>>> from prime import is_prime
>>> is_prime(23)
True
>>> is_prime(28)
False
>>> is_prime(25)
True

# there seems to be a bug since 25 is not prime

# this is not the right way to test the function manually

# Create a external file test0.py to test the function is_prime from file prime.py

# Another way could be to create a bash script file to test it, test0.sh

# run using command ./test0.sh

# this would give 2 cases where it failed 
is_prime(8)
is_prime(25)

# fix the code in prime.py for the OFF BY ONE Error 

# We need ot make good comrehensive test cases to PASS or FAIl our test

# Python inbuilt has a ASSERT command 
# takes expression and assert if it is TRUE or thown an Error

>>>assert True
Nothing happens

>>>assert False
Breaks and gives a AssertError

# create a file assert0.py

python assert0.py
Nothing happends 

make assert square(10) == 101

Now u run it gives AssertError


# to find the exit code use echo $? on prompt

# Intorduce the concept of exit code
# If there is an error, then there is a non zero exit code of 1
# If there is no error, then there is a exit code of 0


# Python gives some tools to testing 
# Unittest 

# create test1.py

# Now run test1.py
python test1.py

it runs 6 tests and gives OK

# now again make the prime.py buggy and try runnit the test1.py


"""

"""
#test0.py

from prime import is_prime

def test_prime(n,expected):
  if is_prime(n) != expected :
    print(f"ERROR on is_prime{n}, expected {expected}")


#test0.sh
python3 -c "from test0 import test_prime; test_prime(1,False)"
python3 -c "from test0 import test_prime; test_prime(2,True)"
python3 -c "from test0 import test_prime; test_prime(8,False)"
python3 -c "from test0 import test_prime; test_prime(11,True)"
python3 -c "from test0 import test_prime; test_prime(25,False)"
python3 -c "from test0 import test_prime; test_prime(28,False)"


#assert0.py

def square (x):
  return x*x


assert square(10) == 100


"""

# test1.py

import unittest

from prime import is_prime

class Tests ( unittest.TestCase):
  def test_1(self):
    """Check that 1 is not prime. """
    self.assertFalse(is_prime(1))

  def test_2(self):
    """Check that 2 is prime. """
    self.assertTrue(is_prime(2))

  def test_8(self):
    """Check that 8 is not prime. """
    self.assertFalse(is_prime(8))

  def test_11(self):
    """Check that 11 is prime. """
    self.assertTrue(is_prime(11))

  def test_25(self):
    """Check that 25 is not prime. """
    self.assertFalse(is_prime(25))

  def test_28(self):
    """Check that 28 is not prime. """
    self.assertFalse(is_prime(28))


if __name__ == "__main__":
  unittest.main()

  

# Convert above using the test_calc.py 
# How to run the test from command line
# python -m unittest test_calc.py
# or
# python test_calc.py 
# this should call the __main__ function of the code 
  


# Other Unit Test Methods 
  
# docs.python.org/3/library/unittest.html#unitTest.TestCase.debug
# Class needs to be inherited from TestCase class and the method to be defined starting with test_

"""
assertEquals(a,b)
assertNotEquals(a,b)
assertTrue(x)
assertFalse(x)
assertIs(a,b)
assertIsNot(a,b)
assertIsNone(x)
assertIsNotNone(x)
assertIn(a,b)
assertNotIn(a,b)
assertIsInstance(a,b)
assertNotIsInstance(a,b)
"""


# Introduce the browser testing tools

# Selinium
from selinium import webdriver

driver = webdriver.Chrome()

from tests import file_uri

uri = file_uri("counter.html")
# Counter.html has a java script code two buttons of + and - for inc and dec
 
driver.get(uri)
plus = driver.find_element_by_id("increase")
plus.click()

# test_selenium.py

def test_title(self):
    driver.get(file_uri("counter.html"))
    self.assertEqual(driver.title,"Counter")
    
    increase = driver.find_element_by_id("increase")
    increase.click()
    self.assertEqual(driver.find_element_by_tag_name("h1").text,"1")
    
    decrease = driver.find_element_by_id("decrease")
    decrease.click()
    self.assertEqual(driver.find_element_by_tag_name("h1").text,"-1")
    
    

# Convert this into a code challenege and it solution 


# Unit Testing your code with unittest module 

# calc.py


def add ( x, y ) :
    """ Add Function """
    return x + y

def subtract ( x , y ) :
    """ Subtract Function """
    return x - y 

def multiply ( x , y ) :
    """ Multiply Function """
    return x * y 

def divide ( x , y ) :
    """ Divide Function """
    if y == 0 :
        raise ValueError ("Cannot divide by zero !" )
    return x / y 




"""
Write test 
Tear down your test 
Best Practices for Unit Testing 

Large projects have unit test 
You need to know how to write test 
 

At present we all test our code using the print statement and printing the return of the value of the function    
"""




# test_calc.py  is the unit testing file should be in the same directory as calc.py 

# import the testing module 
import unittest 

# import the module which needs to be tested 
import calc


class TestCalc ( unittest.TestCase ) :
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result,15)


# How to run the test from command line
# python -m unittest test_calc.py
# or
# python test_calc.py 
# this should call the __main__ function of the code 


# What happens when the test fails 
# self.assertEqual(result,14)

