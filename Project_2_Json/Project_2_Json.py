# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:32:06 2019

@author: dell
"""

"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Email (can be Multiple)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""

import json

json_string = """{
	"students": [{
			"student_1": {
				"fname": "lavish",
				"lname": "sharma",
				"phone no.": {
					"phone_1": "7231055855",
					"phone_2": "9828293125"
				},
				"faculty": {
					"department": "ML&AI",
					"research_areas": {
						"area_1": "kota",
						"area_2": "jaipur"
					}
				}
			}
		},
		{
			"student_2": {
				"fname": "ashwani",
				"lname": "dhankhar",
				"phone no.": {
					"phone_1": "9210130040",
					"phone_2": "9310130040"
				},
				"faculty": {
					"department": "ML&AI",
					"research_areas": {
						"area_1": "paris",
						"area_2": "jaipur"
					}
				}
			}
		},
		{
			"student_3": {
				"fname": "dushyant",
				"lname": "khichi",
				"phone no.": {
					"phone_1": "9546210351",
					"phone_2": "8452169575"
				},
				"faculty": {
					"department": "ML&AI",
					"research_areas": {
						"area_1": "london",
						"area_2": "mexico"
					}
				}
			}
		}
	]
}"""
    
print (type(json_string))

# Converts JSON Data types to Python Data Types 
my_data = json.loads(json_string)

print (type(my_data))  # its a python dictionary  , it uses the table to convert 

print (my_data)

print (my_data['students'])

print (my_data['students'][0])

print (my_data['students'][0]['student_1'])

print (my_data['students'][2]['student_3']['phone no.']['phone_2'])


# Converts Python Data types to JSON Data Types
new_json_string = json.dumps(my_data)
print (type(new_json_string) )
print (new_json_string) 

new_json_string = json.dumps(my_data, indent=2 )
print (new_json_string) 

new_json_string = json.dumps(my_data, indent=2, sort_keys=True)
print (new_json_string)


# Writing/Storing the JSON data in a File 
with open("data_file.json", "w") as write_file:
    json.dump(json_string, write_file)


# Reading from a JSON file
with open("data_file.json", "r") as write_file:
    jsondata=json.load(write_file)
    print(jsondata)
 
    # JSON in python data structure 
    my_data = json.loads(jsondata)
    print (my_data)





