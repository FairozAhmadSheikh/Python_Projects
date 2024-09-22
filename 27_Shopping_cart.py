# Empty Shopping Cart
print("Shopping Cart".center(40,"="))
print("Type Checkout to stop adding items !")
shopping_cart=[]
while True:
    element=input("What do you want to add to cart? \n")
    shopping_cart.append(element)
    if element=="Checkout".lower():
        print(" Your Shopping Card Includes : \n",shopping_cart)
        break
