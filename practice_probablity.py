import random
names = []
names = input("Enter the name of friends in the circle: "). split()
length = len(names)
random_choice = random.randint(0, length-1)
print(f"{names[random_choice]} will pay the bills")


probablity_of_paying = random.random()
if probablity_of_paying < 0.5:
    print(f"{names[0]} will pay the bills")
else:
    print(f"{names[random_choice]} will pay the bills")
