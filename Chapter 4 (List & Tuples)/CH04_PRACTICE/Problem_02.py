#Program to accept marks of 6 students and display them in a sorted manner.

 # Initializing an empty list to store marks

marks = []

f1 = int(input("Enter marks : "))
marks.append(f1)
f2 = int(input("Enter marks : "))
marks.append(f2)
f3 = int(input("Enter marks : "))
marks.append(f3)
f4 = int(input("Enter marks : "))
marks.append(f4)
f5 = int(input("Enter marks : "))
marks.append(f5)
f6 = int(input("Enter marks : "))
marks.append(f6)
marks.append(f6)
marks.sort()
print( marks)

#Another way to write the same program
marks = []
for i in range(6):
    marks_input = int(input(f"Enter Marks of the Student {i+1}: "))
    marks.append(marks_input)

    marks.sort()
print("Sorted marks of the students:", marks)
