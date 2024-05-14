"""
# ex.26
-Create a program that read values of apartments you want to rent until the inpute value is 0 or 
a negative number.
-You will calculate the average price for rent and how many apartments you've registered. Print 
the proper message.
-Then compare values of apartments you want to rent with the avarage price of the apartments 
you've registered until you enter 0 or a negative value.
-If the price is above average price print the proper message, else if the price is below average
 print the proper message. If the input value is 0 or a negative number, print the proper message and exit.

Create a program that:
* Reads values until user inputs 0 or a negative value
* Calculates the average price
* Counts how many apartments registered
* Prints the average price and how many apartments registered
* Reads prices and compare with the average price and print proper message
* Input: 234, 764, 123, 654
* Output: "4 apartments have registed. The average price for rent is 443.75$"
* Input: 500, 200, 350, 450, 0, -7
* Output: "Above average price", "Above below price", "Above below price", "Above average price", "Quit Program","Quit Program"
"""

def apartment_values_list(list_values):
    total_apartment_rent = 0
    rents_greater_than_zero = 0
    number_of_registered_apts = len(list_values)
    list_info_on_rents = []
    for value in list_values:
        if value != 0 and value > 0:
            total_apartment_rent += value
            rents_greater_than_zero += 1
            avg_rent = total_apartment_rent/rents_greater_than_zero
        else:
            break
    for value in list_values:
        if value > avg_rent:
            response = "Above average price"
        elif value < avg_rent and value > 0:
            response = "Below average price"
        else:
            response = "Quit Program"
        list_info_on_rents.append(response)

    return number_of_registered_apts, avg_rent, list_info_on_rents

list_apts = [500, 200, 350, 450, 0, -7]
number, average, info = apartment_values_list(list_apts)
print(f"{number} apartments have registed. The average price for rent is {average}$")
print(info)
      


