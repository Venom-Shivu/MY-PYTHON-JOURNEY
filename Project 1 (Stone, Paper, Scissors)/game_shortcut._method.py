import random

# ==========================================
#      ROCK | PAPER | SCISSORS (Optimized)
# ==========================================

CHOICES = ("Rock", "Paper", "Scissors")
RESULTS = ("Tie!", "Computer Wins!", "You Win!")


def get_user_choice():
    """
    Safely obtains and validates user input.
    Returns an integer in range [0, 2].
    """
    while True:
        try:
            choice = int(input("Enter 0 (Rock), 1 (Paper), or 2 (Scissors): "))
            if choice in (0, 1, 2):
                return choice
            print("Invalid choice. Please enter 0, 1, or 2.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")


def play_round():
    """Plays one round of Rock-Paper-Scissors."""
    user_choice = get_user_choice()
    computer_choice = random.randint(0, 2)

    # Core optimized logic (your idea, preserved)
    outcome_index = (computer_choice - user_choice) % 3

    print(f"\nYou       : {CHOICES[user_choice]}")
    print(f"Computer  : {CHOICES[computer_choice]}")
    print(f"Result    : {RESULTS[outcome_index]}")
    print("-" * 40)


def main():
    """Main game loop."""
    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\nGame Over. Thanks for playing!")
            break


if __name__ == "__main__":
    main()
