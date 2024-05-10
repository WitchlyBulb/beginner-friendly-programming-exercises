"""
# ex.16
A fast food chain has these meals

| Meal | Price  |
|---------|--------------|
| Burger | 5$ |
| Pizza | 3$ |
| Hot Dog | 1,5$ |

Create a program that:
* Reads the meal the customer wants
* Prints the cost of the meal
* Input example: "Hot Dog"
* Output: "Hot Dog 1,50$"
"""

#Solution using dictionary:

def menu_price(menu_dict, meal_item):
    if meal_item in menu_dict.keys():
        return meal_item, menu_dict[meal_item]
    else:
        return("This item is not in the menu")

dict_meals = {"Burger": "5$","Pizza": "3$", "Hot Dog": "1.50$"}
food = "Caterpillar"

cost = menu_price(dict_meals, food)
print(cost)
