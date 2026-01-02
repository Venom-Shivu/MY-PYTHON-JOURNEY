"""
Write a program to find out whether a student has passed or failed if it requires a total of 40% and at
least 33% in each subject to pass. Assume 3 subjects and take marks as input from the user.
"""
marks_subject1 = int(input("Enter Marks obtained in Subject 1: "))
marks_subject2 = int(input("Enter Marks obtained in Subject 2: "))
marks_subject3 = int(input("Enter Marks obtained in Subject 3: "))

# Check for Total Percentage
total_percentage = (marks_subject1 + marks_subject2 + marks_subject3)*100 / 300

if(total_percentage >= 40):
    print(f"Congratulations! You are Passed.\nYour percentage is : {total_percentage}")

else:
    print(f"Oo-Oo! You are Failed, Try again next year.\nYour percentage is : {total_percentage}")

if(marks_subject1 < 33):
    print(f"\nYou are Failed in Subject 1, try agian with ReExam or Compartment.")
elif(marks_subject2 < 33):
    print(f"\nYou are Failed in Subject 2, try agian with ReExam or Compartment.")
elif(marks_subject3 <33):
    print(f"\nYou are Failed in Subject 3, try agian with ReExam or Compartment.")