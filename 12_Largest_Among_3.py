def Largest_One():
    num1=int(input("Enter Number First : \n"))
    num2=int(input("Enter Number Second: \n"))
    num3=int(input("Enter Number Third : \n"))
    if num1>=num2 and num1 >=num3:
        return( str(num1)+" Is Greatest")
    elif num2>=num3:
        return(str(num2)+" Is Greatest")
    else:
        return(str(num3)+" Is Greatest")
print("Welcome to Greatest Finder ")
print(Largest_One())