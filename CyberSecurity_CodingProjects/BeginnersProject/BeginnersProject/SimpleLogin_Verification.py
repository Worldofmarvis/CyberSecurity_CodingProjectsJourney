import os

def clear_screen():

    os.system('cls')


username = input("Username: ")
password = input("Password: ")
print()
print("-----Signup Successfully-----\n")

input("Press Entr Key")
clear_screen()

print("Welcome to the website")
print()
print("Login")
attempt = 3
while attempt > 0:
        print()
        input_username = input("Username: ")
        input_password = input("Password: ")
        if(input_username == username and  input_password == password):
              print("Login Successfully.")
              print()
              break
        else:
            attempt-=1
            print("Try Again." + " Attempt Left" ,attempt)
if attempt == 0:
      print("Login Locked.")
