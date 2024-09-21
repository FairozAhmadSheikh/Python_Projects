def Discount_Calculator():
    oroginal_price=int(input("Enter The Orignal Price Of an item ? \n"))
    discount_needed=int(input("Enter how much percentage `%`  of Discount You want? \n"))
    # Calculates Discount
    result=(oroginal_price/100)*discount_needed
    return "You got Discount of "+str(discount_needed)+" % , Your new price will be only "+str(oroginal_price-result)
    #Uncomment this block if you dont want to allow more than 100% discount and comment Line 6
    # if result<=oroginal_price:
    #     return "You got Discount of "+str(discount_needed)+" % , Your new price will be only "+str(oroginal_price-result)
    # else:
    #     return "I Wont Let This Happen !"
print("")
print("Welcome To Discount Shop".center(50,"="))
print("")
consent=input("Do you want to use Discount Calculator\n").lower()
# Program Launcher 
if consent=="yes" or consent=="true" or consent=="1":
    print(Discount_Calculator())
else:
    print("Thanks, You Might need me Soon 😁😁")