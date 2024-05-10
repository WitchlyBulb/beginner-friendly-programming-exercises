"""
# ex.18
* Calculates the sum of 1+3+5+7...+99+101
* Prints the sum of 1+3+5+7...+99+101
* Output: "The sum is 2601"
"""

def arithmetic_series(first_term, last_term, difference):
    number_term = (last_term - first_term)/difference + 1
    sum = (number_term)/2 * (first_term + last_term)
    return int(sum)

a = 1
an = 101
d = 2
result = arithmetic_series(a, an, d)
print(f"The sum is {result}")