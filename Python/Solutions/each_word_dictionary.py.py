"""
Let’s start with a very simple file of words taken from the text of Romeo and 
Juliet. (romeo.txt)

We will write a Python program to read through the lines of the file, break 
each line into a list of words, and then loop through each of the words in 
the line, and count each word using a dictionary.

file_name - 'each_word_dictionary.py'

"""

my_file = open('romeo.txt','r')

read_file = my_file.readlines()

my_dictionary = {}

for i in range(len(read_file)):
    splitted_list = read_file[i].split(' ')
    for i in splitted_list:
        i = i.replace('\n', '')
        if i in my_dictionary.keys():
            my_dictionary[i] = my_dictionary[i]+1
        else:
            my_dictionary[i] = 1

print (my_dictionary)