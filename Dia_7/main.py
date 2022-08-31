# Challenge 1
import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("What is the letter? ").lower()

for word in chosen_word:
    if word == guess:
        print("Right")
    else:
        print("Wrong")

