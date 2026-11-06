# Testing the nested if-else statement
# This checks if the user input username and password matches with already set username and password and prints the result accordingly
username= input("enter your username: ") #asking the user to input their username
password=input("enter your password: ") #asking for password

if username=='admin': 
    if password=='admin@123': # usign nested if-else statement for testing multiple conditions
        print('access accepted')#runs if both password and username is correct
    else:
        print('access denied')#runs if the password only is wrong
else:
    print('your username or password is wrong')#runs if username or both is wrong
