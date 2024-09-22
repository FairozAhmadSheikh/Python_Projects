#Function Decleration and Defination
def simple_intrest_calc():
    principal_amount=float(input("Enter Principal Amount : \n"))
    intrest_rate=float(input("Enter Rate of Intrest : \n"))
    time=float(input("Enter Time in Years : \n"))
    simple_intrest=(principal_amount*intrest_rate*time)/100
    return("Simple Intrest after Calculations is : "+str(simple_intrest))
# Welcome Message
print("Welcome To Simple Intrest Calculator")
# Function Call
print(simple_intrest_calc())