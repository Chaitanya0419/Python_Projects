import random

m = input("you want to play guessing game?Yes/No : ")
num = random.randint(0, 100)
count=0
if m == "Yes":
    while True:
        n = int(input("enter a number"))
        if n == num:
            print("your guess is correct u reached the target",)
            break
        elif n < num:
            print("your number is lesser than target",)
        else:
            print("your number is greater than target",)
            count=count+1
            if(count==5):
                print("Try Again Later")
                print("______GAME OVER______")
                break

else:
    print("______GAME OVER______")
