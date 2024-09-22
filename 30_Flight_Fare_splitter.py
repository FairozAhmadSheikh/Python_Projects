def fare_share():
    total_fare=float(input("What was your Total Flight Fare : "))
    number_of_splitters=int(input("How many People are You sharing Fare with : "))
    splitted_amount=total_fare/number_of_splitters
    return"Total Amount Each Person has to Pay is : "+str(splitted_amount)+" $"
print("Split Fare With Freidns".center(40,"="))
print(fare_share())