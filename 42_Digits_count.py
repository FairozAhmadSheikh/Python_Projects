number=int(input("Enter  A Number To Count Digits :\n"))
# Function to count number of digits
def number_counter(n):
    counter=0
    while n!=0:    # Loop for floor dividing a number continously
        n=n//10    # Updatas a value
        counter+=1
    return counter
print(number_counter(number))