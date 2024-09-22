import time
# First find something like setTimeout()

# Ask user Coundown seconds 
seconds=int(input("Enter the number of seconds to countdown : \n"))

# Start a loop that runs upto 0 starting from seconds entered
for i in range(seconds,0,-1):
    print(i)
    time.sleep(1) # Gives exact delay of 1 second
print("Time's Up ! ")