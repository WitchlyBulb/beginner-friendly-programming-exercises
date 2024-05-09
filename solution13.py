"""# ex.13
An internet cafe has 2 ways of charging. If the user is a member pays 2$/hour, Else the user pays 5$. Find if someone is a member or not 
and calculate the price based on how many hours the user spend. If the user is a member the tax is 10% else the tax is 20%.

Create a program that:
* Reads how many hours the user spend
* Check if is a member
* Add the proper tax fee
* Print the total amount the user has to pay
* Output: "The user is a member stayed 2 hours for 2$/hour plus the 10% the total amount is 4.4$"
"""

def calculate_payment (hours_used, membership):
    if membership == "yes":
        basic_payment = hours_used * 2      #hours spent * $2 for member
        total_payment = basic_payment * 1.1 #basic payment + 10% tax for member
        total_payment = round(total_payment, 2)
        description = "member"
        rate = "$2/hour"
        tax = "10%"
    else:
        basic_payment = hours_used * 5      #hours spent * $5 for non-member
        total_payment = basic_payment * 1.2  #basic payment + 20% tax for non-member
        total_payment = round(total_payment, 2)
        description = "non-member"
        rate = "$5/hour"
        tax = "20%"
    return total_payment, description, rate, tax


member = "no"
hours = 10 
money_owed, desc, hourly_rate, taxes = calculate_payment (hours, member)
print(f"The user is a {desc} and stayed {hours} hours for {hourly_rate} plus the {taxes} the total amount is {money_owed}")
