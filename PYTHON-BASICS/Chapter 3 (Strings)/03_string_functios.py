#FUNCTIONS OF STRING

#1. len() function
    # len() function returns the length of the string

name = "Shivu"

# --- Approach 1: Direct Print ---

print(len(name)) 
# This calculates the length (5) and immediately prints the result to the console.

# --- Approach 2: Store then Print ---

length_of_name = len(name) 
# This calculates the length (5) and stores the result in a new variable called 'length_of_name'.

print(length_of_name) 
# This retrieves the stored value (5) from the variable and prints it to the console.

#2. String.endswith() function
    # The endswith() function checks if the string ends with the specified suffix.

name = "Shivu"
print(name.endswith("vu"))  # returns True
print(name.endswith("hi"))  # returns False

filename = "document.txt"
print(filename.endswith(".txt"))  # returns True
print(filename.endswith(".pdf"))  # returns False

#3. String.count() function
    # The count() function returns the number of occurrences of a substring in the given string.

name = "Shivansh Shivansh"
print(name.count("h"))  # returns 4
print(name.count("Shiv"))  # returns 2
print(name.count("s"))  # returns 2 (case-sensitive)
print(name.count("S"))  # returns 2 (case-sensitive)
print(name.count("z"))  # returns 0 # substring not found

#4. String.capitalize() function
    # The capitalize() function converts the first character of the string to uppercase. 

name = "shivansh yadav"

capitalized_string = name.capitalize()
print(capitalized_string)  # returns 'Shivansh yadav'

print(name.capitalize())  # returns 'Shivansh yadav'
# Note: Only the first character is capitalized; the rest of the string remains unchanged.

#5. String.find() function
        # The find() function returns the lowest index of the substring if found in the string. 
        # If not found, it returns -1.

name = "Shivansh Yadav"
print(name.find("Yadav"))  # returns 9 (starting index of substring)
print(name.find("shiv"))  # returns -1 (substring not found, case-sensitive)
print(name.find("a"))  # returns 4 (first occurrence of 'a')
print(name.find("s"))  # returns 6 (first occurrence of 's')
print(name.find("z"))  # returns -1 (substring not found)


#6. String.replace() function
    # The replace() function replaces the old wrold with new word in the string.
    #It replaces all the occurences of the old word with new word.

name = "Shivansh Yadav"
print(name.replace("Shivansh", "Shivu"))  # returns 'Shivu Yadav'
print(name.replace("Yadav", "Yaduvanshi")) # returns 'Shivansh Yaduvanshi'
print(name.replace("yadav", "Yaduvanshi")) # returns 'Shivansh Yadav' (case-sensitive, no change)
# We can copy the line using ALT + SHIFT + DOWN ARROW
new_name = name.replace("Yadav", "Singh")
print(new_name)  # returns 'Shivansh Singh'


#7. String.lower() function
    # The lower() function converts all uppercase characters in a string to lowercase.

name = "Shivansh Yadav"
print(name.lower())  # returns 'shivansh yadav'
print("HELLO WORLD".lower())  # returns 'hello world'
print("Python3 Is AwEsOmE".lower())  # returns 'python3 is awesome'


#8. String.upper() function
    # The upper() function converts all lowercase characters in a string to uppercase.

name = "Shivansh Yadav"
print(name.upper())  # returns 'SHIVANSH YADAV'
print("hello world".upper())  # returns 'HELLO WORLD'
print("Python3 Is AwEsOmE".upper())  # returns 'PYTHON3 IS AWESOME'


#9. String.split() function
    # The split() function splits a string into a list of substrings based on a specified delimiter.

name = "Shivansh Yadav"
print(name.split())  # returns ['Shivansh', 'Yadav'] (default delimiter is space)  
print("apple,banana,cherry".split(","))  # returns ['apple', 'banana', 'cherry'] (delimiter is comma)
print("one;two;three;four".split(";"))  # returns ['one', 'two', 'three', 'four'] (delimiter is semicolon)
#Insersts space in place of delimiter, i.e., semicolon
print("one;two;three;four".replace(";", " ").split(" ")) # returns ['one', 'two', 'three', 'four']
print("a b c d e".split(" "))  # returns ['a', 'b', 'c', 'd', 'e'] (delimiter is space)
print("2024-06-15".split("-"))  # returns ['2024', '06', '15'] (delimiter is hyphen)


#10. String.join() function
    # The join() function joins the elements of an iterable (like a list or tuple)
    # into a single string, with a specified separator between each element.

words = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)
print(sentence)  # returns 'Hello world from Python' (space as separator)

fruits = ["apple", "banana", "cherry"]
csv = ",".join(fruits)
print(csv)  # returns 'apple,banana,cherry' (comma as separator)

dates = ["2024", "06", "15"]
date_string = "-".join(dates)
print(date_string)  # returns '2024-06-15' (hyphen as separator)

letters = ['a', 'b', 'c', 'd']
joined_letters = "".join(letters)
print(joined_letters)  # returns 'abcd' (no separator)  

#11. String.strip() function
    # The strip() function removes any leading and trailing whitespace characters from the string.  

name = "   Shivansh Yadav   "
print(name.strip())  # returns 'Shivansh Yadav' (whitespaces removed from both ends)

greeting = "\tHello, World!\n"
print(greeting.strip())  # returns 'Hello, World!' (tabs and newlines removed)

padded_string = "   Python Programming   "
print(padded_string.strip())  # returns 'Python Programming' (whitespaces removed from both ends)  

#12. String.startswith() function
    # The startswith() function checks if the string starts with the specified prefix. 

name = "Shivansh Yadav"
print(name.startswith("Shi"))  # returns True
print(name.startswith("Yadav"))  # returns False

filename = "document.txt"
print(filename.startswith("doc"))  # returns True
print(filename.startswith("txt"))  # returns False

url = "https://www.example.com"
print(url.startswith("https://"))  # returns True
print(url.startswith("www.")) #returns False

#13. String.isdigit() function
    # The isdigit() function checks if all characters in the string are digits (0-9).

num = "12345"
print(num.isdigit())  # returns True

alpha = "Shivansh"
print(alpha.isdigit())  # returns False

mixed = "123abc"
print(mixed.isdigit())  # returns False

empty = ""
print(empty.isdigit())  # returns False


#14. String.isalpha() function
    # The isalpha() function checks if all characters in the string are alphabetic (a-z, A-Z).

name = "Shivansh"
print(name.isalpha())  # returns True

num = "12345"
print(num.isalpha())  # returns False   

mixed = "Shivu123"
print(mixed.isalpha())  # returns False

empty = ""
print(empty.isalpha())  # returns False


#15. String.isspace() function
    # The isspace() function checks if all characters in the string are whitespace characters (spaces, tabs, newlines).
    
whitespace_str = "   \t\n"
print(whitespace_str.isspace())  # returns True

non_whitespace_str = "  Hello  "
print(non_whitespace_str.isspace())  # returns False

str = "\n Shivansh \n\t" 
print(str.isspace())  # returns False

empty_str = ""
print(empty_str.isspace())  # returns False


#16. String.title() function
    # The title() function converts the first character of each word in the string to uppercase 
    # and the rest to lowercase.

name = "shivansh yadav"
print(name.title())  # returns 'Shivansh Yadav'

sentence = "hello world from python"
print(sentence.title())  # returns 'Hello World From Python'

mixed_case = "pYtHoN pRoGrAmMiNg"
print(mixed_case.title())  # returns 'Python Programming'

empty_str = ""
print(empty_str.title())  # returns '' (empty string remains unchanged)

#17. String.zfill() function
    # The zfill() function pads the string on the left with zeros (0) until it reaches the specified width.

num_str = "42"
print(num_str.zfill(5))  # returns '00042' (pads with three zeros)

short_str = "7"
print(short_str.zfill(3))  # returns '007' (pads with two zeros)

long_str = "12345"
print(long_str.zfill(3))  # returns '12345' (no padding, string is already long enough)

empty_str = ""
print(empty_str.zfill(4))  # returns '0000' (pads with four zeros)


#18. String.center() function
    # The center() function centers the string within a specified width by padding it with spaces on both sides.    

text = "Hello"
print(text.center(11))  # returns '   Hello   ' (pads with 3 spaces on each side)

text = "Python"
print(text.center(14))  # returns '    Python    ' (pads with 4 spaces on each side)

text = "Data"
print(text.center(8))  # returns '  Data  ' (pads with 2 spaces on each side)   

text = "Centered"
print(text.center(6))  # returns 'Centered' (no padding, string is already long enough)


#19. String.swapcase() function
    # The swapcase() function converts uppercase characters to lowercase and lowercase characters to uppercase.

text = "Hello World"
print(text.swapcase())  # returns 'hELLO wORLD'

text = "sHIVANSH yADAV"
print(text.swapcase())  # returns 'Shivansh Yadav'

text = "Python3 Is AwEsOmE"
print(text.swapcase())  # returns 'pYTHON3 iS aWeSoMe'

empty_str = ""
print(empty_str.swapcase())  # returns '' (empty string remains unchanged)


#20. String.format() function
    # The format() function formats specified values in a string.

name = "Shivansh"
age = 20   
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # returns 'My name is Shivansh and I am 20 years old.'

print("Hello, {}! You are {} years old.".format("Shivu", 21))  # returns 'Hello, Shivu! You are 21 years old.'

print("The temperature is {}°C.".format(25))  # returns 'The temperature is 25°C.'

print("Coordinates: ({}, {})".format(10.5, 20.3))  # returns 'Coordinates: (10.5, 20.3)'


#21. String.partition() function
    # The partition() function splits the string at the first occurrence of the specified separator

text = "Hello, world! Welcome to Python."
partitioned = text.partition("world")
print(partitioned)  # returns ('Hello, ', 'world', '! Welcome to Python

text = "one;two;three;four"
partitioned = text.partition(";")
print(partitioned)  # returns ('one', ';', 'two;three;four')

text = "no separator here"
partitioned = text.partition("xz")
print(partitioned)  # returns ('no separator here', '', '') as there is no separator defined .


