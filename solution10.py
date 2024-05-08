"""ex.10
Create a program that prints the last digit of a given integer

Create a program that:
1) Reads the integer
2) Prints the last digit
Warning! Do not use the programming language MAGIC. After you complete the exercise feel free to do so.
Warning! Don't try to convert the number into string etc.
Warning! For this problem it's ok after spending some time to look for the solution."""


number = int(input("enter any integer: "))

if number in range(0, 9):
    print (number)
elif number > 9:
    while number >9:
        number = number - 10
    print (number)
else:
    while number <-10:
        number = number + 10
        number *= -1    
        print (number)

