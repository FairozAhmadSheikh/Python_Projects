Inventory={
    "physics":{"Name":"Arihants Physics","Author":"Arihant","Stock":20},
    "cyber":{"Name":"Cyber World","Author":"JP-Morgan","Stock":30},
    "chemistry":{"Name":"Java","Author":"YeshwantSir","Stock":10},
    "c programming":{"Name":"Lets C","Author":"Salman Khan","Stock":0},
}
def Library_Manger():
    Search=input("Write name of any book you want to issue \n Physics \n Chemistry \n Cyber \n C programming \n").lower()
    if Search=="physics":
        if int(Inventory["physics"]["Stock"])>=1:
            Inventory["physics"]["Stock"]-=1
            return("Book Issued Sucessfully",Inventory["physics"]["Name"]," By ",Inventory["physics"]["Author"])
        else:
            return("Book out of Stock")
    elif Search=="cyber":
        if int(Inventory["cyber"]["Stock"])>=1:
            Inventory["cyber"]["Stock"]-=1
            return("Book Issued Sucessfully",Inventory["cyber"]["Name"]," By ",Inventory["cyber"]["Author"])
        else:
            return("Book out of Stock")
    elif Search=="chemistry":
        if int(Inventory["chemistry"]["Stock"])>=1:
            Inventory["chemistry"]["Stock"]-=1
            return("Book Issued Sucessfully",Inventory["chemistry"]["Name"]," By ",Inventory["chemistry"]["Author"])
        else:
            return("Book out of Stock")
    elif Search=="c programming":
        if int(Inventory["c programming"]["Stock"])>=1:
            Inventory["c programming"]["Stock"]-=1
            return("Book Issued Sucessfully",Inventory["c programming"]["Name"]," By ",Inventory["c programming"]["Author"])
        else:
            return("Book out of Stock")
    else:
        return("We dont have  this book")
print("IUST Library".center(50,"="))
choice=input("Do you want to use our Library Mangment System ? \n").lower()
if choice=="yes" or choice=="1" or choice=="true":
    Library_Manger()
elif choice=="no" or choice==0 or choice=="false":
    print("Come Back when You need Books ")
else:
    print("Sorry I could not understand Say Yes or No !")

