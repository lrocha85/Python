# Exercicio 1
#two_digit_number = input("Type a two digit number: ")

#print (int(two_digit_number[0]) + int(two_digit_number[1]))

## Operações matemáticas seguem uma prioridade, () ** * / + -, abaixo vai resolver primeiro a *, depois / e por último a -
#print (int(3 * 3 + 3 / 3 - 3))

## Abaixo eu forço a prioridade para a adição, depois a divisão para poder ter o resultado q quero, q é 3.
#print(3 * (3 + 3) / 3 - 3)

##Exercicio calculadora de IMC

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# imc = int(weight) / float(height) ** 2
# int_imc = int(imc)
# print (int_imc)

## NO exemplo abaixo eu pego o valor de a e multiplico por 2 com a sintax *= 2
# a = 2 + 2
# a *= 2 
# print (a)

## Usando f-String 

# status = True
# name = "Leandro"
# idade = 36
# altura = 1.7

# print("Parabéns", name, "Seu status é", status, "Sua idade é", idade, "Sua altura é", altura)

# print(f"Parabéns {name} Seu status é {status} Sua idade é {idade} Sua altura é {altura}")


# Calculadora de dias restantes para descobrir quantos dias, semanas e meses faltam da idade fornecida até se completarem 90 anos

# age = input("What is your current age?")
# max_age = 90
# dif_age = max_age - int(age)
# d = dif_age * 365 
# w = dif_age * 52
# m = dif_age * 12

# print (f"You have {d} days, {w} weeks, and {m} months left.")

# Projeto final aula 2, calculadora de conta com gorjeta

# print ("Welcome to the tip calculator.")
# total_bill = input("What was the total bill? ")
# tip = input("What percentage tip would you like to give?10 , 12, or 15? ")
# people_number = input("How many people to split the bill? ")

# total_tip = float(total_bill) * int(tip) /100
# full_bill = float(total_bill) + float(total_tip)
# split_valor = full_bill / int(people_number)
# print (f"Each person should pay: {round(split_valor,2)}")


