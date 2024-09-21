# Function that calaculates Percentage
def Percentage_Calculator():
    conversion_Type=int(input("Select one among following \n 1 : Calculate Percentage Of a Number \n 2 : Calculate what percentage one number is of another \n 3 : Calculate Percentage Change \n "))
    if conversion_Type==1:
        num=float(input("Write a Number Here ? \n"))
        how_much=float(input("Enter Percentage to be calculated for Above Number :"))
        result=((how_much/100)*num)
        return (str(how_much)+" % of "+str(num) +" is : ",str(result))
    elif conversion_Type==2:
        whole=float(input("Write a Number Here  (Whole) ? \n"))
        part=float(input("Write a Part of Number (Part)  ? \n"))
        result=((part/whole)*100)
        return (str(part)+" of "+str(whole)+" is :"+str(result)+" %")
    elif conversion_Type==3:
        old_val=float(input("Enter Old Value please : \n"))
        new_val=float(input("Enter New Value please : \n"))
        result=((new_val-old_val)/old_val)*100
        if result>1:
            return ("Increased by  "+str(result)+" % ")
        elif result<0:
            return ("Decreased by  "+str(result)+" % ")
        else:
            return ("Stayed Same! ")
    else:
        return ("Please Choose Correct Option! ")       
# Welcome Message        
print("")
print("Percentage Calculator".center(40,"="))
# Consent of User
consent=input("Do you want to use Percentage Calculator\n").lower()
# Program Launcher 
if consent=="yes" or consent=="true" or consent=="1":
    print(Percentage_Calculator())
else:
    print("Thanks For Saving My Energy! ")