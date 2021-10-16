# If the Player guess is too higher than the actual number the program will display "Lower Number please". If the player guess too Lower than the actual program will display "Higher number please"
# when the player guess the right number, program will display the number of times he required to guess the right number. create a file highscore.txt and save the highscore only

import random
randNumber = random.randint(1 , 100)
#print(randNumber)
userGuess = 0
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if (userGuess == randNumber):
        print("You guessed is right!")
    else:
        if (userGuess < randNumber):
            print("your guess is wrong! Enter a Larger number: ")    
        else:
            print("your guess is wrong! Enter a Smaller number: ")  
        

print(f"You guessed the number in {guesses} guesses")        
with open('highscore.txt') as f:
    highscore = int(f.read())

if (guesses<highscore):
    print("You have Broken the Highscore!")
    with open("highscore.txt", 'w') as f:
        f.write(str(guesses))    