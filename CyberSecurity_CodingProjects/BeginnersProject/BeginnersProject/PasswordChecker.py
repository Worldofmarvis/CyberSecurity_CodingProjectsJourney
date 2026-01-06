right_password = "Alpha123"
password = input("Enter your password: ")
if(password!=right_password):
    for i in range(1,4):
        print("Try Again!")
        password = input("Enter your password: ")
else:
    print("You entered the right password.")
