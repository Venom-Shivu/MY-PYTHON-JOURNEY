"""
Wrire a python funtion to print first n lines of the following star pattrern:
* * *
 * *            --- For n =  3
  *
                                """
# Function definition: Takes 'n' as the starting number of stars
def pattern(n):
    # --- BASE CASE ---
    # Every recursive function needs a 'Stop' condition.
    # If n reaches 0, we return (stop) so we don't go into an infinite loop.
    if (n == 0):
        return
    
    # --- ACTION (PRINTING) ---
    # This prints the character '*' n times on the current line.
    # Note: In Python, "string" * n repeats that string.
    print("*" * n)
    
    # --- RECURSIVE STEP ---
    # We call the same function but with (n - 1).
    # This ensures that the NEXT time the function runs, it prints one less star.
    pattern(n - 1)

# --- USER INPUT ---
# We convert the input to an integer because input() always returns a string.
n = int(input(" Enter the Number to print the Star pattern: "))

# --- EXECUTION ---
# We call the function. Note: This function doesn't 'return' a value to be saved, 
# it just prints directly to the console.
pattern(n)

# For reverse printing of above like bottom have n number of starts with top has 1

def pattern(n):
    # BASE CASE
    if (n == 0):
        return
    
    # RECURSIVE STEP
    # We call the function first. This "waits" until the smaller calls are done.
    pattern(n - 1)
    
    # ACTION (PRINTING)
    # This line only runs AFTER the line above finishes its work.
    print("*" * n)

n = int(input("Enter the Number: "))
pattern(n)