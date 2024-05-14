"""
# ex.28
Create a program that asks the user for seconds(integers values) and then start printing the countdown, 
when the countdown ends print Go!. If the user enters a non integer value, exit the program with proper message.

Create a program that:
* Reads integers until user enters a non integer value.
* Print the countdown and at the end print Go!
* Input: 3, -7
* Output: 3, 2, 1, Go! - Exit Program
"""

def input_seconds(list1):
    output_list = []
    for i in list1:
        if type(i) == int:
            output_list.append(i)
        else:
            output_list.append("Go")
            break
    return output_list
    
input_list = [3, 5, 7, 0, -3, 3.4, "sally", 6, 9]
result = input_seconds(input_list)
print(result)

