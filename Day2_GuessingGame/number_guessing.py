import random

def number_guessing():
    number = random.randint(1, 100)  # 1 to 100 random number generate
    attempts = 0

    print("🎯 Welcome to Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!\n")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("📉 Too low! Try again.\n")
        elif guess > number:
            print("📈 Too high! Try again.\n")

        elif guess == number:
            print(f"✅ Correct! The number was {number}.")
            print("🎉 Congratulations! You've guessed the number!")
            print(f"🎉 You guessed it in {attempts} attempts!\n")
            break

        if attempts >= 10:
            print(f"💥 You've used all 10 attempts! The number was {number}. Better luck next time!\n")
            break

        else:
            print(f"Attempts left: {10 - attempts}\n")

        
number_guessing()
