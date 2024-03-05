# import random
# dice_number = ["one", "two", "three", "four", "five", "six"]
# dice_num = random.randint(0, 6)
# print(dice_number[dice_num])


year = int(input("your born year? "))
if year > 1980 or year < 1996:
    print("You're milinial")
elif year > 1996:
    print("You're Gen Z")
