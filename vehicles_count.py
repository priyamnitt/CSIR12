# Problem: Write a python program to count the number of vehicles entering and leaving the main gate of NITT.


from bisect import bisect_left

print("Enter the timing of entrance and exit of vehicle.")
vehicles = []
vehicles_time = []

# here we take entrance and exit timing as input from the user for the entire day
while(1):
    operation_no = int(input("Enter 1 if you want to enter timing of vehicles\nEnter 2 to observe the simulation.\n"))
    
    if operation_no == 2:
        break
    
    time = input("Enter the time of entrance/exit of vehicle in the format HH:MM:SS - ")
    is_entering = input("Is the vehicle entering the gate of NITT. Write Yes for  entering and No for exiting. - ")
    vehicles.append([time, is_entering])
    vehicles_time.append(time)
    
    
# here we perform the precomputation in order to process queries fastly - O(N) where N = size of vehicles array
entering_array = []
exit_array = []
mp = {}

# Although the array will be sorted with time but just to take care of case when someone enters data not in sync 
vehicles.sort(key = lambda x:x[0])
vehicles_time.sort()

for vehicle in vehicles:
    if vehicle[1] == "Yes":
        entering_array.append(1)
        exit_array.append(0)
    else:
        exit_array.append(1)
        entering_array.append(0)
    
vehicles_count = len(entering_array)

for i in range(1,vehicles_count):
    entering_array[i] += entering_array[i-1]
    exit_array[i] += exit_array[i-1]
    
# here we handle queries to find number of vehicles between start_time and end_time
print("Welcome to the simulation!!")
while(1):
    operation_no = int(input("Enter 1 to get count of vehicles within a timeframe.\nEnter 2 to exit.\n"))
    
    if operation_no == 2:
        break
    
    # find index using binary search - O(lg(N))
    start_time = input("Enter the start time. - ")
    end_time = input("Enter the end time. - ")
    
    start_index = bisect_left(vehicles_time, start_time) - 1
    end_index = bisect_left(vehicles_time, end_time)
    
    print(start_index, end_index)
    
    if end_index < vehicles_count and vehicles_time[end_index] != end_time:
        end_index -= 1
    
    if start_index <= -1:
        enter_s = 0
        exit_s = 0
    elif start_index >= vehicles_count:
        enter_s = entering_array[vehicles_count - 1]
        exit_s = exit_array[vehicles_count - 1]
    else: 
        enter_s = entering_array[start_index]
        exit_s = exit_array[start_index]
    
    if end_index >= vehicles_count:
        enter_e = entering_array[vehicles_count - 1]
        exit_e = exit_array[vehicles_count - 1]
    elif end_index <= -1:
        enter_e = 0
        exit_e = 0
    else: 
        enter_e = entering_array[end_index]
        exit_e = exit_array[end_index]
        
    # compute vehicles using O(1)
    print(start_index, end_index)
    print("No of vehicles entered - ", enter_e - enter_s)
    print("No of vehicles exited - ", exit_e - exit_s)
    
    
