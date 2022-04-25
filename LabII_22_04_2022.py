print("Press 1 for printing (Hello World).\nPress 2 for greeting with your name.\nPress 3 to convert the temperature from Fahrenheit value into Degree Celsius value.\nPress 4 to find the greatest and smallest of three numbers.\nPress 5 for exiting.")

while(1):
    # enter the operation number which you want to perform
    y = int(input("Enter operation number: "))
    if (y == 5):
        # exit code
        print("Hope you enjoyed!😊")
        break
    elif (y == 1):
        # print Hello World
        print("Hello World!😊")
    elif (y == 2):
        # enter your name to let your friend(computer) greet you
        name = str(input("Enter your name : "))
        print("Hello, " + name + "! Hope you have a nice day ahead😊")
    elif (y == 3):
        # fah denotes Fahrenheit
        fah = float(input("Enter the temperature in Fahrenheit : "))
        # cel denotes Celsius
        cel = ((fah - 32) * 5) / 9
        # print the converted temperature in °C
        print("Temperature in degree celsius is %0.3f°C." %cel)
    elif (y == 4):
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        c = int(input("Enter the third number : "))
        
        # here is the code for finding the smallest and 
        # greatest number among the three numbers given by 
        # the user
        if (a == b and b == c):
            print("All the three numbers entered are same so the smallest number is equal to the greatest number.")
            # as a = b = c so we can write any of these to print smallest and greatest
            print("The smallest number is %d." %a)
            print("The greatest number is %d." %a)
        elif (a >= b):
            if (a >= c):
                if (b >= c):
                    print("The smallest number is %d." %c)
                else:
                    print("The smallest number is %d." %b)
                print("The greatest number is %d." %a)
            else:
                print("The smallest number is %d." %b)
                print("The greatest number is %d." %c)
        else:
            if (b >= c):
                if (a >= c):
                    print("The smallest number is %d." %c)
                else:
                    print("the smallest number is %d." %a)
                print("The greatest number is %d." %b)   
            else:
                print("The smallest number is %d." %a)
                print("The greatest number is %d." %c)
    else:
        print("Please enter the correct operation number.")
