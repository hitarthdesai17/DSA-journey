while True:
    print("Hello")
    userinput = input("Yes/No: ").lower()

    if userinput != "yes":
        break

#Python doesnt have do while so we create an infinite loop and tell it when to break
print("---Guess The Number---")
import random
comp = random.randint(1,100)
while True:
    try:
        guess = int(input("Guess a number: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    if guess<1 or guess>100:
        print("Enter number between 1 to 100")
        continue
    if(guess<comp):
        print("too low!")
    elif(guess>comp):
        print("too High")
    else:
        print("Congrats, Correct Guess")
        break