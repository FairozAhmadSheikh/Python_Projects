# # This will have  a flaw that even if you deposit amount you will only be able to withdraw initial amount of 1000  
# def Bank():
#     wallet=1000
#     user_action=input("Select Option \n'1' : For Balance Enquiry \n'2' : For Deposit \n'3' : For Withdrawal  \n'4' : For Exit  :\n")    
#     if user_action=="1":
#         return "Your Account Balance is : "+str(wallet)+" $"
#     elif user_action=="2":
#         credit_amount=float(input("Enter Amount to deposit : "))
#         wallet+=credit_amount
#         print(wallet)
#         return "Added Sucessfully, Balance "+str(wallet)+" $"
#     elif user_action=="3":
#         credit_amount=float(input("Enter Amount to deposit : "))
#         if credit_amount<=wallet:
#             wallet-=credit_amount
#             print(wallet)
#             return "Withdrawl Sucessfull, Balance "+str(wallet)+" $"
#         else:
#             return "You don't have Enough Balance to Withdraw"
#     elif user_action=='4':
#         print("Thanks Visit Again")
#         global value
#         value=False
#         return value

# print("Sasta ATM".center(40,"="))
# print(Bank())
# Approach 32
def bank(initial_amount):
    amount = initial_amount
    
    def bank_function():
        nonlocal amount
        while True:  # Loop to keep the banking operations running
            try:
                user_action = int(input(" '1' : For Balance Enquiry\n '2' : For Deposit\n '3' : For Withdrawal\n '4' : To Exit\n"))
                
                if user_action == 1:
                    print(f"Your Balance is: {amount} $")
                    
                elif user_action == 2:
                    deposit_amount = float(input("How much do you want to deposit? \n"))
                    if deposit_amount > 0:
                        amount += deposit_amount
                        print(f"Deposit successful! New Balance = {amount} $")
                    else:
                        print("Please enter a valid deposit amount!")
                        
                elif user_action == 3:
                    withdrawal_amount = float(input("How much do you want to withdraw? \n"))
                    if withdrawal_amount <= amount:
                        amount -= withdrawal_amount
                        print(f"Withdrawal successful! New Balance = {amount} $")
                    else:
                        print("Insufficient balance for this withdrawal!")
                        
                elif user_action == 4:
                    print("Thank you for using the bank service. Goodbye!")
                    break  # Exit the loop
                    
                else:
                    print("Select a valid option, please!")

            except ValueError:
                print("Invalid input. Please enter a number.")

    return bank_function

# Create the bank function with an initial balance and call it
bank_account = bank(2500)
bank_account()
