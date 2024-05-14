"""
# ex.25
You start flipping a coin, count and print how many times the result was head or tails until you enter the word 
"stop". Then find and print the percentage of how many head or tails was the result.

Create a program that:
* Reads if the flipped coin was head or tails
* If the value is "stop", print proper message and quit program
* While value not "stop", count the result
* Print the proper message
* Calculates the percentage of head and tails
* Prints the proper message
* Input: "head", "tails", "tails", "tails", "head", "head", "tails", "tails", "tails", "head"
* Ouput: "Head won 4 times and tails won 6 times"
* Output: "40% Head, 60% Tails"
"""

def read_flip(flip_result_list):
    count_heads = 0
    count_tails = 0
    for item in flip_result_list:
        if item == "head":
            count_heads += 1
        elif item == "tails":
            count_tails += 1
        else:
            item == "stop"
            break
    total_flips = count_heads + count_tails
    percentage_heads = (count_heads/total_flips) * 100
    percentage_tails = (count_tails/total_flips) * 100
    return count_heads, count_tails, percentage_heads, percentage_tails, total_flips

list_flips = ["head", "tails", "tails", "tails", "head", "head", "tails", "tails", "tails", "head", "stop"]
heads, tails, perc_heads, perc_tails, total = read_flip(list_flips)
print(f"The coin flipping was stopped after {total} flips")
print(f"Head won {heads} times and tails won {tails} times")
print(f"{perc_heads}% Head, {perc_tails}% tails")

