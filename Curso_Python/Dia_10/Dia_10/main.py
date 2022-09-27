# def format_name(f_name, l_name):
#     f_name = f_name.title() # .title is used to format the result to title form, like leadro rocha = Leandro Rocha, with first word up case
#     l_name = l_name.title()
#     return f"{f_name} {l_name}"


# name = format_name("leandro","rocha")

# print (name)

## Exercise 1 - Days in Month

# def is_leap(year):

#     if year % 4 == 0: # Uso o módulo para dividir o ano em porções de 4, se o resto for 0, p número é totalmente dividido por 4
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else: 
#         return False



# def days_in_month(year, month):
#   month -= 1
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   leap = is_leap(year)
#   if leap is True:
#       if month == 1:
#           days = 29      
#           return days
#   return month_days[month]
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# # Calculator

# #Add
# def add(n1,n2):
#     return n1 + n2

# #Sub
# def sub(n1,n2):
#     return n1 - n2

# #Mult
# def mult(n1,n2):
#     return n1 * n2

# #Div
# def div(n1,n2):
#     return n1 / n2

# operations = {
#     "+" : add,
#     "-" : sub,
#     "*" : mult,
#     "/" : div
# }

# num1 = int(input("What's the firt number?: "))

# for item in operations:
#     print(item)

# operator= input("What operator do you want to do?: ")

# num2 = int(input("What's the second number?: "))

# calculator = operations[operator]

# answer = calculator(num1, num2)

# print (f"{num1} {operator} {num2}: {answer}")

# question = input("Do you have another operation? yes or no: ")

# if question == "yes":
#     for item in operations:
#         print(item)

#     operator= input("What operator do you want to do?: ")    
#     num3 = int(input("What's the next number?: "))
#     calculator = operations[operator]
#     second_answer = calculator(answer, num3)

#     print (f"{answer} {operator} {num3}: {second_answer}")