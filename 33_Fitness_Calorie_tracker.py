Exercise_list={
    "running":{"calories burned":120},
    "cycling":{"calories burned":220},
    "swiming":{"calories burned":320},
    "gym":{"calories burned":420},
}
what_did_you_do=input("What Exercise did you do today \nrunning\ncycling\nswiming\ngym \n").lower()
how_much_time_spent=float(input("How much Time did you spend "+what_did_you_do+" in Hours ?"))

if what_did_you_do=="running":
    print("You Burned "+str(Exercise_list[what_did_you_do]["calories burned"]*how_much_time_spent)+" Calories")
elif what_did_you_do=="cycling":
    print("You Burned "+str(Exercise_list[what_did_you_do]["calories burned"]*how_much_time_spent)+" Calories")
elif what_did_you_do=="swiming":
    print("You Burned "+str(Exercise_list[what_did_you_do]["calories burned"]*how_much_time_spent)+" Calories")
elif what_did_you_do=="gym":
    print("You Burned "+str(Exercise_list[what_did_you_do]["calories burned"]*how_much_time_spent)+" Calories")
else:
    print("I dont know about this Exercise yet! You Might had a Typo while Entering")