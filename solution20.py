"""
# ex.20
Create a program that reads a number that you want to get the sum until that number and 
then calculate the averge of these numbers

Create a program that:
* Reads the number you want to sum
* Calculates the sum of 1+2+3+4...+98+99+n
* Calculates the average of the sum 1+2+3+4...+98+99+n
* Input example: 100
* Output: "The average is 50.5"
"""


def sum_avg_of_natural_numbers(last_number, n):
    sum = last_number* (1 + last_number) / 2
    avg = (sum + n)/2 
    return int(avg)

num = 99
x = 100
result = sum_avg_of_natural_numbers(num, x)
print(f"The average is {result}")