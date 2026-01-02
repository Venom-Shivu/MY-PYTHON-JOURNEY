'''
The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt'
which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function
breaks the Hi-score.
 '''

import random

def game():
    """
    This function simulates a game.
    It generates a random score and updates the high score stored in a file
    if the current score is greater than the previous high score.
    """

    # Inform the user that the game has started
    print("You are playing the game...")

    # Generate a random score between 1 and 100
    score = random.randint(1, 100)

    # Open the high-score file in read mode
    # This file stores the best score achieved so far
    with open("Hi-score.txt", "r") as file:
        content = file.read()

    # If the file is empty, assume the high score is 0
    # Otherwise, convert the stored value to an integer
    if content == "":
        high_score = 0
    else:
        high_score = int(content)

    # Display the current score and previous high score
    print(f"Your Score: {score}")
    print(f"Previous High Score: {high_score}")

    # Compare current score with stored high score
    # Update the file only if a new high score is achieved
    if score > high_score:
        with open("Hi-score.txt", "w") as file:
            file.write(str(score))
        print("New High Score Updated!")

    # Return the current score
    return score


# Call the game function to start playing
game()
