def grade_calc():
    marks=float(input("Enter Your Marks Out of 100 : "))
    if marks>100:
        return("You Are Albert Einstine No need To Calculate Your Grades 😂")
    elif marks >=90 and marks<=100:
        return("Congratulation's  You Got  A Grade  🎇 ")
    elif marks >=80 and marks<=89:
        return("Congratulation's  You Got  B Grade  🎇 ")
    elif marks >=70 and marks<=79:
        return("Congratulation's  You Got  C Grade  🎇 ")
    elif marks >=60 and marks<=69:
        return("Congratulation's  You Got  D Grade  🎇 ")
    else:
        return(" Failed !, Try Working Hard Next Time  ")
print("Grades Generator".center(30,"="))
print(grade_calc())