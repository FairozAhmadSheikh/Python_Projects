import math
# coordinates for point one
x1=float(input("Enter Coordinate x1: \n"))
y1=float(input("Enter Coordinate y1: \n"))
# coordinates for point two
x2=float(input("Enter Coordinate x2: \n"))
y2=float(input("Enter Coordinate y2: \n"))
# result calc
euclids_distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f"Euclids Distance between two points is : {euclids_distance}")