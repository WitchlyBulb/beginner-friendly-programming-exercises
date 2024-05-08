"""
ex.11
You have started working and you are wondering how many things you can buy with the money 
you've earned. A PS4 costs 200$, a Samsung phone 900$, a TV 500$, a game skin 9.99$

Create a program:
* Notice that you can't but half TV or 1/4 of PS4.
* Reads how many hours you've worked
* Reads your hourly income
* Prints how many items you can buy
* Output: "I can buy 4 PS4, 1 Samsung, 3 TV, 80 game skin"
"""

def calculate_income(hours_worked, hourly_pay):
    money_earned = hours_worked * hourly_pay
    number_PS4 = money_earned // 200
    number_phone = money_earned // 900
    number_TV = money_earned // 500
    number_gameskin = money_earned // 9.99
    return number_PS4, number_phone, number_TV, number_gameskin

hours = 40
pay_per_hour = 100
ps4, ph, tv, gs = calculate_income(hours, pay_per_hour)
print(f"I can buy {ps4} PS4, {ph} Samsung phones, {tv}TVs and {gs} game skins")

