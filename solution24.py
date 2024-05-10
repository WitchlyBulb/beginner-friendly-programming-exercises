"""
# ex.24
Create a program that reads numbers and sum them until the user inputs a negative value or zero value

Create a program that:
* Reads numbers
* Sum them
* Prints the sum
* Input example: 5, 9, 3, 7, 0
* Output: "The sum is 24"
"""

def sum_of_given_numbers(list_numbers):
    sum = 0
    for num in list_numbers:
        if num <= 0:
            break
        sum += num
    return sum

given_numbers = [1, 5, 5.8, 9, 0, -3, -5, 8]
result = sum_of_given_numbers(given_numbers)
print(result)
