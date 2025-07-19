import random
minimum = 1
tries = 1

def display_heading():
    print("===========Welcome to the Guessing Game!===========")
    print(f"|Try to guess a random number between {minimum} and a number|")
    print("==================================================")
pass

def set_limit():
    while True:
        try:
            M = int(input("Enter the maximum number for the GuessingGame (greater than 1): "))
            if M > 1:
                return M
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


display_heading()
limit = set_limit()
secret_number = random.randint(minimum, limit)

def GuessingGame():
    global tries
    while True:
        guess = int(input(f"Guess the number between {minimum} and {limit}: "))
        if guess == secret_number:
            print("Correctamondo!")
            print(f"You guessed it in {tries} tries.")
            pass
            return
        elif guess < secret_number:
            print(f"Too low, try again! You are on try {tries}")
            pass
        else:
            print(f"Too high, try again! You are on try {tries}")
            pass
        tries += 1
    pass

def PlayAgain():
    global tries, secret_number, limit
    while True:
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again == 'y' or again == 'yes' or again == 'Y' or again == 'YES':
            tries = 1
            pass
            limit = set_limit()
            pass
            secret_number = random.randint(minimum, limit)
            GuessingGame()
        elif again == 'no' or again == 'n' or again == 'NO' or again == 'N':
            print("Thanks for playing!")
            break
        else:
            print("Please answer with 'y' or 'n'.")
            pass

GuessingGame()
PlayAgain()