#Mini project :
#Problem Statement : Password Generator
#Make a program to generate a strong password using the input given by the user.
#To generate a password, randomly take some words from the user input and then
#include numbers, special characters and capital letters to generate the password.
#Also, keep a check that password length is more than 8 characters.
#Note: Include Exception handling wherever required. Also, make a ‘User’ class
#and store the details like user id, name and password of each user as a tuple.

import random

class User:
    def save_data(self, user_id, name, password):
        self.data = (user_id, name, password)

print("*****Password Generator******")

try:
    u_id = input("Enter ID : ")
    name = input("Enter Name : ")
    password = input("Enter word hint for generating a password : ")

    if len(password) == 0:
        print("Password cannot be empty")
    else:
        password_list = list(password)
        password_list.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        password_list.append(random.choice("0123456789"))
        password_list.append(random.choice("@#%$&*"))

        while len(password_list) < 8:
            password_list.append(random.choice("abcdefghijklmnopqrstuvwxyz"))

        random.shuffle(password_list)
        password = ""
        for i in password_list:
            password += i

        obj = User() 
        obj.save_data(u_id, name, password)
        print("Your strong password is : ",password)
        print("User Detail : ", obj.data)

except Exception as e:
    print("Error:", e)