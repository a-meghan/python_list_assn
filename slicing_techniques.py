#Task 1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print("These are the temperatures for the second week of the month:",temperatures[7:14])


#Task 2
really_stinkin_hot = []
for temp in temperatures:
    if temp > 100:
        really_stinkin_hot.append(temp)
print("These are the temperatures that are over 100 degrees this month:",really_stinkin_hot)