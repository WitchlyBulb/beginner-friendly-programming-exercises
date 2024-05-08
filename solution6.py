"""You are interested in buying a new laptop. You check the price and you see that the price is 300$ without the 10% tax.

Create a program that:
1) Reads the price of the laptop
2) Reads the tax percentage
3) Prints the total amount

* Output: "The total price of the laptop is 330$"  """

def calculate_total(price_of_laptop, tax_percent):
    tax_value = (tax_percent/100) * price_of_laptop
    total_value = price_of_laptop + tax_value
    return total_value

laptop = 1000
tax = 6.5
total = calculate_total(laptop, tax)
print("The total price of the laptop is ",total)
