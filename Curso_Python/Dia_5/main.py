
#Exercise 1 - Average Height - Pegar os números passados, separar e criar uma lista com eles, depois pegar a soma desses números e dividir pela quantidade de itens nessa lista
# # Não pode usar sum() nem len()
student_heights = input("Input a list of student heights ").split()
total = 0
i = 0
for n in student_heights:
    n = int(n)
    total += n
    i += 1
print (round(total/(i)))


# ## Exercise 2 - High Score
student_scores = input("Input a list of student scores ").split()
highest = 0
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if student_scores[n] > highest:
    highest = student_scores[n]
print (f"The highest score in the class is: {highest}")


## Exercise 3 - Adding Even Numbers - Criar programa para somar todos os números pares de 2 a 100 e imprimir o total, além de imprimir a lista com todos os números somados

total = 0
lista = [0]
for number in range(2, 101, 2):
    total += number
    lista.append(number)
print (total)
print (lista)


# #Exercise 4 - FizzBuzz # Imprimir numeros de 1 a 100, se o numero for divisível por 3, imprimi "Fizz" no lugar do número
# # se for divisível por 5, Buzz e se for divisível por 3 e por 5, imprimi FizzBuzz
for number in range (1, 101):
    if number % 3 == 0:
        if number % 5 ==0:
            print ("FizzBuzz")
        else:    
            print ("Fizz")
    elif number % 5 == 0:
        print ("Buzz")
    else:
        print (number)

## Projeto final: password-generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_letters = ""
lista = []
for l in range(1, nr_letters + 1): # de 1 até o número de letras escolhido acima, pego 1 letra aleatória na lista letters e adiciono na variável lista.
    total_letters = random.choice(letters)
    lista += total_letters

total_symbols = ""
for s in range(1, nr_symbols + 1): # de 1 até o número de símbolos escolhido acima, pego 1 símbolo aleatório na lista symbols e adiciono na variável lista.
    total_symbols = random.choice(symbols)
    lista += total_symbols

total_numbers = 0
for n in range(1, nr_numbers + 1 ): # de 1 até o número de números escolhidos acima, pego 1 número aleatório na lista numbers e adiciono na variável lista.
    total_numbers = random.choice(numbers)
    lista += total_numbers

random.shuffle(lista) # Aqui uso a função shuffle para embaralhar a lista

password = "" 
for char in lista: # Jogo todos os itens da lista em 1 única variável para poder imprimir certinho
    password += char

print (f"Here is your password: {password}")
