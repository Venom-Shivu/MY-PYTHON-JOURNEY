        # Write a program to print multiplication table of n using for loops in reversed order.

n= int(input("Enter the number for the multiplication table: "))
# The loop will run 10 times (from i=1 up to i=10).
for i in range(1, 11):
# Calculate the multiplier in reverse order (10, 9, 8, ..., 1).
    # When i=1, the multiplier is 11 - 1 = 10.
    # When i=10, the multiplier is 11 - 10 = 1.
    # So we can directly use (11-i) as i increases the table coming to it's original form in reverse order like (11-1)=10,(11-2)=9,(11-3)=8 and so on
    print(f"{n} X {11-i} = {n*(11-i)}")


# In another way We can use advanced version of range
# we can use range() more effectively taking negative steps range starting from 10 to 0, with step of -1
p = int(input("Enter the Number for reversed multiplication: "))
for i in range(10,0,-1):
    print(f"{p} X {i} = {p*i}")