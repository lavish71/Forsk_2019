# Logging 

"""
Six Log Levels Available ascending 
    DEBUG 
        Detailed information, typically of interest only when diagnosing problems 
    INFO
        Confirmation that things are working as expected
    WARNING
        An indication that something unexpected happened, but the s/w is still working as expected
    ERROR
        Due to some serious problem, the s/w has not been able to perform some functions 
    CRITICAL
        A serious error, indicating that the program itself may be unable to continue running 
    NOTSET
"""

# Default logging level is WARNING 
import logging 
logging.basicConfig ( level = logging.DEBUG )
logging.debug()

# To log things directly the console 
# This will not get printed on the console
logging.info ("You won’t see this ")
logging.warn("oh NO")


# Storing the logs in some files 
logging.basicConfig ( filename = 'game.log', level = logging.DEBUG )
logging.info("Monster {} door {} and player {} ". format (monster,door,player)
 

# Advance logging - LogRecord Attribute
# logging.basicConfig ( format = '%(asctime)s:%(levelname)s:%(message)s' )

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

import logging
logging.basicConfig ( level = logging.DEBUG )
logging.basicConfig ( filename = 'game.log', level = logging.DEBUG )
logging.basicConfig ( format = '%(asctime)s:%(levelname)s:%(message)s')


logging.debug("This is a debugging message")
logging.info("This is an information message")
logging.warn("This is a warning mesage")
logging.error("This is an error message")
logging.critical("This is a critical message")


# Python Debugger ( pdb )

"""
Track the state of variables at any given time 
Keeping track of the index while you are working with the list 
Alternative is to always log the value of the index 

Can we get inside of the script when it is running
Can we control the statements which needs to be executed 
 
"""
my_list = [ 5,2,1,True, “abcdefg”,3,False,4]

# Code to modify the list to have only numbers 
del my_list [ 3 ]
del my_list [ 4 ]
del my_list [ 6 ]

print (my_list)

import pdb

pdb.set_trace ()
del my_list [ 3 ]
del my_list [ 4 ]
del my_list [ 6 ]

print (my_list)

"""
You will get a new (pdb) prompt 
This is the next line which it is going to run 

you can print the value of my_print 

to run the next line n or next 
to quit the pdb type q or quit 
to continue the pdb type c or continue , 
it will run like it is running without at pdb


again check on my_list

change the script in live coding  

to quit the pdb type q or quit 

now go and change the code to del the right indexes  


once you have fixed the code, you need to remove the line pdb.set_trace ()

import pdb; pdb.set_trace ()  # semi colon can be used for multiple statements 

"""