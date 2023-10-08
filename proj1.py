import random

name = input("What is your name?")
age = input("What is your age?")
car = input("What is your car?")
cargood = random.randint(1,2)

print(name + age)
if cargood == 1:
    print(car + " bad")
if cargood == 2:
    print(car + " good")




