
"""
Types Of Errors
    Syntax Error
    Compile Time Errors
    Runtime Errors 
"""



"""
Introduce the concept of Exception Handling 
Try to  input a non integer number while input
try and except block gets executed when failed  
Introduce the else block, it gets executed when it does not throws error 
"""


try:
    pass

except Exception:
    pass

except Exception:
    pass

else:
    pass
    # it runs code when try block does not raise exception 

finally:
    pass
    # this gets executed every time whether exception was raised or no
    # releases resources , databases, 



# How to convert a simple code to handle exception handling 
    
my_age = int(input("Enter your age >"))

print ("Your age is {}".format(my_age))

print ("Program ended")

# On running the code with multiple different values we get ValueError Exception


try:
    my_age = int(input("Enter your age >"))

except Exception:
    print ("Non Integer value, try giving the age again ")

else:
    print ("Your age is {}".format(my_age)) 

finally :
    print ("Program ended")



# trying to catching multiple Exceptions 

try:
    my_age = int(input("Enter your age >"))

except ValueError :
    print ("Non Integer value, try giving the age again ")

except Exception as e:
    print (e)

else:
    print ("Your age is {}".format(my_age)) 

finally :
    print ("Program ended")




"""
you can use the raise Exception statement to raise your own exceptions 
in the try block 
"""

