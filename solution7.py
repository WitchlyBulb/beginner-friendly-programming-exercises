
""" ex.7
In a company the monthly salary of an employee is calculated by: the minimum wage 400$ per month, plus 20$ multiplied 
by the number of years employed, plus 30$ for each child they have.

Create a program that:
1) Reads the number of years employed
2) Reads the number of children the employee has
3) Prints the total amount of salary the employee makes

* Output: "The total amount is 560$. 400$ minimum wage + 100$ for 5 years experience + 60$ for 2 kids"  """

def calculate_salary(years_employed, num_children):
    minimum_wage = 400
    money_for_experience = years_employed * 20
    benefits_for_children = num_children * 30
    monthly_salary = minimum_wage + money_for_experience + benefits_for_children
    return monthly_salary, money_for_experience, benefits_for_children

years = 20
children = 3
s, y, c = calculate_salary(years, children)
print(f"The total amount is ${s}. 400$ minimum wage + {y}$ for 20 years experience + {c}$ for 3 kids")


