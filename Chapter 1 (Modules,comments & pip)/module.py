# pip install pyjokes (This will install the external module pyjokes)
import pyjokes

print("Printing Jokes...")
# This is a random single line comment.
# Yet another line
# Again another one

""" This is a multi line comment. The content inside the tripple quotes won't 
print or give any syntax errror
"""

joke = pyjokes.get_joke()
print (joke)