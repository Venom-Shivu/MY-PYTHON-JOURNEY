                                     #IF ELIF ELSE LADDER


a = int(input("Enter your age: "))

#If Elif else Ladder

if(a>=18):
    print("You are an adult and have right to vote in elections")
    print("No need for conset")
# Returns the first result if the conditon is true.

elif(a<0):
    print("You are entering an invalid negative age")
# returns the otherwise result if user is entering an invalid input

elif(a==0):
    print("Oo-Oo! You entered zero, which is not a valid age, try to enter a valid age")
#Elif in pythin means "Else If". An if statement can be changes together with a lot of these Elof statements followed by an Else.


else:
    print("You are a teenager and do not have right to vote")
#Returns the result if first condition is not true.

print(" End Of Program")
#This print() statement is not under any of the conditions, if any of the conditions are true the program reach here.
# Only one of the above condition execute the the ladder reaches end of the program or outside the conditional statements.

