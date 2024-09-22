print("Shopping Discounts".center(30,"="))
total_shopping=float(input("What was Your Total Shopping Amount : \n"))
discount=0.1
Vocher_Code1="save_iust50" 
Vocher_Code2="sameer100" 
Vocher_Code3="SAVE_IUST50" 
if total_shopping>100:
    new_total=total_shopping-(total_shopping*0.1)
    print("Congratulations 🎉🎉🎉 got Discount 10% , New Total is ",new_total,"$")
else:
    print("You have Shopped for less than 100 $ ")
    voch=input("Type Coupoun or Vochers Code  Here To claim Discount ? \n")
    if voch==Vocher_Code1 or voch==Vocher_Code3:
        new_total=total_shopping-(total_shopping*0.5)
        print("Congratulations 🎉🎉🎉 got Discount 50% , New Total is ",new_total,"$")
    
    elif voch==Vocher_Code2 :
        new_total=0
        print("Congratulations 🎉🎉🎉 100% Discount For You")
        print("You Got Everything for Free 🎉🎉🎉🎆🎇")
    else:
        print("You did not get discount ,Pay Actual price of : ",total_shopping)