import random

# ------------------------------------------
# 1. CONSTANT DEFINITIONS
# ------------------------------------------
# Index-based mapping keeps logic compact and avoids long if-else blocks
CHOICES = ["Rock", "Paper", "Scissors"]

# Result mapping based on modular arithmetic outcome
# 0 → Tie
# 1 → Computer wins
# 2 → User wins
RESULTS = ["Tie!", "Computer Wins!", "You Win!"]


# ------------------------------------------
# 2. USER & COMPUTER INPUT
# ------------------------------------------
user_choice = int(input("Enter 0 (Rock), 1 (Paper), or 2 (Scissors): "))
computer_choice = random.randint(0, 2)


# ------------------------------------------
# 3. CORE GAME LOGIC (SHORTCUT)
# ------------------------------------------
"""
Logic Explanation (This is the key part):

We assign numbers:
Rock = 0, Paper = 1, Scissors = 2

We compute:
    (computer_choice - user_choice) % 3

Why this works:
------------------------------------------------
Case 1: Same choice
    (x - x) % 3 = 0 → Tie

Case 2: Computer wins
    Rock(0) beats Scissors(2) → (0 - 2) % 3 = 1
    Paper(1) beats Rock(0)    → (1 - 0) % 3 = 1
    Scissors(2) beats Paper(1)→ (2 - 1) % 3 = 1

Case 3: User wins
    Scissors(2) beats Rock(0) → (0 - 2) % 3 = 2
    Rock(0) beats Paper(1)    → (1 - 0) % 3 = 2
    Paper(1) beats Scissors(2)→ (2 - 1) % 3 = 2

The modulo (%) ensures the result always stays in the range [0, 2],
which directly maps to the RESULTS list.
"""

outcome_index = (computer_choice - user_choice) % 3


# ------------------------------------------
# 4. OUTPUT
# ------------------------------------------
print(f"\nYou: {CHOICES[user_choice]}")
print(f"Computer: {CHOICES[computer_choice]}")
print(f"Result: {RESULTS[outcome_index]}")
