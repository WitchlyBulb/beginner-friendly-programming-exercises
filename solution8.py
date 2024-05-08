"""ex.8
The exercise is almost identical to a previous exercise with a minor change. In a company the monthly salary of an employee is calculated by minimum wage
 400$ per month, plus 20$ multiply by the employment years, plus 30$ for each employee kid, plus 100$ if the employee didn't miss 1 day of work.

Create a program that:
* Reads the employment years
* Reads the number of each employee kids
* Prints the total amount the employee must take
* Output: "The total amount is 660$, 400$ minimum wage + 100$ for 5 years experience + 60$ for 2 kids + 100$ for not missing a day at work"
"""

def calculate_salary(years_employed, num_children, missed_days):
    minimum_wage = 400
    money_for_experience = years_employed * 20
    benefits_for_children = num_children * 30
    monthly_salary = minimum_wage + money_for_experience + benefits_for_children
    bonus = 100
    if missed_days == 0:
        monthly_salary += bonus
    return monthly_salary, money_for_experience, benefits_for_children

years = 20
children = 3
holidays = 0
s, y, c = calculate_salary(years, children, holidays)
if holidays == 0:
    print(f"The total amount is ${s}. 400$ minimum wage + {y}$ for 20 years experience + {c}$ for 3 kids + $100 for not missing a day at work")
else:
    print(f"The total amount is ${s}. 400$ minimum wage + {y}$ for 20 years experience + {c}$ for 3 kids")
