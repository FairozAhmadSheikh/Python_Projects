print("Budget Planner".center(40,"="))
total_expense=float(input("What is Your Total Budget :\n"))
flight_expense=float(input("What is Your Flight Ticket Price :\n"))
accommodation_expense=float(input("What is Cost of  Accomodation : \n"))
food_expense=float(input("How much will your Food cost in whole Trip : \n"))
transportation_exprense=float(input("How Much will  you spend for transportation : \n"))
# Calculating Expense
overall_cost=(flight_expense+accommodation_expense+food_expense+transportation_exprense)
# Decession wheather you can afford or not
can_afford=total_expense-overall_cost
if can_afford==0:
    print("You can Go for trip with  remaining balance as : 0 $")
elif can_afford>0:
    print("You can Go for trip Your savings from Total budget will be :"+str(can_afford)+" $")
else:
    print("This trip is Out of your Budget , Try Lowering the expenses! ")