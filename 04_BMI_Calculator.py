def BMI_Calculator():
    weight=float(input("Enter Weight in kilograms : "))
    height=float(input("Enter Height in Meters :"))
    Categories=["Over Weight", "Under Weight", "Normal Weight","Obesity Class I","Obesity Class II","Obesity Class III"]
    BMI= weight/(height**2)
    if weight<=0 or height<=0:
        return " Enter Correct Height and Weight! " 
    elif BMI<=18.5:
        return "Your BMI IS : ",BMI, Categories[1] 
    elif BMI>18.5 and BMI <=24.9:
        return "Your BMI IS : ",BMI, Categories[2] 
    elif BMI>=25 and BMI <=29.9:
        return "Your BMI IS : ",BMI,Categories[0] 
    elif BMI>=30 and BMI <=34.9:
        return "Your BMI IS : ",BMI,Categories[3] 
    elif BMI>=35 and BMI <=39.9:
        return "Your BMI IS : ",BMI,Categories[4] 
    elif BMI>=40:
        return "Your BMI IS : ",BMI,Categories[5] 
    else:
        return("Something Details Entered are Wrong! ")

consent =input("Do you want Your BMI To be Calculated ?\n").lower()
if consent=="yes" or consent=="1" or consent=="true":
    print(BMI_Calculator())
else:
    print("Thanks for Not Using Me !❤️")
