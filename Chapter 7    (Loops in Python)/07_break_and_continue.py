# Break in for loop
#    'break' is used to come out of the loop when encountered. It instructs the program to -- exit the loop now.

for i in range(100):
    if( i == 35):
        break # when i becomes 35 the loop will terminate. Exits at 35 printing 34 as last item. THE LOOP EXITS WHEN  BREAK IS ENCOUNTERED.
    print(i) 

#Continue in for loop
#     'continue' is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to "skip this iteration"
for i in range(100):
    if(i == 34):
        continue # Skip this iteration (it skips the value at 34 and continues the loop from 35)
    print(i)

