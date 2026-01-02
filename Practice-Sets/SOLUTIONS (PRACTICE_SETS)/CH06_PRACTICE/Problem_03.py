"""

A spam comment is defined as a text containing the following keywords:
"Make a lot of Money", "Buy Now", "Subscribe this", "Click This".
Write a program to detect these spam comments.

"""
p1 = "Make a lot of Money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"\

message = input("Enter your Comment: ")

if(p1.lower() in message.lower()) or (p2.lower() in message.lower()) or (p3.lower() in message.lower()) or (p4.lower() in message.lower()):
    #This will check the comment either it is in upper case or lower case or mixed.
    print("This is Spam Comment")
else:
    print(f"Thank you for your comment.\nWaiting to hear you next time.") 

