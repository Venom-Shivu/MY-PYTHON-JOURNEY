#Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter Your Username: ")

if(len(username) < 10):
    print(f"Username is Valid contains : {len(username)} characters")
else:
    print(f"Username is Invalid contains : {len(username)} characters which are greater than or equal to predefined limit ")