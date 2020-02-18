# guess secret word
# you will get 10 attemps
# if you guess right latter of the secret word then your attempt will not be counted or else your attempt will reduce one by one if you guess wrong letter

import time

name = input("whats your name?")

print("hello", name, "time to play hangman!")
print("")

time.sleep(1)

print()
"start gussin...."
time.sleep(0.5)

word = "secret"
word_chars = set(word)

guesses = set()
turns = 10

# while turns > 0 :
#     failed = 0
#     for char in word:
#          if char in guesses:
#              print(char),

#          else:
#             print("_")
#             failed +=1

#     if failed == 0:
#         print("you won hahaha")
#         break

print()

while True:
    guess = input("guess a chr dudeeee:")

    guesses.add(guess)

    if guess not in word:
        turns -= 1

        print("its wrong")

    print("you got", + turns, "more guesses")

    if turns == 0:
        print("phewww !!! you loseeee")
        break

    if guesses > word_chars:
        print("wWHOOHOOOOOOOOOOOOOOOOO! YOU WONT DUDEEE AHHAAHA!")
        break
