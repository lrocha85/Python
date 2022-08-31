
#Exercise 1 - Average Height - Pegar os números passados, separar e criar uma lista com eles, depois pegar a soma desses números e dividir pela quantidade de itens nessa lista
# # Não pode usar sum() nem len()
# student_heights = input("Input a list of student heights ").split()
# total = 0
# i = 0
# for n in student_heights:
#     n = int(n)
#     total += n
#     i += 1
# print (round(total/(i)))


## Exercise 2 - High Score
student_scores = input("Input a list of student scores ").split()
highest = 0
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if student_scores[n] > highest:
    highest = student_scores[n]
print (f"The highest score in the class is: {highest}")


