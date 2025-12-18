                                     # FOR LOOP IN PYTHON

# It functions similar to WHILE LOOP.
# It is used to itrate through a sequence like list, tuple, or string[iterables]

for i in range(5): # range() function is used to generate a sequance of numbers
    print(i)
# It prints from 0 to (Range-1) value, as it starts from 0 unless i is specified to start from other value.


""" 
RANGE() Function: 
In Python range() function is used to generate a sequence of number
We can also specify the start, stop and step_size as follows:
       SYNTAX: range(start, stop, step_size)
               #step_size is usually not used with range()

"""

for i in range(1, 100, 4):
    print(i)
# it returns the numbers starting from 1 with a step of 4
# The steps in for loop work same as string slicing.

for p in range(0,7):
    print(p+1) # The numbers will print from 1 to 7 as print is specified with (p+1)




