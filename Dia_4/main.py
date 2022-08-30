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

import random
test_seed = int(input("Create a seed number: ")) # Apenas iniciando o seed
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a ,. ")
names = names_string.split(", ") # A função split separa os nomes que passei e coloca na lista

i = (len(names)) # Aqui estou contando quantos elementos tenho na minha lista

num = random.randint(0, (i-1)) # Estou gerando um número randomico entre 0, primeiro item da lista, e i-1, q é o número total de elementos na lista -1 pq a lista começa com 0

bucha = names[num] # Buscando um nome aleatório na lista

print (f"{bucha} is going to buy the meal today!")

