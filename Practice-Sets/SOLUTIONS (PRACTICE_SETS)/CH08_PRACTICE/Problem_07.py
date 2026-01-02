    # Write a python function to remove a given word from a list and strip it at the same time.


# Function to clean and filter a list

# 'word_list' is the list we want to process
# 'word_to_remove' is the specific name we want to kick out
def remove_and_strip(word_list, word_to_remove):
    newlist = []  # Create a fresh, empty list to store the results
    
    # Loop through every item in the original list one by one
    for item in word_list:
        
        # 1. CHECK: Only proceed if the current item is NOT the word we want to remove
        if not item == word_to_remove:
            
            # 2. STRIP: Remove any accidental spaces at the start or end of the word
            # 3. APPEND: Add the cleaned word into our new list
            newlist.append(item.strip())
            
    # Give back the final list after the loop finishes
    return newlist

# --- MAIN PROGRAM ---
# Our original list of names
names = ["Shivansh", "Shivam", "Abhay", "Ananya", "Shubhankar", "Divya"]

# Call the function and tell it to remove "Abhay"
# Note: It will also strip spaces from other names if they have any!
cleaned_names = remove_and_strip(names, "Abhay")

print(cleaned_names)
