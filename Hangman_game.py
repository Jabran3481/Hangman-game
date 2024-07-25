import random

with open('words.txt','r') as file:
    data = file.read().strip()
    words = data.split()
word = random.choice(words).lower()

total_chances = 7
guessed_word = '_'*len(word)

while total_chances !=0:

    print(guessed_word)
    letter = input("enter a letter ").lower()
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single letter.")
        continue
    if letter in word:
        guessed_list = list(guessed_word)
        for index in range(len(word)):
            if word[index] == letter:
                guessed_list[index] = letter

                print(guessed_word)
        guessed_word = ''.join(guessed_list)
        if guessed_word == word:
            print("congratulations you won")
            break
    else:
        total_chances -= 1
        print("incorrect guess")
        print("the remaining chances are ",total_chances)

else:
    print("Game over")
    print("YOu loose")
    print("All the chances are exhausted")
    print("The correct word is ",word)