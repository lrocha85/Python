# Exercise 1 - Paint Area Calculator 
# Criando uma função para calcular a quantidade de tinta necessária, o modulo math vai arredondar para cima o número final do cálculo
# import math
# def paint_calc(height, width, cover):
#     total = (height * width)/cover
#     print (f"You'll need {math.ceil(total)} cans of paint.")

# # Aqui eu chamo a função passando os argumentos necessários para o cálculo, depois de capturar os valores do usuário
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

#Exercise 2 - Prime Numbers:
# def prime_checker(number):
#     if number > 1: # Número 1 nunca é impar
#         for i in range(2, number): # Vai testar se o número escolhido é totalmente divisível por 2-até o número
# # anterior a ele mesmo, exemplo, se o número escolhido for 6, vai testar 6/2 6/3 6/4 e 6/5, se for totalmente divisível por alguma, não é número primo            
#             if (number % i) == 0:
#                 return print ("It's not a prime number")                
#         return print ("It's a prime number.")
#     else:
#         return print ("It's not a prime number.")

# n = int(input("Check this number: "))
# prime_checker(number=n)

# fruits = [4, 55, 64, 32, 16, 32]

# x = fruits.index(32) # Função index mostra a posição do item passado na lista

# print (x)

## caesar-cipher-1-start

# from operator import index
# from tkinter import N


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))



# def encrypt(text, shift):
#     final_text = ""
#     for i in (text):
#         word = alphabet.index(i)
#         word_encode = word + shift
#         final_text += alphabet[word_encode]
#     print(f"The encoded text is {final_text}")

# def decrypt(text, shift):
#     final_text = ""
#     for i in (text):
#         word = alphabet.index(i)
#         word_encode = word - shift
#         final_text += alphabet[word_encode]
#     print(f"The encoded text is {final_text}")

# if direction == "encode":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)

## Juntando as 2 funções acima em 1 só chamada cesar:

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

reload = ""
end = False

def cesar(text, shift, direction):
    final_text = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        if i in alphabet:
            word = alphabet.index(i)
            new_word = word + shift
            final_text += alphabet[new_word]
        else:
            final_text += i
    print (f"Here's the {direction}d result: {final_text} ")

from operator import index
from art import logo

print (logo)

while not end:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    cesar(text=text, shift=shift, direction=direction)

    reload = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")   

    if reload == "no":
        end = True
        print("Goodbye")
