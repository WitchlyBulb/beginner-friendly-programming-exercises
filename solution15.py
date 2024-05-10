"""
# ex.15
A cell phone company has the following billing policy

|  | Fixed cost 25$  |
|---------|--------------|
| Call duration(in seconds)| Charge($/per second)|
| 1-500 | 0,01 |
| 501-800 | 0,008 |
| 801+ | 0,005 |

Create a program that:
* Reads how many seconds was the calls duration
* Calculates the monthly bill for the subscriber
* Prints the total amount
* Output: "total amount: 48$"

#### Notice that that the charge for the first 500 seconds it's 0,01$ then for the next 501 to 800 seconds
 it's 0,008 and then it's 0,005$
 """

def calculate_montly_bill (calls_duration):
    fixed_cost = 25
    if calls_duration == 0:
        bill = fixed_cost
    elif calls_duration in range(1, 500):
        bill = (calls_duration * 0.01) + fixed_cost
    elif calls_duration in range(501, 800):
        diff1 = calls_duration - 500            #where diff1 represents the next tier 501-800 sec
        bill = (diff1 * 0.008) + (500 * 0.01) + fixed_cost
    else:
        diff2 = calls_duration - 800
        bill = (diff2 * 0.005) + (300 * 0.008) + (500 * 0.01) + fixed_cost
    return bill

seconds_duration = 800
amount = calculate_montly_bill (seconds_duration)
print(f"Total amount {amount}")




