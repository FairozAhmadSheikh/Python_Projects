number=int(input("Enter  A Number to check Armstrong :\n"))

def arm_chechk(n):
    global number
    fact_check=0
    while n!=0:
        reminder=n%10
        fact_check+=reminder**3
        n=n//10
    if number==fact_check:
        return f"{number} Is a Armstrong Number  "
    else:
        return  f"{number} Is Not a Armstrong Number  "
print(arm_chechk(number))