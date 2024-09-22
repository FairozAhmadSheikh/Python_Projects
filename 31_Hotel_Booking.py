rooms_data={"luxury":{"price":4000},
            "delux":{"price":6000},
            "super delux":{"price":12000},
            "seven stars":{"price":18000}
            }

print("Rooms we provide are : "+str(list(rooms_data.keys())))
room_type=input("Enter What type of room you want from above list ?").lower()

if room_type=="luxury":
    print("You will be booking",room_type," Room","For  Amount : ",rooms_data[room_type]["price"],"$")
    consent=input("Confirm Your Order with Yes or No ?\n").lower()
    if consent=="yes":
        print(room_type," Booked Sucessully")
    else:
        print("Come back when You need a Room")
elif room_type=="delux":
    print("You will be booking",room_type," Room","For  Amount : ",rooms_data[room_type]["price"],"$")
    consent=input("Confirm Your Order with Yes or No ?\n").lower()
    if consent=="yes":
        print(room_type," Booked Sucessully")
    else:
        print("Come back when You need a Room")
elif room_type=="super delux" :
    print("You will be booking",room_type," Room","For  Amount : ",rooms_data[room_type]["price"],"$")
    consent=input("Confirm Your Order with Yes or No ?\n").lower()
    if consent=="yes":
        print(room_type," Booked Sucessully")
    else:
        print("Come back when You need a Room")
elif room_type=="seven stars" :
    print("You will be booking",room_type," Room","For  Amount : ",rooms_data[room_type]["price"],"$")
    consent=input("Confirm Your Order with Yes or No ?\n").lower()
    if consent=="yes":
        print(room_type," Booked Sucessully")
    else:
        print("Come back when You need a Room")
else:
    print(" Please Choose Correct Option")