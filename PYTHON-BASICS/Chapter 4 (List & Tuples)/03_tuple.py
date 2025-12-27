                #TUPLES 
#Tuple is a collection which is ordered and unchangeable(immutable). Allows duplicate members.
#Tuple is written with round brackets.
# Tuples can contain items of different data types.

    #Creating a Tuple

tuple1 = () # Empty Tuple
print(tuple1)

tuple2 = (1,) # Tuple with single element needs a comma.
print(tuple2)

tuple3 = (10, 20, 30, "Shivansh", 45.67, True, "Rahul", 10) # Tuple with multiple elements
print(tuple3)

    #Accessing Tuple Items/Slicing

print(tuple3[1])    # Accessing the second item of the tuple
print(tuple3[-1])   # Accessing the last item of the tuple
print(tuple3[2:5])  # Accessing a range of items (from index 2 to 5, excluding 5)

    #Tuples are immutable
# The elements of a tuple cannot be changed or modified after the tuple has been created.
# However, you can create a new tuple by concatenating or slicing existing tuples.
# Example of concatenation
tuple4 = tuple3 + (99, 100)
print("After concatenation:", tuple4)

# Example of slicing
tuple5 = tuple3[1:4]
print("After slicing:", tuple5)


