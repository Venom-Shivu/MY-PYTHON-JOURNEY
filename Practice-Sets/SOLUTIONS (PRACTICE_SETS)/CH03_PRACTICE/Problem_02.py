""" Write a program to fill in a letter template given below with name and date.
letter = '''
    Dear <|NAME|>,
    You are selected!
    Date: <|DATE|>'''
"""

letter = '''
Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''

print(letter.replace("<|NAME|>","Shivansh Yadav").replace("<|DATE|>","26 November 2024"))
# The above syntax is chainning two replace() methods to replace both placeholders .
# The replace() method is used to replace occurrences of a specified substring with another substring.

#Another way to do this is by using f-strings (formatted string literals) in Python.

print(letter.replace("<|NAME|>",f"{input('Enter your name: ')}").replace("<|DATE|>",f"{input('Enter the date: ')}"))
# Here, we use the input() function to get the user's name and date, and then we 
# use f-strings to format the replacements in the letter template.
