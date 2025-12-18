# ESCAPE SEQUENCE CHARACTERS IN STRINGS

# 1. Including Double/Single Quotes in a String

a = "Shivansh is good at \"Python\" programming."
a1 = "Shivansh is good at \'Python\' programming."
# The backslash (\) is used as an escape character to include double quotes inside the string.
# Without the backslash, the string would terminate at the first double quote.
print(a)  # Output: Shivansh is good at "Python" programming.
print(a1)  # Output: Shivansh is good at 'Python' programming.


# 2. Including Single Quotes in a String

b = 'It\'s a beautiful day.'
# The backslash (\) is used to include a single quote inside a string that is enclosed in single quotes.
print(b)  # Output: It's a beautiful day.


# 3. NewLine Character

c = "I am  Shivansh Yadav.\nI am learning Python."
# The \n escape sequence is used to insert a new line in the string.
print(c)
# Output:
#I am Shivansh Yadav.
# I am learnin g Python.


# 4. Tab Character

d = "Name:\tShivansh Yadav"
# The \t escape sequence is used to insert a tab space in the string.
print(d)  # Output: Name:	Shivansh Yadav


# 5. Backslash Character

e = "This is a backslash: \\"
# The double backslash (\\) is used to include a single backslash in the string.
print(e)  # Output: This is a backslash: \


# 6. Carriage Return Character

f = "Hello World! \rPython"
# The \r escape sequence is used to move the cursor to the beginning of the line.
# Everything after \r overwrites at the beginning of the string, replacing current content with respective indexes
# and length occupy the same positions including spaces if the character is larger in length than previous content.
print(f)  # Output: PythonWorld!


# 7. Form Feed Character

g = "Hello\fWorld!"
# The \f escape sequence is used to insert a form feed in the string.
# It is treated as \n (new line) in many environments.
print(g)  # Output: HelloWorld!
# Note: The form feed character may not produce visible effects in all environments.


# 8. Backspace Character

h = "Hello\bWorld!"
# The \b escape sequence is used to insert a backspace in the string.
print(h)  # Output: HellWorld!
# Note: The backspace character may not produce visible effects in all environments.


# 9. Unicode Character

i = "This is a unicode character: \u03B3"
# The \u escape sequence is used to include a unicode character in the string.
# Here, \u03B3 represents the Greek letter gamma (γ).
# The uicode escape sequence is followed by a four-digit hexadecimal number.
# Each unicode character is represented by a unique code point.
print(i)  # Output: This is a unicode character: γ


# 10. Raw Strings

j = r"This is a raw string with a backslash: \n \t \\"
# The r prefix before the string indicates that it is a raw string.
# In raw strings, escape sequences are not processed, and backslashes are treated as literal characters.
print(j)  # Output: This is a raw string with a backslash: \n \t \\

# SUMMARY:
# Escape sequences are special characters used in strings to represent certain whitespace characters,
# special symbols, or to include quotes within strings.
# They are preceded by a backslash (\) and have specific meanings.
# Common escape sequences include:
    # - \" : Double quote  
    # - \' : Single quote
    # - \n : New line
    # - \t : Tab
    # - \\ : Backslash
    # - \r : Carriage return
    # - \f : Form feed
    # - \b : Backspace
    # - \u : Unicode character
    # Raw strings (prefixed with r) treat backslashes as literal characters, ignoring escape sequences.
