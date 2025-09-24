import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
rounds = 5 

for round in range(rounds):
    user = input("Enter rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a Tie!😅 🤝")

    elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
        print("✅ You win → 🏆 🎉")
        user_score += 1


    else:
        print("❌ Computer wins → 🤖 💀")
        computer_score += 1


    print("Score --> You:", user_score, "Computer:", computer_score)

if user_score > computer_score:
    print("🎊 Congratulations! You won the game! 🎊")

elif user_score < computer_score:
    print("💻 Computer won the game! Better luck next time! 💻")

else:
    print("It's a draw! Well played! 🤝")

