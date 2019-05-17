# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:40:37 2019

@author: dell
"""

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file 
"""

with open("words.txt", "rt") as file:
    file_txt = file.read()

with open("copy.txt", "wt") as copy:
    copy.write(file_txt)
    
with open("copy.txt", "rt") as copy1:
    print(copy1.read())

# OR
    
with open("words.txt", "rt") as file_new:
    with open("new_copy.txt", "wt") as copy_new:
        for i in file_new:
            copy_new.write(i)
with open("new_copy.txt", "rt") as new:
    print(new.read())
    
    
"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
n=0
while n<=25:
    n+=1
    user = input("Enter absentee's names : ")
    if not user:
        break
    with open("absentee.txt", "at") as absent:
        absent.write(user+'\n')
with open("absentee.txt", "rt") as file:
    print(file.readlines())
    
"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    Read the zoo.csv file using readlines and Print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    Print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    Print the total number of water needed by all the animals    
"""

# Read the zoo.csv file using readlines and Print them
import csv
def func_read():
    with open("zoo.csv", "rt") as read:
        csv_read = read.readlines()
        print(csv_read)
func_read()

# Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
def animal():
    list1 = []
    with open("zoo.csv") as anim:
        file_read = csv.reader(anim, delimiter = ",")
        next(file_read)
        for i in file_read:
            if i[0] not in list1:
                list1.append(i[0])
        print(list1)
animal()

# Print the total number of water need by elephant / tiger / lion / zebra / kangaroo
def total_each():
    water_need_elephant = 0
    water_need_tiger = 0
    water_need_zebra = 0
    water_need_lion = 0
    water_need_kangaroo = 0
    with open("zoo.csv") as water:
        water_read = csv.reader(water, delimiter = ",")
        next(water_read)
        for i in water_read:
            if i[0]=="elephant":
                water_need_elephant = int(i[2])+ water_need_elephant
            elif i[0]=="tiger":
                water_need_tiger= int(i[2])+ water_need_tiger
            elif i[0]=="zebra":
                water_need_zebra = int(i[2])+ water_need_zebra
            elif i[0]=="lion":
                water_need_lion = int(i[2])+ water_need_lion
            elif i[0]=="kangaroo":
                water_need_kangaroo = int(i[2])+ water_need_kangaroo
    print("ELEPHANT : {}".format(water_need_elephant))
    print("TIGER : {}".format(water_need_tiger))
    print("ZEBRA : {}".format(water_need_zebra))
    print("LION : {}".format(water_need_lion))
    print("KANGAROO : {}".format(water_need_kangaroo))
total_each()

# Print the total number of water needed by all the animals    
def total():
    total_water_needed = 0
    with open("zoo.csv") as summ:
        read_add = csv.reader(summ, delimiter = ",")
        next(read_add)
        for j in read_add:
            total_water_needed += int(j[2])
    print("Total water needed by all the animals is {}".format(total_water_needed))
total()
    
"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""

with open("romeo.txt", "rt") as romeo:
    for i in romeo:
        read_txt = romeo.readline()
        print(read_txt)









