decession=int(input("Choose An Entity  : \n 1: Length \n 2: Weight \n 3: Temperature \n 4: Time \n"))

if decession==1:
    print("Welcome".center(30,"="))
    option_selected=int(input("Select From Below Options \n 1 For KMPH to MPH \n 2 For Meters to Feet \n"))
    if option_selected==1:
        data=int(input("How many Kilometer to convert in Miles ? \n"))
        print(" There Are  "+str(data*0.621371) +" Miles in "+ str(data) +" Kilometers")
    elif option_selected==2:
        data=int(input("How many Meters do you want to convert in Feet ? "))
        print("There are "+ str(data*3.28)+"Feets In "+str(data)+" Meters")
    else:
        print(" Invalid Option  Selected !")
        
elif decession==2:
    print("Weight Converter".center(40,"="))
    data=int(input("How many Kilograms do you want to convert in Pounds? \n"))
    print("There are "+str(data*2.204)+" Pounds in "+str(data)+" Kilograms")
    
elif decession==3:
    print("Temperature Converter ")
    temperature=float(input("Enter Temperature First ? \n"))
    choice=int(input("Select One Option \n 1 For Converting  Celcius to Fahrenheit \n 2 For Converting Fahrenheit into Celcius"))
    
    if choice==1:
        converted=float((temperature*(9/5))+32)
        print(str(converted)+" Fahrenheit's")
        
    elif choice==2:
        converted=float((temperature-32)*(5/9))
        print(str(converted)+" Celcius")
        
    else:
        print("Invalid Option Choosen! ")      

elif decession==4:
    print("Select one Option ".center(40,"="))
    choice=int(input(" 1: Convert Hours to Minutes \n 2: Convert Minutes to Seconds \n 3: Convert Seconds to Milli-Seconds \n"))
    if choice==1:
        data=int(input("Enter Hours to be converted to Hours ? \n"))
        print("Number of Minutes in ",str(data)+" Hours are : "+str(data*60)+" Minutes" )
    elif choice==2:
        data=int(input("Enter Minutes to be converted to Seconds? \n"))
        print("Number of Seconds in ",str(data)+" Minutes are : "+str(data*60)+" Second" )
    elif choice==3:
        data=int(input("Enter Seconds to be converted to Milli-seconds ? \n"))
        print("Number of Minutes in ",str(data)+" Hours are : "+str(data*1000)+" Milli-seconds")
    else:
        print("Invalid Choice !")  

else:
        print("Invalid Option Choosen! ")