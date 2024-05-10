"""
# ex.22
Create a program that reads 5 numbers and prints if the number is negative or positive

Create a program that:
* Reads the 5 numbers you want
* Print if a number is negative or positive
* Input example: 4, 6, -11, -4, 9
* Ouput: "Positive", "Positive", "Negative", "Negative", "Positive",
"""

def sign_of_number(list1):
    for num in list1:
        if num > 0:
            x = print ("Positive")
        elif num < 0:
            x = print ("Negative")
        else:
            x = print ("Zero")
    
        
list2 = [-2, 4, 5, 0, -5.9]
number_sign = sign_of_number(list2)


