import random

target = random.randint(1, 10)

while True:
    userchoice = input("Guess the target or quite:")

    if(userchoice == "Quite"):
       
        break
    userchoice = int(userchoice)
    if(userchoice == target):
        print("success : correct Guess!")
        break

    elif(userchoice < target):
        print("your number was too small. Take a bigger guess..")
    else:
        print("your number was too big. Take a smaller guess..") 

print("-----GAME OVER-----")           