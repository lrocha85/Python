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

# Calculator

# from replit import clear

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

# def calculadora():
 
#     num1 = float(input("What's the firt number?: "))

#     for item in operations:
#         print(item)

#     loop = True

#     operator= input("What operator do you want to do?: ")

#     num2 = float(input("What's the second number?: "))

#     calculator = operations[operator]

#     answer = float(calculator(num1, num2))

#     print (f"{num1} {operator} {num2}: {answer}")

#     while loop is True:

#         question = input(f"Do you have another operation with the number {answer}? yes or no: ")

#         if question == "yes":
#             clear()
#             for item in operations:
#                 print(item)

#             operator= input(f"What operator do you want to do with the number {answer}?: ")    
#             num3 = float(input("What's the next number?: "))
#             calculator = operations[operator]
#             second_answer = float(calculator(answer, num3))

#             print (f"{answer} {operator} {num3}: {second_answer}")
#             answer = second_answer
#         else:
#             loop = False
#             print("FIM")
# calculadora()

## Projeto final da aula, o jogo 21

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random
from replit import clear

endgame = False

while endgame == False:
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return (card)

    def calculate_score(cards):
        num_len = len(cards)
        num = 0
        sum = 0 
        
        for num in (cards):     
            sum += num
        return sum

    def get_print(): # <- define a função print(void) void pq não recebe argumento
        print(f"User Cards: {user_cards}, Total User Score: {user_score} ") # <- chama a função print passando argumento
        print(f"Computer Cards: {computer_cards}, Total Computer Store: {computer_score}")

    user_cards = []
    computer_cards = []

    for _ in range(2):   
        new_user_cards = deal_card()
        user_cards.append(new_user_cards)
        new_computer_cards = deal_card()
        computer_cards.append(new_computer_cards)

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"User Cards: {user_cards}, Total User Score: {user_score} ")

    if computer_score == 21:
        endgame = True
        print ("Computer has blackjack")
    if user_score == 21:
        endgame = True
        get_print()
        print ("User has blackjack")

    while endgame is False:

        draw_card = input("Do you want to draw another card? y or n: ")

        if draw_card == "y":
            user_new = deal_card()
            if user_new == 11:
                if user_new + user_score >21:
                    user_new = 1
            user_cards.append(user_new)            
            user_score = calculate_score(user_cards)            
            print(f"User Cards: {user_cards}, Total User Score: {user_score} ")
            if user_score >21:
                endgame = True
                print ("User Loss")
        if draw_card == "n":
            while computer_score <17:            
             computer_new = deal_card()
             computer_cards.append(computer_new)
             computer_score = calculate_score(computer_cards)
            if computer_score >21:
                endgame = True
                get_print()
                print ("User Win")
            else:
                if user_score == computer_score:
                    endgame = True
                    get_print()
                    print ("The game is Draw")
                if user_score > computer_score:
                    endgame = True
                    get_print()
                    print ("User Win")
                if computer_score > user_score:
                    endgame = True
                    get_print()
                    print ("User Loss")

    again = input("Do you want play again? y or n: ")

    if again == "y":
        clear()
        endgame = False 
    
clear()
print("End Game")