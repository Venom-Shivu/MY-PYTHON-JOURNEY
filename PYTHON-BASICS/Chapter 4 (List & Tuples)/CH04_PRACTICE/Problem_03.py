# To check that the TUPLE type() cannot be changed in Python.

# my_tuple = (1, 2, 6, 58, "Shivansh")

# print("Original tuple:", my_tuple)

# my_tuple[2] = 100
# print("Tuples are immutable; you cannot change their elements.")
# print("Tuple after attempted modification:", my_tuple) #printing the tuple after attempted modification


#another exapmle

a = (10,20,30,"Shiva")

a[3] = "Shivansh" # This will raise an error because tuples are immutable
#Shows an error without any print statement: 'tuple' object does not support item assignment
print(a)