"""# ex.14
You want to buy something from Amazon. The seller charges different prices for shipping cost based on location.
 For US it's 5$, for Europe it's 7$, for Canada it's 3$, for other places it's 9$

Create a program that:
* Reads the cost of the product
* Reads your location
* Print the amount of money you have to pay
* Ouput: "You have to pay 23$, 20$ for the product and 3$ for shipping cost"
"""


def total_cost(item_cost, location):
    if location == "US":
        shipping_fee = "$5"
        total_due = item_cost + 5
    elif location == "Europe":
        shipping_fee = "$7"
        total_due = item_cost + 7
    elif location == "Canada":
        shipping_fee = "$3"
        total_due = item_cost + 3
    else:
        shipping_fee = "$9"
        total_due = item_cost + 9
    return total_due, shipping_fee

item_costs = 10
place = "US"
pay, shipping = total_cost(item_costs, place)
print(f"You have to pay ${pay}, {item_costs}$ for the product and {shipping} for shipping cost")


    