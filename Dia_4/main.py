## Trabalhando com números randomicos - https://www.askpython.com/
# import random

# random_int = random.randint(1, 10)
# print(random_int)

# random.float = random.random()

# print(random.float)

# random.uni = random.uniform(1, 10)

# print(random.uni)
# import random

# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# number = random.randint(0, 1)

# if number == 0:
#     print("Tails")
# else:
#     print("Heads")

## Exercise 2 - Banker Roulette

# import random
# test_seed = int(input("Create a seed number: ")) # Apenas iniciando o seed
# random.seed(test_seed)

# names_string = input("Give me everybody's names, separated by a ,. ")
# names = names_string.split(", ") # A função split separa os nomes que passei e coloca na lista

# i = (len(names)) # Aqui estou contando quantos elementos tenho na minha lista

# num = random.randint(0, (i-1)) # Estou gerando um número randomico entre 0, primeiro item da lista, e i-1, q é o número total de elementos na lista -1 pq a lista começa com 0

# bucha = names[num] # Buscando um nome aleatório na lista

# print (f"{bucha} is going to buy the meal today!")

# ## Trabalhando com lista dentro de lista
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1])
# print(dirty_dozen[0])
# print(dirty_dozen[1][2])
# print(dirty_dozen[0]+dirty_dozen[1])

## Exercise 3 - Treasure Map

# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# h = int(position[0])
# v = int(position[1])

# map[v -1] [h -1] = "X"

# print(f"{row1}\n{row2}\n{row3}")

## Projeto final do dia

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if human_choice >= 3 or human_choice < 0:
    print ("You typed an invalid number, you lose!")
else:

    pc_choice = int(random.randint(0, 2))

    images = [rock, paper, scissors]

    print(images[human_choice])

    print (f"\nComputer chose: \n{images[pc_choice]}")

    if human_choice == 0:
        if pc_choice == 0:
            print ("Draw")
        elif pc_choice == 1:
            print ("You lose")
        else:
            print ("You win")
    elif human_choice == 1:
        if pc_choice == 0:
            print("You win")
        elif pc_choice ==1:
            print ("Draw")
        else:
            print ("You lose")
    else:
        if pc_choice == 0:
            print ("You lose")
        elif pc_choice == 1:
            print("You win")
        else:
            print ("Draw")

