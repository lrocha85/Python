def list (num_user):
    arr = [2,3,4,3,2,1]
    cont = 0
    num_user = int(num_user)
    num = 0

    for num in arr:
       if num_user == num:
            cont = cont + 1
    return cont
        

num_user = input("What number?: ")

number = list(num_user)

print(number)