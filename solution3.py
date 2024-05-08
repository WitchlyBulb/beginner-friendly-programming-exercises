""" ex.3
You've bought a Bitcoin and now it's on the rise!!!

Create a program that:
1) Reads the value of the bitcoin at the time of purchase
2) Reads the percentage of increase (or decrease)
3) Prints the total value of your bitcoin
4) Prints the increase or decrease value

* Example: bitcoin_value = 10000, bitcoin_increase = 10
* Output: total_bitcoin_value = 11000, bitcoin_increase_value = 1000
"""

def bitcoin_value(value_of_bitcoin_at_purchase, percentage_change, type_of_change):
    change_in_value = (percentage_change/100) * value_of_bitcoin_at_purchase
    if type_of_change == "increase":
        total_value_of_bitcoin = value_of_bitcoin_at_purchase + change_in_value
    else:
        total_value_of_bitcoin = value_of_bitcoin_at_purchase - change_in_value
    return total_value_of_bitcoin, change_in_value, type_of_change

bought_bitcoin_at = 20000
percentage_diff = 10
increase_or_decrease = "decrease"
x, y, z = bitcoin_value(bought_bitcoin_at, percentage_diff, increase_or_decrease)

print(f"The total value of your Bitcoin is ${x}")

print(f"The {z} in Bitcoin since last year is ${y}")
