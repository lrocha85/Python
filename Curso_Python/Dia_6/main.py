# Projeto final, Escaping the maze
# site https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world3.json&url=user_world%3Aproblem_world3.json

def move_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
      if right_is_clear():
         move_right()
         move()
      elif front_is_clear():
          move()
      else:
          turn_left()        
