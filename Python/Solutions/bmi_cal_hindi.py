"""
Code Challenge
  Name: 
    BMI in Hindi
  Filename: 
    bmi_cal_hindi.py
  Problem Statement:
    Convert the BMI program to use hindi titles while taking input and print weight, 
    height and BMI in Hindi script using formatted strings concept   
  Hint: 
     Create a copy of the old bmi_cal.py program and do modification
"""

# Take weight from user
weight = float(input(u"\u0915\u093F\u0932\u094B\u0917\u094D\u0930\u093E\u092E \u092E\u0947\u0902 \u0905\u092A\u0928\u093E \u0935\u091C\u0928 \u0926\u0930\u094D\u091C \u0915\u0930\u0947\u0902"+" >"))


# Take height from user
height = float(input(u"\u092E\u0940\u091F\u0930 \u092E\u0947\u0902 \u0905\u092A\u0928\u0940 \u090A\u0902\u091A\u093E\u0908 \u0926\u0930\u094D\u091C \u0915\u0930\u0947\u0902"+" >"))


# BMI Formula
BMI_value = (weight/height)/height

weight_hindi = u"\u0935"+u"\u091C"+u"\u0928"

height_hindi = u"\u090A"+u"\u0901"+u"\u091A"+u"\u093E"+u"\u0908"

BMI_hindi = u'\u0936\u0930\u0940\u0930 \u0915\u0947 \u0926\u094D\u0930\u0935\u094D\u092F\u092E\u093E\u0928 \u0915\u0940 \u0938\u0942\u091A\u0940'

print (weight_hindi+" : "+str(weight))

print (height_hindi+" : "+str(height))

print (BMI_hindi+" : "+str(round(BMI_value,2)))