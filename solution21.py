"""
# ex.21
Create a program that reads 5 numbers and find the average of these numbers

Create a program that:
* Reads the 5 numbers you want
* Calculates the average of these numbers
* Input example: 4, 6, 1, 4, 9
* Ouput: "the average is 4.8"
"""

def list_of_numbers(list1):
    sum_list1 = sum(list1)
    length = len(list1)
    avg = sum_list1/length
    return int(avg)

list2 = [1, 2, 3, 4, 5]
average = list_of_numbers(list2)
print("The average is", average)
