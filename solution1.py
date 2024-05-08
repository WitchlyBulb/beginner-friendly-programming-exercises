"""ex.1
Create two variables a and b, and initially set them each to a different number. 
Write a program that swaps both values."""

def input_variables(a, b):
    temporary_c = a                #assign the value of a to the temporary variable c
    a = b                          #assign the value of b to a, now a has b's value
    b = temporary_c                #now b has a's original value
    return (a, b)

x = 7
y = 8
result = input_variables(x, y)
print("The swapped values are", result)
