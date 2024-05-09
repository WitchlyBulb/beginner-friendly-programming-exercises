"""# ex.12
You've consumed X amount of Mbps on Wikipedia and Y amount of Mbps on memes. The cost of visiting Wikipedia is 0,10$ per Mb
and the cost for watching memes is 0,05$ per Mb. If total consumption  is more than 100$ print "Too much consumption".
If watching meme consumption is greater than reading wikipedia consumption print "WOW MANY MEMES", "SUCH LOL"(in new line).

Create a program that:
* Reads X(wikipedia Mb consupmtion) and Y(watching meme Mb consumption)
* Calculates the total consumption
* If total consumption greater than 100$ print proper message
* If watching meme consumption  is greater than reading wikipedia articles print proper messages

Warning! For the greater meme consumption you will use one print statement and the output must be in seperate lines
"""

def calculate_consumption(X_wikipedia, Y_memes, time_in_sec_wiki, time_in_sec_memes):
    consumption_wiki = (X_wikipedia/0.10) * time_in_sec_wiki
    consumption_memes = (Y_memes/0.05) * time_in_sec_memes
    total_consumption = consumption_wiki + consumption_memes
    if total_consumption > 100:
        print("Too much consumption")
    if consumption_memes > consumption_wiki:
        print("WOW MANY MEMES\nSUCH LOL")
    return consumption_wiki, consumption_memes, total_consumption




X = 400
Y = 300
time_wiki = 60
time_memes = 50
wiki, meme, con = calculate_consumption(X, Y, time_wiki, time_memes)
print(f"The cost of your wikipedia usage is {wiki} and the cost of your memes usage is {meme} your total consumption is {con}")



