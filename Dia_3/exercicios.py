# Descobrindo se o número passado é par ou impar

# number = int(input("Which number do you want to check? "))

# result = number % 2

# if result == 0:
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

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
         print("Leap year")
else: 
    print ("Not leap year")