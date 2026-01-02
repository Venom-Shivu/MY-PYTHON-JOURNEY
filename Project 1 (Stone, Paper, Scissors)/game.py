import random

# ==========================================
#        STONE | PAPER | SCISSORS
#        Console-Based Game (Python)
# ==========================================

VALID_CHOICES = ("stone", "paper", "scissors")
SEPARATOR = "-" * 42


def display_header():
    """Displays the game title."""
    print("\n" + SEPARATOR)
    print("        STONE  |  PAPER  |  SCISSORS")
    print(SEPARATOR)


def get_user_choice():
    """
    Prompts the user for input and validates it.
    Returns a valid choice.
    """
    while True:
        choice = input("Enter your move (stone / paper / scissors): ").strip().lower()
        if choice in VALID_CHOICES:
            return choice
        print("Invalid input. Please try again.\n")


def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(VALID_CHOICES)


def determine_winner(user, computer):
    """
    Determines the game outcome based on user and computer choices.
    Returns the result as a string.
    """
    if user == computer:
        return "It's a TIE!"

    if (
        (user == "stone" and computer == "scissors") or
        (user == "paper" and computer == "stone") or
        (user == "scissors" and computer == "paper")
    ):
        return "YOU WIN!"

    return "COMPUTER WINS!"


def play_game():
    """Runs a single round of the game."""
    display_header()

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose      : {user_choice}")
    print(f"Computer chose : {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    print(f"\nRESULT: {result}")
    print(SEPARATOR)


def main():
    """Main program loop."""
    while True:
        play_game()
        replay = input("Play again? (y/n): ").strip().lower()
        if replay != "y":
            print("\nGame Over. Thanks for playing!\n")
            break


if __name__ == "__main__":
    main()
