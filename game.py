import random

def start_game():
    number = random.randint(1, 100)
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} tries.")
            break

if __name__ == "__main__":
    start_game()

