"""
# ex.23
Create a program that reads numbers and sum them until the user inputs a negative value

Create a program that:
* Reads numbers
* Sum them
* Prints the sum
* Input example: 5, 9, 3, 0, 2, 0, 4, -7
* Output: "The sum is 23"
"""


def add_until_negative(list1):
    sum = 0
    for num in list1:
        if num < 0:
            break
        sum += num  
    return sum

list_of_given_numbers = [5, 9, 3, 0, 2, 0, 4, -7]
result = add_until_negative(list_of_given_numbers)
print(result)
