def Calculations():
    while True:
        num1=int(input("Enter first number :"))
        num2=int(input("Enter second number :"))    
        operator=input("Enter + - * or / ")
        if operator=="+":
            print(num1+num2)
        elif operator =='-':
            print(num1-num2)
        elif operator=='*':
            print(num1*num2)
        elif operator=='/':
            if num2==0:
                print("Not Defined")
            else:
                print(num1/num2)
        else:
            print("Wrong Operator Selected Try again ")
        Runner=input("Y: for More Calculation \n N : for Exiting Calculator ").lower()
        if Runner == "y":
            Calculations()
        else:
            break;
Calculations()
