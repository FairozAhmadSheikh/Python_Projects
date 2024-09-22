print("Welcome to Sasta Cinema".center(30,"="))
age=int(input("Enter Your age :\t"))
quantity=int(input("How much tickets  do you want :\t"))
if age<12:
    ticket=5
    price=quantity*ticket
    print("Total amount : ",price,"$")
elif age>12 and age<60:
    ticket=10
    price=quantity*ticket
    print("Total amount : ",price,"$")
elif age>60:
    ticket=7
    price=quantity*ticket
    print("Total amount : ",price,"$")
