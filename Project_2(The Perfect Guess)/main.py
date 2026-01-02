import random
import os


class PerfectGuessGame:
    """
    A number guessing game that demonstrates:
    - OOP design
    - Input validation
    - Difficulty levels
    - Persistent high score tracking
    """

    SCORE_FILE = "high_score.txt"

    def __init__(self):
        self.target_number = None
        self.attempts = 0
        self.max_range = 0

    def select_difficulty(self):
        """Allows the user to choose a difficulty level."""
        print("\nChoose Difficulty:")
        print("1. Easy   (1 - 50)")
        print("2. Medium (1 - 100)")
        print("3. Hard   (1 - 500)")

        while True:
            choice = input("Enter choice (1/2/3): ").strip()
            if choice == "1":
                self.max_range = 50
                break
            elif choice == "2":
                self.max_range = 100
                break
            elif choice == "3":
                self.max_range = 500
                break
            else:
                print("Invalid choice. Try again.")

        self.target_number = random.randint(1, self.max_range)

    def get_high_score(self):
        """Reads the best score from file, if it exists."""
        if os.path.exists(self.SCORE_FILE):
            with open(self.SCORE_FILE, "r") as file:
                return int(file.read())
        return None

    def save_high_score(self, score):
        """Saves the best score to file."""
        with open(self.SCORE_FILE, "w") as file:
            file.write(str(score))

    def play(self):
        """Main game loop."""
        self.select_difficulty()
        print(f"\nI have selected a number between 1 and {self.max_range}. Start guessing!")

        while True:
            guess = input("Your guess: ").strip()

            if not guess.isdigit():
                print("Please enter a valid number.")
                continue

            guess = int(guess)
            self.attempts += 1

            if guess < self.target_number:
                print("Too low.")
            elif guess > self.target_number:
                print("Too high.")
            else:
                print(f"\nCorrect! You guessed it in {self.attempts} attempts.")
                self.update_score()
                break

    def update_score(self):
        """Updates high score if the current score is better."""
        high_score = self.get_high_score()

        if high_score is None or self.attempts < high_score:
            print("🎉 New High Score!")
            self.save_high_score(self.attempts)
        else:
            print(f"Best Score: {high_score} attempts")


# -------------------------------
# Program Entry Point
# -------------------------------

if __name__ == "__main__":
    while True:
        game = PerfectGuessGame()
        game.play()

        replay = input("\nPlay again? (y/n): ").strip().lower()
        if replay != "y":
            print("Thanks for playing!")
            break
