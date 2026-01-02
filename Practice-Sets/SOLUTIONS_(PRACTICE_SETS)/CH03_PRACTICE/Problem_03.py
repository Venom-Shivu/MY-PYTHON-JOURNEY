# WRITE A PROGRAM TO DETECT DOUBLE SPACES IN A STRING.


name = " Shivansh is good at  Python  Programming"

# 1st Way to do this is by using the find() method to locate double spaces.

print(name.find("  ")) # Output: Index of first occurrence of double spaces, -1 if not found.
# It tells the index of the substring if found else returns -1.

#2nd Way to do this is by using the 'in' keyword to check for double spaces.

double_spaces = "  "  # Two consecutive spaces

if double_spaces in name:
    print("The string contains double spaces.")
else:
    print("The string does not contain double spaces.")

#3rd way to do this by using the count() method to count occurrences of double spaces.

count_double_spaces = name.count(double_spaces)
if count_double_spaces > 0:
    print(f"The string contains double spaces {count_double_spaces} times.")
else:
    print("The string does not contain double spaces.")