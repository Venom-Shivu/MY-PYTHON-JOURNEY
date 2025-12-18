# A program to input eight numbers from the user and display all the unique numbers (once)
s = set()
for i in range(8):
    n= int(input(f"Enter Number {i+1}: "))
    s.add(n)
""" 
print(s) As this print is inside the loop so the set will print after each number entry.
 If we have to print the complete set at once we have to run print outside the loop
Output in this case:Enter Number 1: 5
                    {5}
                    Enter Number 2: 2
                    {2, 5}
                    Enter Number 3: 16
                    {16, 2, 5}
                    Enter Number 4: 1
                    {16, 1, 2, 5}
                    Enter Number 5: 041
                    {1, 2, 5, 41, 16}
                    Enter Number 6: 1
                    {1, 2, 5, 41, 16}
                    Enter Number 7: 0
                    {0, 1, 2, 5, 41, 16}
                    Enter Number 8: 6
                    {0, 1, 2, 5, 6, 41, 16}

 """
print("Unique Numbers   are:",s)
'''Output:Enter Number 1: 5
Enter Number 2: 5
Enter Number 3: 53
Enter Number 4: 43
Enter Number 5: 45
Enter Number 6: 4
Enter Number 7: 4
Enter Number 8: 44
{4, 5, 43, 44, 45, 53}'''

