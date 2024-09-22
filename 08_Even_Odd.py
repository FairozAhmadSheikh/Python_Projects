# Printing 1 to 10 using For and Range function
for i in range(1,11):
    print(i)
print("")
    
# Using While to print even numbers 

start = 2
while start <= 20:
    if start % 2 == 1:
        start += 1
        continue
    else:
        print(start)
        start += 1
