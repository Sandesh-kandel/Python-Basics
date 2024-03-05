import random
word_lsit = ["apple", "ball", "cat", "Dog", "Eagle"]
lives = 6
choosen_word = random.choice(word_lsit)
print(choosen_word)
display = []
for letter in range(len(choosen_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter:- ").lower()
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in choosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")
    if '_' not in display:
        game_over = True
        print("You win")
