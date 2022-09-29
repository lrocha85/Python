#Exercise 1 - Grading Program

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# for name in student_scores:
#     score = student_scores[name]
#     if score <=70 :
#         student_grades[name] = "Fail"
#     elif score <=80:
#         student_grades[name] = "Acceptable"
#     elif score <90:
#         student_grades[name] = "Exceeds Expectations"
#     else:
#         student_grades[name] = "Outstanding"

# print(student_grades)

## Exercise 2 - Dictionary in List

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]



# def add_new_country(country,visits,cities):
#     travel_log.append(
#         [{"country": country,
#          "visits": visits,
#          "cities": cities}]
#     )
 

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# Final program class 9

from replit import clear
from art import logo

fim_leilao = False

highest= 0.0
winner = ""

print (logo)

def leilao (name, price):
    global highest # If i'm not add "global", It is return a error because the variable highest did not start on def.
    global winner
   
    if price > highest:
        winner = name
        highest = price
        
           
name = input("What is your name? ")
price = float(input("What is your bid price? "))

leilao(name, price)

more_player = input("Are there more users who want to bid? yes or no ") 
if more_player == "no":
    print(f"The Winner is {winner}, with the valor: {highest}")  
    fim_leilao = True
clear

