# Attempt to solve Problem 01 using while loop.(Multiplication Table)

input_number = int(input("Enter a number to print its multiplication table: "))

i = 1
while i <= 10:
    print(f"{input_number} X {i} = {input_number * i}")

    i = i+1