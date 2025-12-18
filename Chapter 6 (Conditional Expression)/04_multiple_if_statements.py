                #Logical Operators in Python
#1. "AND": Returns true if both the operand/statements are true.
#2. "OR" : Returns true if atleast on operand/Statement are true.
#3. "NOT" : It returns the Inverterd value : not(True)= False,not(False)=True, not(a)=b


                    # Multiple If statements in Python
a = int(input("Enter your age: "))

# If Statement Number 1
if(a%2 == 0):
    print(f"{a} is Even Number")
#End Of IF Statement 1, this is independent IF statement.

# If Statement number 2
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

# End Of IF Statement 2

else:
    print("You are a teenager and do not have right to vote")
 # Last else is executed only if all the conditions inside Elif Fails    