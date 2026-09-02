import random

target = random.randint(1, 99)

while True:
    userchoice = int(input("Guess the target:"))
    if(userchoice == target):
        print("succes : correct guess!!")
        break
    elif(userchoice < target):
        print("your number was too small. Take a bigger guess..")
    else:
        print("your number was too big. Take a smaller guess..") 

print("-----GAME OVER-----")           