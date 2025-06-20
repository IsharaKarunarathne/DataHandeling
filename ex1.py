#create the list named temperatures
temperatures = [25.5, 28.1, 22.9, 30.2, 27.8, 24.3, 29.5]

#add 31.0 to the end of the list
temperatures.append(31.0)

#remove the third element from the list
temp=temperatures.pop(2)
print(temp)

print(f"modified_list: {temperatures}")
max_temperature = max(temperatures)
print(f"max temp: {max_temperature}")
min_temperature = min(temperatures)
print(f"min temp: {min_temperature}")

avg_temp = sum(temperatures)/len(temperatures)
print(f"average temp: {avg_temp:.2f}")