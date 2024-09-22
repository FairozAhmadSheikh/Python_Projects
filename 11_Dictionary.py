# Creating 3 key value paired Dictionary

student={
    "Name":"IUST Student",
    "Age":23,
    "Roll_No":7
}
#Prints whole dictionary
for i in student:
    print(student[i])

# To only print name and age using for loop will work as 
for i in student:
    if i=="Roll_No":
        continue
    print(student[i])