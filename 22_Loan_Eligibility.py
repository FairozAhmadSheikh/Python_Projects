# Function to check if we can process the loan Amount or not
def Cibil_score():
    global decession
    income_monthly=float(input("Enter Your Monthly Income : \n"))
    loan_amount=float(input("How Much Loan Amount Do You Want : \n"))
    if loan_amount<=5*income_monthly:
       decession=True
       return decession
    else:
        return decession 
print("E-Loans Check".center(20,"="))
decession=False
agreement=input("Do You want to apply for Personal Loan ? ").lower()
if agreement=="yes" or agreement=="1" or agreement=="true":
    Cibil_score()
    if decession==True:
        print("You are Eligible")
    else:
        print("Not Eligible , Try raising monthly income 5 times your required loan amount")
else:
    print("Answer in 'Yes' or 'NO' or 'True' or 'False' or '1' or'0' ")