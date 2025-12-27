""" A program to create a dictionary of Hindi words with values as their English translation.
                        Provide user with an option to look it up."""

# Step 1: Creatibg a Dictionary with hindi words with english meaning
words = {
    "Dhanyawad": "Thank You",
    "Kripya" : "Please",
    "Maaf Kijiye" : "Sorry/Excuse Me",
    "Chai" : "Tea",
    "Khana" : "Eat",
    "Pani" : "Water",
    "Doodh" : "Milk",
    "Padhna" : "Read",
    "Likhna" : "Write",
    "Samay" : "Time",
    "Baithna" : "Sit",
    "Chalna" : "Walk"
}

# Step 2: Print a welcome message for the user
print(f"The Hindi words whose meaning is available in english are:{words.keys()}\n")
#output:The Hindi words whose meaning is available in english are:
# dict_keys(['Dhanyawad', 'Kripya', 'Maaf Kijiye', 'Chai', 'Khana', 'Pani', 'Doodh', 'Padhna', 'Likhna', 'Samay', 'Baithna', 'Chalna'])
print("Welcome to the Hindi-English Dictionary!")
print("Type a Hindi word to get its English meaning.")
print("Type 'exit' to quit.\n")

# Step 3: Use a loop to keep asking the user for input until they type 'exit'
while True:
    # Ask the user to enter a Hindi word
    user_input = input("Enter a Hindi word: ")

    # Step 4: Check if the user wants to exit
    if user_input.lower() == "exit":
        print("Goodbye! 👋")  # Friendly exit message
        break  # End the loop

    # Step 5: Look up the word in the dictionary
    meaning = words.get(user_input)  # .get() returns None if word not found

    # Step 6: Show the result
    if meaning:
        # If word is found, print its meaning
        print(f"English meaning of '{user_input}' is: {meaning}\n")
    else:
        # If word is not found, show an error message
        print("Sorry, word not found in dictionary.\n")


