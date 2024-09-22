# Could not understand Question
print("")
print("Grocery Bill Generator".center(50,"="))
print("To checkout Type Stop".center(50,"="))

cart={
    "Products":[],
    "Rates":[]
}
while True:
    element=input("Enter Name of Item : ").lower()
    if element=="stop":
          break
    price=float(input("Enter Price of Entered Item : "))
    cart["Products"].append(element)
    cart["Rates"].append(price)
# Displays Products and rates
print("Bill Here".center(40,"="))
for item,price in zip(cart["Products"],cart["Rates"]):
    
    print("You Bought "+str(item)+" For : "+str(price)+"$".rjust(4))
# Check if user has a coupon
coupoun="Free60"   # Gives 60% discount
coupon_check=input("Do you have a Discount Vocher ?\n").lower()
if coupon_check=="true" or coupon_check=="yes" or coupon_check=="1":
    coupon_enterd=input("Enter Vocher Code Here : ")
    if coupon_enterd=="Free60":
    # Your Total With Discount 
        sum=0
        for i in cart["Rates"]:
            sum+=i   
        print("You got 60% OFF on Total Amount of : "+str(sum)+" $")
        print("After Discount Total Bill is : "+ str(sum-(sum*0.6))+" $".rjust(4))
else:
    # Your Total Without comes out to be 
    sum=0
    for i in cart["Rates"]:
        sum+=i
    print("Your Total Bill is : "+ str(sum)+" $".rjust(4))