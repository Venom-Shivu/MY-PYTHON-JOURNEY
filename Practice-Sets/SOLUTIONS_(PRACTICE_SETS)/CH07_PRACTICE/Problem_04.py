# Write a program to find whether a given number is prime or not.

# To store the numbers as an interger.
input_number = int(input("Enter a number to check if it is prime or not: "))

for i in range(2, input_number):
    if(input_number % i) == 0: # The entered number is divided by any number with remainder == 0
        print("The Number you have entered is not prime")
        break # This will stop the iteration when the number is checked once and is divisible.
else:
    print("The number you have entered is Prime.")
