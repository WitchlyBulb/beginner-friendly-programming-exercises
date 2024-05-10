"""
# ex.17
Create a program that:
* Calculates the sum of 1+2+3+4...+98+99
* Prints the sum of 1+2+3+4...+98+99
* Output: "The sum is 4950"
"""

def sum_of_natural_numbers(last_number):
    sum = last_number* (1 + last_number) / 2
    return int(sum)

num = 99
result = sum_of_natural_numbers(num)
print(f"The sum is {result}")
