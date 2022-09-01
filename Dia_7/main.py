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

# Challenge 2
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print (stages[6])

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
life = 6

display = []

for length in range(word_length):
    display += "_"

print (display)

while not end_of_game:
    guess = input("What is the letter? ").lower()

    if guess not in chosen_word:
        life -= 1
        (f"stages{life}\n{display}")
        
        if life == 0:
            end_of_game = True
            print ("You lose!")

    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

    if "_" not in display:
        end_of_game = True
        print ("You win!")
    print (f"{stages[life]}\n{display}")

    
