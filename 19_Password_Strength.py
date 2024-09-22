lower=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
spe=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
nums=['0','1','2','3','4','5','6','7','8','9']
# User input
password=input("Enter Your Passoword ")
#Check point
contains_Upper=False
contains_Lower=False
contains_special=False
conatins_num=False
def Password_Checker(password):
    global contains_special,contains_Lower,conatins_num,contains_Upper
    for val in password:
        if val in lower:
            contains_Lower=True
        elif  val in upper:
            contains_Upper=True
        elif val in nums:
            conatins_num=True
        elif val in spe:
            contains_special=True

Password_Checker(password)  
if conatins_num and contains_Lower and contains_special and contains_Upper:
    print("Password Strong Enough ")
else:
    print("Weak Password")
    
