
import random
import time


responseList : list[str] = [
    "Hello, ",
    "Salutations, ",
    "Nice to see you again, ",
    "Welcome back, "
]

name    : str = input("What's your name? ")
randRes : str = responseList[random.randint(0,3)]
print(randRes, name)
time.sleep(2)
sport : str = input("What's your favorite sport? ")
time.sleep(2)
print("Your favorite sport is ", sport)

