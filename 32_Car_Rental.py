car_collection={
    "suv":{"price":600},
    "sports":{"price":1200},
    "comfort":{"price":1800},
    "luxury":{"price":2700},
    "sedan":{"price":2900}
}

# Booking Function
def car_booking():
    car_requested=input("Select One Among Above Cars : \n").lower()
    if car_requested=="suv":
        print("You are booking SUV for Fare of "+str(car_collection[car_requested]["price"])+" $ Per Hour")
        confirmation=input("Type yes or Y to confirm booking ").lower()
        if confirmation=="yes" or confirmation=="y":
            return("Booking Successfull ")
        else:
            return("Come back when you need a car")
    elif car_requested=="sports":
        print("You are booking SUV for Fare of "+str(car_collection[car_requested]["price"])+" $ Per Hour")
        confirmation=input("Type yes or Y to confirm booking ").lower()
        if confirmation=="yes" or confirmation=="y":
            return("Booking Successfull ")
        else:
            return("Booking Halted ❌ \nCome back when you need a car")
    elif car_requested=="comfort":
        print("You are booking SUV for Fare of "+str(car_collection[car_requested]["price"])+" $ Per Hour")
        confirmation=input("Type yes or Y to confirm booking ").lower()
        if confirmation=="yes" or confirmation=="y":
            return("Booking Successfull ")
        else:
            return("Booking Halted ❌ \nCome back when you need a car")
    elif car_requested=="luxury":
        print("You are booking SUV for Fare of "+str(car_collection[car_requested]["price"])+" $ Per Hour")
        confirmation=input("Type yes or Y to confirm booking ").lower()
        if confirmation=="yes" or confirmation=="y":
            return("Booking Successfull ")
        else:
            return("Booking Halted ❌ \nCome back when you need a car")
    elif car_requested=="sedan":
        print("You are booking SUV for Fare of "+str(car_collection[car_requested]["price"])+" $ Per Hour")
        confirmation=input("Type yes or Y to confirm booking ").lower()
        if confirmation=="yes" or confirmation=="y":
            return("Booking Successfull ")
        else:
            return("Booking Halted ❌ \nCome back when you need a car")
    else:
        print("We do not have the car you are mentioning ")
# Welcome Message and Displaying Collection
print("IUST CAR RENTAL".center(40,"="))
print("Cars we have \n",list(car_collection.keys()))
permission=input("Do you wish to book any car From above List ? Yes or No \n").lower()
if permission=="yes" or permission=="true" or permission=="1":
    print(car_booking())
else:
    print("Thanks! 🎉🎉🎉 \nWe will Try to improve car collection so that you book car from us next time ")