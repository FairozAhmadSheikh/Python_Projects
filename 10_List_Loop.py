# Initaialize an empty list
list_one=[]
max_integers=5

for i in range(1,max_integers+1):
    element=int(input("Enter List element Here\n"))
    list_one.append(element)

print("Displaying Square's :".center(30,"="))
for val in list_one:
    print(val**2)


