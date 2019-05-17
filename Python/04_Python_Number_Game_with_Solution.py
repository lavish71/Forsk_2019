
# Interactive Guess the Number Game 

"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
    Then ask you ( Player ) to guess the number and store as guess number

    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""

import random 

secret_number = random.randint(1,10)

guess = int(input(" Guess a number between 1 and 10 > ") )

if ( guess == secret_number ) :
    print ( " Player Wins and Computer Loses " )
else :
    print ( " Player Loses and Computer Wins " )



"""
Challenge 2
    Print the secret number and guess number when Player loses using format function 
"""


import random 

secret_number = random.randint(1,10)

guess = int(input(" Guess a number between 1 and 10 > ") )

if ( guess == secret_number ) :
    print ( " Player Wins and Computer Loses " )
else :
    print ( " Player Loses and Computer Wins " )
    print ( " Player guessed {} number but Computer secret is {}".format (guess, secret_number) )




"""
Challenge 3
    Print too HIGH or too LOW messages for bad guesses using elif. 
"""


import random 

secret_number = random.randint(1,10)

guess = int(input(" Guess a number between 1 and 10 > ") )

if ( guess == secret_number ) :
    print ( " Player Wins and Computer Loses " )    
else :
    print ( " Player Loses and Computer Wins " )
    
    if (guess < secret_number ) :
        print ( " Player guessed LOW" ) 
    elif (guess > secret_number ) :
        print ( " Player guessed HIGH" ) 
    


"""
Challenge 4
    Let people play again and again until he guesses the right secret number
"""

import random 

secret_number = random.randint(1,10)

while (True):
    
    guess = int(input(" Guess a number between 1 and 10 > ") )

    if ( guess == secret_number ) :
        print ( " Player Wins and Computer Loses " )  
        break
    else :
        print ( " Player Loses and Computer Wins " )
    
        if (guess < secret_number ) :
            print ( " Player guessed LOW" ) 
        elif (guess > secret_number ) : 
            print ( " Player guessed HIGH" ) 


"""
Challenge 5
Limit the number of guesses to maximum 6 tries 
"""

import random 

secret_number = random.randint(1,10)
guesses = 0 
max_tries = 6

while (guesses < max_tries):
    
    guess = int(input(" Guess a number between 1 and 10 > ") )

    if ( guess == secret_number ) :
        print ( " Player Wins and Computer Loses " )  
        break
    else :
        guesses+=1
        print ( " Player Loses and Computer Wins " )
    
        if (guess < secret_number ) :
            print ( " Player guessed LOW" ) 
        elif (guess > secret_number ) : 
            print ( " Player guessed HIGH" ) 

"""
Challenge 6
    Print the number of tries left 
"""


import random 

secret_number = random.randint(1,10)
guesses = 0 
max_tries = 6

while (guesses < max_tries):
    
    guess = int(input(" Guess a number between 1 and 10 > ") )

    if ( guess == secret_number ) :
        print ( " Player Wins and Computer Loses " )  
        break
    else :
        guesses+=1
        print ( " Player Loses and Computer Wins " )
        print ( " Player has {} tries left ".format(max_tries - guesses) ) 
        if (guess < secret_number ) :
            print ( " Player guessed LOW" ) 
        elif (guess > secret_number ) : 
            print ( " Player guessed HIGH" ) 

"""
Challenge 7
    Lets give user the option to play again
"""

"""
Challenge 8
    Catch when someone submits a non integer
"""




