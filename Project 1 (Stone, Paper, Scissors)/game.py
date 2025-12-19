import random

                                    # ==========================================
                                    #    STONE PAPER SCISSORS - CONSOLE GAME
                                    # ==========================================

# Using string multiplication "-" * 42 creates a neat visual border
print("\n" + "-" * 42)
print("        STONE  |  PAPER  |  SCISSORS")
print("-" * 42)


# ------------------------------------------
# Get player's choice
# ------------------------------------------
# .strip() removes accidental spaces at start/end
# .lower() converts "Stone" to "stone" for easy comparison or if the user inputs upper case
user_choice = input("Enter your move (stone / paper / scissors): ").strip().lower()


# ------------------------------------------
# Input Validation
# ------------------------------------------
# Storing choices in a list makes it easy to check if the input is correct
valid_choices = ["stone", "paper", "scissors"]

if user_choice not in valid_choices:
    print("\nInvalid input! Please enter stone, paper, or scissors.")
    print("-" * 42)
    exit() # This command terminates the program early if the user messes up


# ------------------------------------------
# Generate computer's choice
# ------------------------------------------
# random.choice() picks a random item directly from our list
computer_choice = random.choice(valid_choices)

print(f"\nYou chose      : {user_choice}")
print(f"Computer chose : {computer_choice}")


# ------------------------------------------
# Game decision logic
# ------------------------------------------
# Step 1: Check for a Tie first
if user_choice == computer_choice:
    result = "It's a TIE!"

# Step 2: Use Parentheses and 'or' to group all winning scenarios
# This is called 'Compound Conditional Logic'
elif (
    (user_choice == "stone" and computer_choice == "scissors") or # Stone crushes the Scissors.
    (user_choice == "paper" and computer_choice == "stone") or    # Paper wraps the Stone.
    (user_choice == "scissors" and computer_choice == "paper")    #Scissors cut the Paper
):
    result = "YOU WIN!"

# Step 3: If it's not a tie and you didn't win, the only remaining option is a loss
else:
    result = "COMPUTER WINS!"


# ------------------------------------------
# Display result
# ------------------------------------------
print(f"\nRESULT: {result}")
print("-" * 42)
print("Game Over. Thanks for playing!\n")                                   