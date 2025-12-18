# Write a program to find out whether a given post is talking about "Shivansh" or not.

post = input ("Enter the post content: ")
if ("Shivansh".lower() in post.lower()):
    #This will make the check case insensitive wither the input is in upper case or lower case or mixed.
    print("The post is talking about Shivansh.")
else:
    print("The post not related to Shivansh")