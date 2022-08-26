# Exercicio 1
#two_digit_number = input("Type a two digit number: ")

#print (int(two_digit_number[0]) + int(two_digit_number[1]))

## Operações matemáticas seguem uma prioridade, () ** * / + -, abaixo vai resolver primeiro a *, depois / e por último a -
#print (int(3 * 3 + 3 / 3 - 3))

## Abaixo eu forço a prioridade para a adição, depois a divisão para poder ter o resultado q quero, q é 3.
#print(3 * (3 + 3) / 3 - 3)

##Exercicio calculadora de IMC

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

imc = int(weight) / float(height) ** 2
int_imc = int(imc)
print (int_imc)