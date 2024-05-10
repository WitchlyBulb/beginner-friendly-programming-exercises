"""
# ex.19
Create a program that reads a number that you want to get the sum until that number

Create a program that:
* Reads the number you want to sum
* Calculates the sum of 1+2+3+4...+98+99+n
* Prints the sum of 1+2+3+4...+98+99+n
* Input example: 100
* Output: "The sum is 5050"

###### Try the program with a very very big number, [if it takes too long check this 
out](http://mathcentral.uregina.ca/qq/database/qq.02.06/jo1.html)
"""
from timeit import default_timer as timer

start = timer()
def sum_of_natural_numbers(last_number):
    sum = last_number* (1 + last_number) / 2
    return int(sum)

num = 2000000202020202020202020202
result = sum_of_natural_numbers(num)
print(f"The sum is {result}")
stop = timer()
print(stop-start)

