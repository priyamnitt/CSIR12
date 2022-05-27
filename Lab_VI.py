print("Press 1 to find sum of two given integers and get the output as per the number given by user.\nPress 2 to print a triangle of numbers where number of rows is specified by the user.\nPress 3 to print  first 3 letters of my name on the screen using #.\nPress 4 for exiting.")

while(1):

    y = int(input("Enter the operation number : "))
    
    if( y == 4):
        
        # exit code
        print("Hope you enjoyed!")
        break
    
    elif (y == 1):
        count = 0
        while(1):
            if (count == 3):
                break
            a = int(input("Enter the first number : "))
            b = int(input("Enter the second number : "))
            
            # if sum of the number is between 25 and 50 the output will be 50
            
            if ((a + b) > 25 and (a + b) <= 50):
                print("50")
                try_more = int(input("Enter 1 to try the program once again or 2 to exit : "))
                
                if (try_more == '1'):
                    continue
                else:
                    break
                
            # if sum of the number is between 50 and 60 the output will be 60
            
            elif((a + b) > 50 and (a + b) <= 60):
                print("60")
                try_more = int(input("Enter 1 to try the program once again or 2 to exit : "))
                
                if (try_more == '1'):
                    continue
                else:
                    break
                
            # if sum will be less than 25 or greater than 60 the user will get 2 more chance to run the code 
            
            else:
                print("Please enter the appropriate numbers.")
                count += 1
                continue
    
    elif (y == 2):
        rows = int(input("Enter the number of rows : "))
        print()
        p = int((rows * (rows + 1)) / 2) # Initially it is set the maximum value possible for given number of rows
        c = rows -1 # Variable which helps to track number of spaces to give in the start
        k = -(p - 1) # Initial constant to achieve desired pattern and generate current_value at each step
        
        space = len(str(p)) + 1 # Length of maximum_value possible in terms of number of digits
        for row in range(rows):
            for g in range(c):
                print(" " * (int(space / 2) + 1), end = "")
            c = c - 1
            for j in range(row + 1):
                current_value = p + k
                print(current_value, end = "")
                print(" " * (space - len(str(current_value)) + 1), end = "")
                p = p - 1
            k = k + (2 * (row + 1) + 1)
        
            print()
    
    elif (y == 3):
        for rows in range(8):
            
            for col in range(37):
                # condition on how many and where the symbol # should be present for the shape as my name.
                if col == 30 or col == 0 or col == 14 or (col in [8,22] and (rows == 1 or rows == 2)) or ((col in [1,2,3,4,5,6,7,15,16,17,18,19,20,21]) and (rows == 0 or rows == 3)) or (col == 16 and rows == 4) or (col == 18 and rows == 5) or (col == 20 and rows == 6) or (col == 22 and rows == 7) or(col in [26,27,28,29,31,32,33,34] and (rows == 0 or rows == 7)):
                    
                    print("#",end = "")
                    
                else:
                    
                    print(end = " ")
                    
            print()
            
    else:
        print("Enter the correct operation number.")
