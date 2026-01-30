total_sum = 0
stop = False
while(True):
    num = input("Enter a number (or type 'stop' to finish): \n")
    if(num=="stop"):
        print("Final Total sum: ", total_sum)
        stop
    converted_int = int(num)
    total_sum += converted_int
    print("Current total: ", total_sum)
    



