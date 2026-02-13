import os
def Toadd(a,b):
    result = a + b
    return result
  

def Tosubtract(a,b):
    result = a - b
    return result

def Tomultiply(a,b):
    result = a * b
    return result

def Todivide(a,b):
        try:
            result = a / b
        except ZeroDivisionError:
             print("Warning, its a Zero Division Error!")
             return None
        else:
            return result
        
def Showoptions():
    print("-"*30)
    print("Welcome to my Calculator")
    print("-"*30)
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

def ClearScreen():
     os.system('cls')
    

while(True):
     ClearScreen()
     Showoptions()
     operation = int(input("Choose an operation: "))

     if(operation==1):
          num1 = int(input("Enter a first number: "))
          num2 = int(input("Enter a second number: "))
          print( "Answer: ", Toadd(num1,num2))
          input("Press enter key to continue")     

     elif(operation==2):
          num1 = int(input("Enter a first number: "))
          num2 = int(input("Enter a second number: "))
          print( "Answer: ", Tosubtract(num1,num2))
          input("Press enter key to continue") 

     elif(operation==3):
          num1 = int(input("Enter a first number: "))
          num2 = int(input("Enter a second number: "))
          print( "Answer: ", Tomultiply(num1,num2))
          input("Press enter key to continue") 

     elif(operation==4):
          num1 = int(input("Enter a first number: "))
          num2 = int(input("Enter a second number: "))
          print( "Answer: ", Todivide(num1,num2))
          input("Press enter key to continue") 

     elif(operation==5):
          print("Program Terminated")
          break
     
     else:
          print("Invalid options")

     


    