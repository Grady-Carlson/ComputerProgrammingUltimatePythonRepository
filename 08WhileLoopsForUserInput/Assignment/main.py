import random
number = random.randint(1,10)
number2 = random.randint(1,10)
correct = False
correct2 = False
lives = 3

print("")
print("Number Guesser:")
while correct == False:
    print("Guess a the random Number 1-10:")
    checker2 = input()
    if checker2 in ("12345678910"):
        guess = int(checker2)
        if guess == number:
            correct = True
        elif guess > number:
            print("Too High, Try Again")
        elif guess < number:
            print("Too Low, Try Again")
    else:
        print("Make sure to enter a valid guess!")
        
print("Correct! You Win.")    
print("")

print("Number Guesser with Lives:")
while correct2 == False:
    if lives == 0:
            correct2 = True
    else:
        print("You have",lives, "lives left.")
        print("Guess a the random Number 1-10:")
        checker = input()
        if checker in ("12345678910"):
            guess2 = int(checker)
            if guess2 == number2:
                correct2 = True
            elif guess2 > number2:
                print("Too High, Try Again")
                lives = lives - 1
            elif guess2 < number2:
                print("Too Low, Try Again")
                lives = lives - 1
        else:
            print("Make sure to enter a valid Guess!")

if lives == 0:
    print("Game Over, You ran out of Lives") 
    print("")
else:
     print("Correct! You Win. You had",lives,"lives left.")     
     print("") 

amount = 0
print("You owe 50 cents, insert coins to pay")
while amount < 50:
    print("Insert Coin")
    checker = input()
    if checker in ("25", "10", "5"):
        coin = int(checker)
        if coin == 25:
            amount = amount + 25
            print("You have paid", amount,"cents so far.")
        elif coin == 10:
            amount = amount + 10
            print("You have paid", amount,"cents so far.")
        elif coin == 5:
            amount = amount + 5
            print("You have paid", amount,"cents so far.")
    else:
            print("Please Enter a valid Coin")

change = amount - 50
print("You have successfully bought your snack, your change is", change, "cents")