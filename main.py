# calculate height from average of heights
age = input("Enter the height in feet of five boys: ")
age_list = age.split(',')
count = 0

for _ in age_list:
    count += 1

for i in range(count):
    age_list[i] = float(age_list[i])

total = sum(age_list)
average = total / count

print("Total number of entries:", count)
print("Average height:", round(average))
