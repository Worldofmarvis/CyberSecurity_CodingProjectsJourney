import os
def Showoption():
    print("-"*30)
    print("Welcome to my Simple To-do List")
    print("-"*30)
    print("1.Add an Activity")
    print("2.Show all Activitie(s)")
    print("3.Update an Activity")
    print("4.Delete an Activity")
    print("5. Exit")

def Add_Activity():
    memory_activity = []
    number_activity = int(input("Enter the number of activities you want to add: "))
    for i in range(number_activity):
        activity = input(f"Enter activity {i+1}: ")
        memory_activity.append(activity)
    return memory_activity

def clearScreen():
    os.system('cls')

Showoption()
while(True):
    clearScreen()
    Showoption()
    operation = int(input("Enter an operation: "))

    if(operation==5):
        False
    
    if(operation==1):
        Add_Activity()
        input("Press entr key to continue")


    


    
    