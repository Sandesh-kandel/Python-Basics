import random
print("guess the number")
computer_guessed = random.randint(1, 50)
difficulty_level = input("enter a difficulty level 'hard' or  'easy':")
if difficulty_level == "easy":
    print("you have 10 chances")
    for i in range(1, 10):
        human_guessed_number = int(input("enter a no"))
        if computer_guessed == human_guessed_number:
            print("you are correct")
            break
        elif human_guessed_number > computer_guessed:
            print("your guess is more")
        elif human_guessed_number < computer_guessed:
            print("your guess is low")
        print(f"try again {9-i}")
elif difficulty_level == "hard":
    print("you have 5 chances")
    for i in range(1, 6):
        human_guessed_number = int(input("enter a no"))
        if computer_guessed == human_guessed_number:
            print("you are correct")
            break
        elif human_guessed_number > computer_guessed:
            print("your guess is more")
        elif human_guessed_number < computer_guessed:
            print("your guess is low")
        else:
            print(f"try again {4-i}")
