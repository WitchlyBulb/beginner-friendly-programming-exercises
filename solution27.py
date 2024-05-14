"""
# ex.27
Create a program that register a user with a username and a password. Then the user will try to login with the login 
credentials. If the user make 3 wrong attempts exit program with proper message.

Create a program that:
* Reads the username and the password
* Then the user try to login
* If the user makes 3 wrong attempts exit with proper message
"""

def login_info(username, password):
    dict_login_info = {}
    dict_login_info[username] = password
    return dict_login_info

ask_username = input("Enter your username: ")
ask_password = input("Enter your password: ")
info_client_dict = login_info(ask_username, ask_password)

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    ask_username_again = input("Enter your username: ")
    ask_password_again = input("Enter your password: ")
     
    if ask_username_again in info_client_dict and info_client_dict[ask_username_again] == ask_password_again:
        print("Welcome back")
        break
    else:
        print("Try again")
        attempts += 1
        

else: 
    print("Sorry, your login failed")
    exit()
    