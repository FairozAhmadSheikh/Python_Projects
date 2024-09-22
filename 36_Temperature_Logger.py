Data_Temperature={
    "Saturday":23.0,
    "Sunday":21.2,
    "Monday":27.4,
    "Tuesday":22.5,
    "Wednsday":28.3,
    "Thursday":31.2,
    "Friday":33.1,
}
average_temp=0.0
for i in Data_Temperature:
    average_temp+=Data_Temperature[i]/7

print("Average Temperature for the Week remained :"+str(average_temp)+" Degree Celcius")