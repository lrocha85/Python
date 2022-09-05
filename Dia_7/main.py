# # Challenge 1
# import random

# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# guess = input("What is the letter? ").lower()

# for word in chosen_word:
#     if word == guess:
#         print("Right")
#     else:
#         print("Wrong")

# Programa completo da forca
import random
from replit import clear # Essa função limpa a tela a cada execução, para evitar barra de rolagem
from art import stages, logo
from words import words

print (logo)

print (stages[6])

end_of_game = False
chosen_word = random.choice(words)
word_length = len(chosen_word)
life = 6

display = []

for length in range(word_length):
    display += "_"

print (display)

while not end_of_game:
    guess = input("What is the letter? ").lower()

    clear ()

    if guess not in chosen_word:
        life -= 1
        (f"stages{life}\n{display}")
        
        if life == 0:
            end_of_game = True
            print ("You lose!")
            print (f"The word is: {chosen_word}")

    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

    if "_" not in display:
        end_of_game = True
        print ("You win!")
        print (f"The word is: {chosen_word}")
    print (f"{stages[life]}\n{display}")

    
