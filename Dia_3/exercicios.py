# Descobrindo se o número passado é par ou impar

# number = int(input("Which number do you want to check? "))

# result = number % 2 

# if result == 0: - aqui verifico se sobra algum produto, exemplo: se estou testando o número 6, é o mesmo de 2 + 2 + 2 =6, então sobra 0. Se eu testar 5, seria 2+ 2+ 1, pq eu pedi o modulo (%)
# para dividir em porções de 2, então no caso vai sobrar esse 1.
#     print ("This is an even number.")
# else:
#     print ("This is an odd number.")

# Utilizando elif

# height = int (input("What's your height in cm? "))

# if height >= 120:
#     print("You can ride")
#     age = int(input("What's your age? "))
#     if age < 12: # Só vai entrar no teste de idade se a condição de altura for true
#         print("You pain 5$")
#     elif age < 18: # Se a idada é menor q 18 e maior que 12
#         print( "You pain 7$")
#     else:
#         print( "You pain 12$")
# else:
#     print("You can't ride, sorry")


## Fazer calculadora de peso versão 2
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))


# imc = round(weight / height ** 2)

# if imc < 18.5:
#     print (f"Your BMI is {imc}, you are underweight.")
# elif imc < 25:
#     print (f"Your BMI is {imc}, you have a normal weight.")
# elif imc < 30:
#     print (f"Your BMI is {imc}, you are slightly overweight .")
# elif imc < 35:
#     print (f"Your BMI is {imc}, you are slightly overweight .")
# else:
#     print (f"Your BMI is {imc}, you are clinically obese.")

# Exercício para descobrir se o ano é bissexto
# year = int(input("Which year do you want to check? "))

# if year % 4 == 0: # Uso o módulo para dividir o ano em porções de 4, se o resto for 0, p número é totalmente dividido por 4
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#          print("Leap year")
# else: 
#     print ("Not leap year")

## Melhorando o código do parque

height = int (input("What's your height in cm? "))

if height >= 120:
    print("You can ride")
    age = int(input("What's your age? "))
    bill = 0
    if age < 12: # Só vai entrar no teste de idade se a condição de altura for true
        print("The value of ticket is 5$")
        bill = 5
    elif age < 18: # Se a idada é menor q 18 e maior que 12
        print( "The value of ticket is 7$")
        bill = 7
    else:
        print( "The value of ticket is 12$")
        bill = 12
    want_photo = input("Do you want a photo? ")
    if want_photo == "y":
        bill += 3 
    print (f"Your bill is {bill}")
else:
    print("You can't ride, sorry")