# Program to sum a list with 4 numbers .

numbers = [34,45,68,999]

total = sum(numbers) #sum function to sum the list

print("The sum of the list is:", total)

#another way if user input the number to sum

l = []
for i in range(4):
	num = int(input(f"Enter number {i+1}:"))
	l.append(num)
total = sum(l)
print("The sum of the list is:", total)