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
def prime_checker(number):
    if number > 1: # Número 1 nunca é impar
        for i in range(2, number): # Vai testar se o número escolhido é totalmente divisível por 2-até o número
# anterior a ele mesmo, exemplo, se o número escolhido for 6, vai testar 6/2 6/3 6/4 e 6/5, se for totalmente divisível por alguma, não é número primo            
            if (number % i) == 0:
                return print ("It's not a prime number")                
        return print ("It's a prime number.")
    else:
        return print ("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
