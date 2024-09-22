# Things to check for 
domain_checker=['@']
dot_checker=['.in','.com','.gov','.uk','.']
print("Email Validator".center(30,"="))
# User Input
email=input("Please Enter Your Email : \n")

# Flags
domain_exists=False
dot_exists=False
# Function to check
for val in email:
    if val in domain_checker:
        domain_exists=True
    elif val in dot_checker:
        dot_exists=True

if dot_exists and domain_exists:
    print("This is a Valid Email ✅ ")
else:
    print(" Not a Valid  Email ❌ ")
