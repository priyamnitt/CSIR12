print("Press 1 for checking for the validity of the password.\nPress 2 for printing natural number upto 100 in pairing from opposite side.\nPress 3 for printing next 5 ip address.\nPress 4 for exiting")

while(1):
    y = int(input("Enter the operation number : "))
    
    if(y == 4):
        # exit code
        print("Hope you enjoyed!😊")
        break
    
    if (y == 1):
        count = 0
        p = input("Enter the password : ")
        
        for i in range(0, len(p)):
            # condition for the presence of (a-z) in the password
            if(ord(p[i]) in range(97,123)):
                count += 1
                break
            
        for i in range(0, len(p)):
            # condition for the presence of (A-Z) in the password
            if(ord(p[i]) in range(65,91)):
                count += 1
                break
            
        for i in range(0, len(p)):
            # condition for presence of (0-9) in the password
            if((p[i]) in str(range(10))):
                count += 1
                break
            
        for i in range(0, len(p)):
            # condition for presence of (#,$,@) in the password
            if(p[i] in ["#","$","@"]):
                count += 1
                break
            
        # condition check to ensure minimum length of the password should be 6 and maximum length of password should be 16.
        if(len(p) >= 6 and len(p) <= 16 ):
            count += 1
        if( count == 5):
            # if all the necessary condition that is required for the password is fulfilled then it is valid
            print("Your password is valid")
        else:
            # if all the necessary condition that is required for the password is not fulfilled then it is not valid
            print("Your password is not valid")
            
    if (y == 2):
        # this program will print the natural numbers from 1 till 99 in pair - both in forward and reverse order
        
        for i in range(1,100):
            print(str(i)+"-----"+str(100-i))
    
    if (y == 3):
        # in ip_address there are four parts - 1st one is known as first_octet, 
        # 2nd one as second_octet, 3rd one as third_octet, 4th one as forth_octet
        ip_address = str(input("Enter the IP address(xxx.xxx.xxx.xxx) : "))
        x = ip_address.split(".")
        first_octet = int(x[0])
        second_octet = int(x[1])
        third_octet = int(x[2])
        fourth_octet = int(x[3])
        
        octet_start = fourth_octet + 1
        octet_end = fourth_octet + 6
        # each octate at max can go upto 255 each 
        
        if (1 <= first_octet <= 255) and (0 <= second_octet <= 255) and (0 <= third_octet <= 255) and (0 <= fourth_octet <= 255):
            
            for ip in range(octet_start, octet_end):
                fourth_octet = forth_octet + 1
                
                if (fourth_octet > 255):
                    fourth_octet = (fourth_octet % 255) - 1
                    third_octet = third_octet + 1
                    
                    if (third_octet > 255):
                        third_octet = (third_octet % 255) - 1
                        second_octet = second_octet + 1
                        
                        if (second_octet > 255):
                            second_octet = (second_octet % 255) - 1
                            first_octet = first_octet + 1
                            
                            if (first_octet > 255):
                                print("Oops! No more available IP address!")
                                break
                            
                print(".".join([str(first_octet),str(second_octet),str(third_octet),str(fourth_octet)]))
        else:
           print("Invalid input!")
    
    else:
        print("Please enter the correct operation number.")
