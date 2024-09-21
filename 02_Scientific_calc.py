import math
def Scientific_Calculator():
    scientific=input(" 1 : For Square Root \n 2 : For Exponentiation \n 3 : Logarithm  \n 4 : Sine \n 5: Cosine \n 6: Tangent  ")
    if scientific=="1":
            number=int(input("Enter a Number You want to find Square root for ? "))
            print(math.sqrt(number))
    elif scientific=="2":
            number=int(input("Enter Base Number?"))
            power=int(input("Enter Power or Exponent "))
            print(math.pow(number,power))
    elif scientific=="3":
            number=int(input("Enter a Number You want to find Log of base 10 ? "))
            print(math.log10(number))
    elif scientific=="4":
            number=int(input("Enter a sine value to calculate ? "))
            print(math.sin(number))
    elif scientific=="5":
            number=int(input("Enter a cosine value to calculate ? "))
            print(math.cos(number))
    elif scientific=="6":
            number=int(input("Enter a tangent value to calculate ? "))
            print(math.tan(number))
    else:
            print("Wrong Choice!")
def Simple_Calculator():
    num1=int(input("Enter first number :"))
    simple_operation=input("\n Choose an Operation \n + : Addition \n - : Subtraction \n * : Multiplication \n / : Divide \n")
    num2=int(input("Enter second number :"))    
    if simple_operation=="+":
        print(num1+num2)
    elif simple_operation =='-':
        print(num1-num2)
    elif simple_operation=='*':
        print(num1*num2)
    elif simple_operation=='/':
        if num2==0:
            print("Not Defined")
        else:
            print(num1/num2)
    else:
        print("Invalid Operator selected")


complex_operation=input("Enter '1'  for Scientfic  or '2' for Simple Calculator ").lower()

if complex_operation=="1":
        Scientific_Calculator()
elif complex_operation=="2":
      Simple_Calculator()
else:
      print("Invalid Choice Please Try again")






    



