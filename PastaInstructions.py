# import time


# name = input("What's your name? \n")
# print(f'Hello, {name}! Here is how to make pasta')
# time.sleep(2)
# print("1. Boil some water")
# time.sleep(2)
# print("2. Wait ~5 minutes until the water boils")
# time.sleep(2)
# print("3. Add salt to water")
# time.sleep(2)
# print("4. Add pasta")
# time.sleep(2)
# print("5. Cook pasta for 10 minutes until 'Al dente'")
# time.sleep(2)
# print("6. Remove water")
# time.sleep(2)
# print("Done")

























import random
import time


greetList : list[str] = [
    "Hello, ",
    "Salutations, ",
    "Nice to see you again, ",
    "Welcome back, "
]

greetPastaList : list[str] = [
    "! Here's how to make pasta",
    "! This is how you make pasta",
    "! Pasta is a very simple dish, this is how you can make them",
    "! Simple pasta recipe coming up "
]

insList : list[str] = [
    "1. Boil some water",
    "2. Wait ~5 minutes until the water boils",
    "3. Add salt to water",
    "4. Add pasta",
    "5. Cook pasta for 10 minutes until 'Al dente'",
    "6. Remove water",
    "Done"
]

name      : str = input("What's your name? ")
randGreet : str = greetList[random.randint(0,3)]
randPasta : str = greetPastaList[random.randint(0,3)]
print(randGreet, name, randPasta)
time.sleep(2)
for data in insList:
    print(data)
    time.sleep(2)